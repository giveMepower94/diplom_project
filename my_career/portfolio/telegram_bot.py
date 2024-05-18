import telegram
import logging
import asyncio

TELEGRAM_BOT_TOKEN = '7133609944:AAG0avgcM-8IHVqsdOy6GrXiOCDcVUumkaY'

TELEGRAM_CHAT_ID = 6208724492

logging.basicConfig(level=logging.DEBUG)


async def send_telegram_message(token, chat_id, message):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message)
        logging.info("Сообщение успешно отправлено")
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения: {e}")
