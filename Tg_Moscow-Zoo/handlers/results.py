import telebot

def results_handler(call):
    # Логика для определения результата и вывода
    result_message = "Ваше тотемное животное – дикобраз!"
    bot.send_message(call.message.chat.id, result_message)
