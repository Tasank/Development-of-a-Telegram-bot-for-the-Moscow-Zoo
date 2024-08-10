def calculate_animal(answers):
    scores = {
        "Дикобраз": 0,
        "Тигр": 0,
        "Обезьяна": 0
    }

    # Пример логики подсчета очков
    for answer in answers:
        if answer == "Лес":
            scores["Дикобраз"] += 2
            scores["Обезьяна"] += 1
        elif answer == "Горы":
            scores["Тигр"] += 2
        elif answer == "Пустыня":
            scores["Тигр"] += 1
        elif answer == "Океан":
            scores["Обезьяна"] += 2

    # Определяем животное с наибольшими очками
    return max(scores, key=scores.get)
