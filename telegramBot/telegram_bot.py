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

# Dictionary mapping source chat IDs to lists of target chat IDs.
# Each key in the dictionary is a source chat ID, and 
# the corresponding value is a list of target chat IDs to which messages from the source chat should be forwarded.
SOURCE_TO_TARGET_MAP = {
    -1002008905623: [
        -1001833328420,
        -1002133513866,
        -1002056442424
    ],
    -1001809265514: [
        -1001945508703,
        -1001833328420,
        -1001905014374,
        -1002121131434,
        -1002133513866,
        -1002056442424
    ],
    -1001985321961: [
	-1001945508703,
	-1002056442424
    ]
}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Telegram client
client = TelegramClient(SESSION_NAME, TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def send_to_groups(event):
    for chat_id in SOURCE_TO_TARGET_MAP.get(event.chat_id):
        try:
            await client.send_message(chat_id, event.message)
            logger.info(f"Message forwarded to chat ID {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send message to chat ID {chat_id}: {e}")

# Function that ignores messages constains http and @ in the event.message.message
def isMessageValidated(message):
    if 'http' in message or '@' in message:
        return False
    return True

@client.on(events.NewMessage(chats=list(SOURCE_TO_TARGET_MAP.keys())))
async def handler(event):
    if isMessageValidated(event.message.message):
        await send_to_groups(event)
    else:
        logger.info(f"Message from {event.chat_id} contains http or @, ignored: {event.message.message}")

def start_bot():
    with client:
        logger.info("Welcome back!!!")
        client.run_until_disconnected()