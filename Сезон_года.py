def check_month(month: int):
    """Напишите ваш код здесь"""
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            result = 'Весна'
        elif 6 <= month <= 8:
            result = 'Лето'
        elif 9 <= month <= 11:
            result = 'Осень'
        else:
            result = 'Зима'
    else:
        result = 'Некорректный номер месяца'
    return result