from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

from random import randint, choice

from glob import glob

from emoji import emojize

from telegram import ReplyKeyboardMarkup

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Здравствуй пользователь {context.user_data['emoji']}!",
        reply_markup=main_keyboard
        )

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Здравствуй, {username} {context.user_data['emoji']}! Ты написал: {text}")

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)

def play_random_numbers(user_number):
    bot_number = randint(user_number-10,user_number+10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выйграл!"
    return message

def send_ref(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_document(chat_id=chat_id, document=open('ref/refMRI.pdf', 'rb'))

def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать направление на МРТ']])

def main():
    #Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY , use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("ref", send_ref))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать направление на МРТ)$'), send_ref))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    


    #Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()

