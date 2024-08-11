import telebot
from telebot import types
import json

# Глобальная переменная для хранения ответов
user_answers = []

with open('data/questions.json', 'r') as f:
    questions = json.load(f)


def quiz_handler(call):
    global user_answers

    # Логика для показа вопросов
    current_question_index = len(user_answers)

    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        question = question_data['question']
        options = question_data['options']

        keyboard = types.InlineKeyboardMarkup()
        for option in options:
            keyboard.add(types.InlineKeyboardButton(option, callback_data=option))

        bot.send_message(call.message.chat.id, question, reply_markup=keyboard)
    else:
        # Все вопросы пройдены, показываем результаты
        results_handler(call, user_answers)

## bot переработать
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data in [option for question in questions for option in question['options']]:
        user_answers.append(call.data)  # Сохраняем ответ
        quiz_handler(call)  # Переходим к следующему вопросу
