def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password': # Здесь напишите свой код для проверки условия
        result = 'Добро пожаловать'    # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
        result = 'Доступ ограничен'    # В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result