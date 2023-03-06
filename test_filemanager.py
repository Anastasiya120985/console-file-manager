from my_bank_account import buy

def test_buy():
    assert buy(200, 50) == 150
    assert buy(100, 50) == 50

from victory import random_peoples

def test_random_peoples():
    peoples = ('Пушкина', 'Ленина', 'Ивана Грозного', 'Петра I', 'Пугачевой', 'Маяковского', 'Гогля', 'Достоевского', 'Лермонтова', 'Есенина')
    assert len(random_peoples(peoples, 5)) == 5

    for people in random_peoples(peoples, 5):
        assert people in peoples

from menu import list_dirs

def test_list_dirs():
    assert '.idea' in list_dirs()
    assert '.git' in list_dirs()