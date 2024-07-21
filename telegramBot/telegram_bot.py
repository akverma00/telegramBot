import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load environment variables from .env file
load_dotenv()

# Constants
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
SESSION_NAME = 'session_name'
TARGET_CHAT_IDS = [
    -1001945508703,
    -1001833328420,
    -1001905014374,
    -1002121131434,
    -1002133513866,
    -1002056442424
]
SOURCE_CHAT_IDS = [
    -1002008905623,
    -1001809265514
]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Telegram client
client = TelegramClient(SESSION_NAME, TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def send_to_groups(event):
    for chat_id in TARGET_CHAT_IDS:
        try:
            await client.send_message(chat_id, event.message)
            logger.info(f"Message forwarded to chat ID {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send message to chat ID {chat_id}: {e}")

@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def handler(event):
    await send_to_groups(event)

def start_bot():
    with client:
        logger.info("Welcome back!!!")
        client.run_until_disconnected()