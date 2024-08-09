import telebot
from config import TOKEN
from handlers.start import start_handler
from handlers.quiz import quiz_handler
from handlers.results import results_handler

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    start_handler(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'quiz':
        quiz_handler(call)
    elif call.data.startswith('result_'):
        results_handler(call)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
