import telegram
import logging
import asyncio
from decouple import config

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')

TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID', cast=int)

logging.basicConfig(level=logging.DEBUG)


async def send_telegram_message(token, chat_id, message):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message)
        logging.info("Сообщение успешно отправлено")
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения: {e}")
