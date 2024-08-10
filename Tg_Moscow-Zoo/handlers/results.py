import telebot
import json
import os

# Загрузка данных о животных
with open('data/animals.json', 'r') as f:
    animals = json.load(f)

def results_handler(call, user_answers):
    # Подсчет очков и определение животного
    from utils.scoring import calculate_animal
    selected_animal_name = calculate_animal(user_answers)

    # Поиск информации о выбранном животном
    selected_animal = next((animal for animal in animals if animal["name"] == selected_animal_name), None)

    if selected_animal:
        result_message = f"Ваше тотемное животное – {selected_animal['name']}!\n\n{selected_animal['description']}"
        # Отправляем изображение
        image_path = selected_animal['image']
        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                bot.send_photo(call.message.chat.id, image_file, caption=result_message)
        else:
            bot.send_message(call.message.chat.id, result_message)
