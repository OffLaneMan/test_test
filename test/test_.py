import pytest
from Проверка_возраста import check_age
from Проверка_пароля import check_auth
from Сезон_года import check_month
from Яндекс_создать_папку import create_foler
ПРАВИЛЬНЫЙ_ЯНДЕКС_ТОКЕН = ''


@pytest.mark.parametrize('a, expected', (
    [19, 'Доступ разрешён'],
    [17, 'Доступ запрещён'],
    [41, 'Доступ разрешён']
))
def test_проверка_возраста(a, expected):
    assert check_age(a) == expected, 'ПРОВАЛ ТЕСТА'


@pytest.mark.parametrize('a, b, expected', (
    ['admin', 'password', 'Добро пожаловать'],
    ['admin', 'hfhfd', 'Доступ ограничен'],
    ['adn', 'password', 'Доступ ограничен']
))
def test_проверка_пароля(a, b, expected):
    assert check_auth(a, b) == expected, 'ПРОВАЛ ТЕСТА'


@pytest.mark.parametrize('a, expected', (
    [19, 'Некорректный номер месяца'],
    [12, 'Зима'],
    [3, 'Весна'],
    [6, 'Лето'],
    [0, 'Некорректный номер месяца'],
    [10, 'Осень']
))
def test_проверка_возраста(a, expected):
    assert check_month(a) == expected, 'ПРОВАЛ ТЕСТА'


@pytest.mark.parametrize('a, b, expected', (
    [ПРАВИЛЬНЫЙ_ЯНДЕКС_ТОКЕН, 'test_folder', 201],
    ['dgsdgdf', 'new_folder', 401],
    [ПРАВИЛЬНЫЙ_ЯНДЕКС_ТОКЕН, '//!@#$%^&*\\\\', 404],
    [ПРАВИЛЬНЫЙ_ЯНДЕКС_ТОКЕН, 'test_folder', 409],
))
def test_create_foler(a, b, expected):
    assert create_foler(a, b) == expected, 'ПРОВАЛ ТЕСТА'
