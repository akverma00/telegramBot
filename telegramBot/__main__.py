import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_bot import TelegramBot

def main():
    bot = TelegramBot()
    bot.start_bot()

if __name__ == "__main__":
    main()