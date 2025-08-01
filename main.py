from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Токен бота (берётся из переменных среды на Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот CH1NO. Отправь ссылку или артикул с Poizon для оформления заказа.")

def main():
    # Создание бота
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавление команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    print("Bot running")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    
