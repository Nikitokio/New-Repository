from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

from random import randint, choice

from glob import glob

from emoji import emojize

from telegram import ReplyKeyboardMarkup, KeyboardButton

from handlers import (greet_user, guess_number, talk_to_me,
send_ref, user_coordinates)

from utils import get_smile, main_keyboard, play_random_numbers

def main():
    #Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY , use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("ref", send_ref))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать направление на МРТ)$'), send_ref))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    


    #Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()

