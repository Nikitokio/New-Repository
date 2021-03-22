def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Здравствуй пользователь {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
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

def send_ref(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_document(chat_id=chat_id, document=open('ref/refMRI.pdf', 'rb'))

def user_coordinates(update,context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    print(coords)
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )