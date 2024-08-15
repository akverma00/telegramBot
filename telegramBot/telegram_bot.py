import os
import logging
import sys
from dotenv import load_dotenv
from telethon import TelegramClient, events

from Constants import Constants
from Validator import Validator


class TelegramBot:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.constants = Constants()
        # Constants
        self.TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
        self.TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
        self.SESSION_NAME = 'session_name'

        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Initialize Telegram client
        self.client = TelegramClient(self.SESSION_NAME, self.TELEGRAM_API_ID, self.TELEGRAM_API_HASH)

        # Register event handler
        self.client.on(events.NewMessage(chats=list(self.constants.SOURCE_TO_TARGET_MAP.keys())))(self.handler)

    async def send_to_groups(self, event):
        for chat_id in SOURCE_TO_TARGET_MAP.get(event.chat_id):
            try:
                await self.client.send_message(chat_id, event.message)
                self.logger.info(f"Message forwarded to chat ID {chat_id}")
            except Exception as e:
                self.logger.error(f"Failed to send message to chat ID {chat_id}: {e}")

    async def handler(self, event):
        if Validator.isMessageValidated(event.message.message, 
                                        self.constants.BLACKLIST_MESSAGES_MAP.get(event.chat_id), 
                                        self.constants.WHITELIST_MESSAGES_MAP.get(event.chat_id)):
            await self.send_to_groups(event)
        else:
            self.logger.info(f"Message from {event.chat_id} ignored: {event.message.message}")

    def start_bot(self):
        with self.client:
            self.logger.info("Welcome back!!!")
            self.client.run_until_disconnected()