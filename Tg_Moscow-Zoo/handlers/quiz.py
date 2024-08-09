import telebot
from telebot import types
import json

with open('data/questions.json', 'r') as f:
    questions = json.load(f)


def quiz_handler(call):
    # Логика для показа вопросов
    question_data = questions[0]  # Например, берем первый вопрос
    question = question_data['question']
    options = question_data['options']

    keyboard = types.InlineKeyboardMarkup()
    for option in options:
        keyboard.add(types.InlineKeyboardButton(option, callback_data=option))

    bot.send_message(call.message.chat.id, question, reply_markup=keyboard)
