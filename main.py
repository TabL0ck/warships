import telebot
import config
import change_color.main
from change_color.err_succ import error_case, succ_case

party_id = [] # Список с id пользователей, которые создали лобби

bot = telebot.TeleBot(config.TOKEN)

#
# Команда для создания лобби
#
@bot.message_handler(commands=['create_game'])
def create_game(message):

    # Проверка есть ли уже созданное лобби у одного и того же пользователя
    if message.from_user.id in party_id:
        if config.DEBUG:
            error_case("[ERROR] More then 1 game per player")
        return

    # Создание лобби
    party_id.append(message.from_user)
    bot.send_message(message.chat.id, "Игра создана, ожидайте подключения")
    if config.DEBUG:
        succ_case(f"[SUCCESS] Game for {message.from_user.id} create")

#
# Команда для отображения готовых лобби
#
@bot.message_handler(commands=['lobby_lists'])
def lobby_lists(message):

    # Проверка на существование хотя бы одного лобби
    if not party_id:
        if config.DEBUG:
            error_case("[ERROR] Party_id list is empty")
        bot.send_message(message.chat.id, "На данный момент нет созданных игр")
        return

    # Вывод лобби на экран
    for index, item in enumerate(party_id):

        # Инлайн клавиатура для подключения к игре
        inline_kb = telebot.types.InlineKeyboardMarkup()
        inline_btn = telebot.types.InlineKeyboardButton("Присоединиться", callback_data="join_btn")
        inline_kb.add(inline_btn)

        #Отправка сообщения с лоббаком
        bot.send_message(message.chat.id, f"{index}. {item.username}", reply_markup=inline_kb)
    if config.DEBUG:
        succ_case(f"[SUCCESS] List of games show successfuly")

#
# Колбэк хэндлер который срабатывает после нажатия на кнопку присоединения
#
@bot.callback_query_handler(func=lambda call: call.data == 'join_btn')
def join_btn(callback_query: telebot.types.CallbackQuery):

    # Проверка пользователя на попытку подключения к своей же игре
    if callback_query.from_user.id == party_id[int(callback_query.message.text[0])].id:
        if config.DEBUG:
            error_case(f"[ERROR] {callback_query.from_user.username} try to connect to own game")
        return

    # Успешное подключение и ожидание принятие игры от создателя лобби
    bot.send_message(callback_query.from_user.id, f"Вы успешно подключились к комнате {callback_query.message.text[3:]} ожидайте ответа от соперника")
    if config.DEBUG:
        succ_case(f"[SUCCESS] Player {callback_query.from_user.username} successfuly join to {callback_query.message.text[3:]} game")
    
    # Функция принятия лобби от хоста
    accept_game(callback_query, int(callback_query.message.text[0]))


def accept_game(callback_data, user_index):
    bot.send_message(party_id[user_index].id, callback_data.from_user.username)

#
# Запуск бота
#
def main():
    bot.polling(none_stop=True) 

if __name__ == "__main__":
    main()
