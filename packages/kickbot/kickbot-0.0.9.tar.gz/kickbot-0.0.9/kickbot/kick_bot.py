import asyncio
import json
import logging
import websockets

from datetime import timedelta
from typing import Callable, Optional

from .constants import KickBotException
from .kick_client import KickClient
from .kick_message import KickMessage
from .kick_moderator import Moderator
from .kick_helper import (
    get_ws_uri,
    get_streamer_info,
    get_current_viewers,
    get_chatroom_settings,
    get_bot_settings,
    message_from_data,
    send_message_in_chat,
    send_reply_in_chat
)

logger = logging.getLogger(__name__)


class KickBot:
    """
    Main class for interacting with the Bot API.
    """
    def __init__(self, username: str, password: str) -> None:
        self.client: KickClient = KickClient(username, password)
        self._ws_uri = get_ws_uri()
        self._socket_id: Optional[str] = None
        self.streamer_name: Optional[str] = None
        self.streamer_slug: Optional[str] = None
        self.streamer_info: Optional[dict] = None
        self.chatroom_info: Optional[dict] = None
        self.chatroom_settings: Optional[dict] = None
        self.chatroom_id: Optional[int] = None
        self.bot_settings: Optional[dict] = None
        self.is_mod: bool = False
        self.is_super_admin: bool = False
        self.moderator: Optional[Moderator] = None
        self.handled_commands: dict[str, Callable] = {}
        self.handled_messages: dict[str, Callable] = {}
        self.timed_events: list[tuple[timedelta, Callable]] = []
        self._is_active = True

    def poll(self):
        """
        Main function to activate the bot polling.
        """
        try:
            asyncio.run(self._poll())
        except KeyboardInterrupt:
            logger.info("Bot stopped.")
            return

    def set_streamer(self, streamer_name: str) -> None:
        """
        Set the streamer for the bot to monitor.

        :param streamer_name: Username of the streamer for the bot to monitor
        """
        if self.streamer_name is not None:
            raise KickBotException("Streamer already set. Only able to set one streamer at a time.")
        self.streamer_name = streamer_name
        self.streamer_slug = streamer_name.replace('_', '-')
        get_streamer_info(self)
        get_chatroom_settings(self)
        get_bot_settings(self)
        if self.is_mod:
            self.moderator = Moderator(self)
            logger.info(f"Bot is confirmed as a moderator for {self.streamer_name}...")
        else:
            logger.warning("Bot is not a moderator in the stream. To access moderator functions, make the bot a mod."
                           "(You can still send messages and reply's, bot moderator status is recommended)")

    def add_message_handler(self, message: str, message_function: Callable) -> None:
        """
        Add a message to be handled, and the asynchronous function to handle that message.

        Message handler will call the function if the entire message content matches (case-insensitive)

        :param message: Message to be handled i.e: 'hello world'
        :param message_function: Async function to handle the message
        """
        if self.streamer_name is None:
            raise KickBotException("Must set streamer name to monitor first.")
        message = message.casefold()
        if self.handled_messages.get(message) is not None:
            raise KickBotException(f"Message: {message} already set in handled messages")
        self.handled_messages[message] = message_function

    def add_command_handler(self, command: str, command_function: Callable) -> None:
        """
        Add a command to be handled, and the asynchronous function to handle that command.

        Command handler will call the function if the first word matches (case-insensitive)

        :param command: Command to be handled i.e: '!time'
        :param command_function: Async function to handle the command
        """
        if self.streamer_name is None:
            raise KickBotException("Must set streamer name to monitor first.")
        command = command.casefold()
        if self.handled_commands.get(command) is not None:
            raise KickBotException(f"Command: {command} already set in handled commands")
        self.handled_commands[command] = command_function

    def add_timed_event(self, frequency_time: timedelta, timed_function: Callable):
        """
        Add an event function to be called with a frequency of frequency_time.
        A tuple containing (time, function) will be added to self.timed_events.
        Once the main event loop is running, a task is created for each tuple.

        :param frequency_time: Time interval between function calls.
        :param timed_function: Async function to be called.
        """
        if self.streamer_name is None:
            raise KickBotException("Must set streamer name to monitor first.")
        if frequency_time.total_seconds() <= 0:
            raise KickBotException("Frequency time must be greater than 0.")
        self.timed_events.append((frequency_time, timed_function))

    async def send_text(self, message: str) -> None:
        """
        Used to send text in the chat.
        reply_text below is used to reply to a specific users message.

        :param message: Message to be sent in the chat
        """
        if not type(message) == str or message.strip() == "":
            raise KickBotException("Invalid message. Must be a non empty string.")
        logger.debug(f"Sending message: {message!r}")
        r = send_message_in_chat(self, message)
        if r.status_code != 200:
            raise KickBotException(f"An error occurred while sending message {message!r}")

    async def reply_text(self, original_message: KickMessage, reply_message: str) -> None:
        """
        Used inside a command/message handler function to reply to the original message / command.

        :param original_message: The original KickMessage argument in the handler function
        :param reply_message: string to reply to the original message
        """
        if not type(reply_message) == str or reply_message.strip() == "":
            raise KickBotException("Invalid reply message. Must be a non empty string.")
        logger.debug(f"Sending reply: {reply_message!r}")
        r = send_reply_in_chat(self, original_message, reply_message)
        if r.status_code != 200:
            raise KickBotException(f"An error occurred while sending reply {reply_message!r}")

    def current_viewers(self) -> int:
        """
        Retrieve current viewer count for the stream

        :return: Viewer count as an integer
        """
        viewer_count = get_current_viewers(self)
        return viewer_count

    @staticmethod
    def set_log_level(log_level: str) -> None:
        """
        Set log level to your desired choice. By default, it is set to INFO.
        Debug will show alot more, including all inbound messages
        """
        log_level = log_level.upper()
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level in valid_levels:
            logger.setLevel(log_level)
        else:
            logger.warning(f"Invalid log level: {log_level}")

    ########################################################################################
    #    INTERNAL FUNCTIONS
    ########################################################################################

    async def _poll(self) -> None:
        """
        Main internal function to poll the streamers chat and respond to messages/commands.
        Create a task for each timed event in self.timed_events.
        """
        for frequency, func in self.timed_events:
            asyncio.create_task(self._run_timed_event(frequency, func))

        async with websockets.connect(self._ws_uri) as self.sock:
            connection_response = await self._recv()
            await self._handle_first_connect(connection_response)
            await self._join_chatroom(self.chatroom_id)
            while True:
                try:
                    response = await self._recv()
                    if response.get('event') == 'App\\Events\\ChatMessageEvent':
                        await self._handle_chat_message(response)
                except asyncio.exceptions.CancelledError:
                    break
        logger.info(f"Disconnected from websocket {self._socket_id}")
        self._is_active = False

    async def _handle_chat_message(self, inbound_message: dict) -> None:
        """
        Handles incoming messages, checks if the message.content is in dict of handled commands / messages

        :param inbound_message: Raw inbound message from socket
        """
        message: KickMessage = message_from_data(inbound_message)
        if message.sender.username == self.client.bot_name:
            return

        content = message.content.casefold()
        command = message.args[0].casefold()
        logger.debug(f"New Message from {message.sender.username} | MESSAGE: {content!r}")

        if content in self.handled_messages:
            message_func = self.handled_messages[content]
            await message_func(self, message)
            logger.info(f"Handled Message: {content!r} from user {message.sender.username} ({message.sender.user_id})")

        elif command in self.handled_commands:
            command_func = self.handled_commands[command]
            await command_func(self, message)
            logger.info(f"Handled Command: {command!r} from user {message.sender.username} ({message.sender.user_id})")

    async def _join_chatroom(self, chatroom_id: int) -> None:
        """
         Join the chatroom websocket.

         :param chatroom_id: ID of the chatroom, mainly the streamer to monitor
         """
        join_command = {'event': 'pusher:subscribe', 'data': {'auth': '', 'channel': f"chatrooms.{chatroom_id}.v2"}}
        await self._send(join_command)
        join_response = await self._recv()
        if join_response.get('event') != "pusher_internal:subscription_succeeded":
            raise KickBotException(f"Error when attempting to join chatroom {chatroom_id}. Response: {join_response}")
        logger.info(f"Bot Joined chatroom {chatroom_id} ({self.streamer_name})")

    async def _handle_first_connect(self, connection_response: dict) -> None:
        """
        Handle the initial response received from the websocket.

        :param connection_response: Initial response when connecting to the socket
        """
        if connection_response.get('event') != 'pusher:connection_established':
            raise Exception('Error establishing connection to socket.')
        self._socket_id = json.loads(connection_response.get('data')).get('socket_id')
        logger.info(f"Successfully Connected to socket...")

    async def _run_timed_event(self, frequency_time: timedelta, timed_function: Callable):
        """
        Launched in a thread when a user calls bot.add_timed_event, runs until bot is inactive

        :param frequency_time: Frequency to call the timed function
        :param timed_function: timed function to be called
        """
        while self._is_active:
            await asyncio.sleep(frequency_time.total_seconds())
            await timed_function(self)
            logger.info(f"Timed Event Called")

    async def _send(self, command: dict) -> None:
        """
        Json dumps command and sends over socket.

        :param command: dictionary to convert to json command
        """
        await self.sock.send(json.dumps(command))

    async def _recv(self) -> dict:
        """
        Json loads command received from socket.

        :return: dict / json inbound socket command
        """
        return json.loads(await self.sock.recv())
