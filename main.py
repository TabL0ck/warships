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
    if config.DEBUG:

        # Проверка есть ли уже созданное лобби у одного и того же пользователя
        if message.from_user.id in party_id:
            print(error_case("[ERROR] More then 1 game per player"))
            return

        # Создание лобби
        party_id.append(message.from_user.id)
        bot.send_message(message.chat.id, "Игра создана, ожидайте подключения")
        print(succ_case(f"[SUCCESS] Game for {message.from_user.id} create"))

    else:
        pass
#
# Команда для отображения готовых лобби
#
@bot.message_handler(commands=['lobby_lists'])
def lobby_lists(message):
    if config.DEBUG:

        # Проверка на существование хотя бы одного лобби
        if not party_id:
            print(error_case("[ERROR] Party_id list is empty"))
            bot.send_message(message.chat.id, "На данный момент нет созданных игр")
            return

        # Вывод лобби на экран
        for index, item in enumerate(party_id):
            bot.send_message(message.chat.id, f"{index}. {item}")
        print(succ_case(f"[SUCCESS] List of games show successfuly"))

    else:
        pass


bot.polling(none_stop=True) 
