import random
peoples = ['Пушкина', 'Ленина', 'Ивана Грозного', 'Петра I', 'Пугачевой', 'Маяковского', 'Гогля', 'Достоевского', 'Лермонтова', 'Есенина']
answers = ['06.06.1799', '22.04.1870', '25.08.1530', '09.06.1672', '15.04.1949', '19.07.1893', '20.03.1809', '11.11.1821', '15.10.1814', '03.10.1895']
months = {
    '03':'марта',
    '04':'апреля',
    '06':'июня',
    '07':'июля',
    '08':'августа',
    '10':'октября',
    '11':'ноября'
}
days = {
    '03':'третье',
    '06':'шестое',
    '09':'девятое',
    '11':'одиннадцатое',
    '15':'пятнадцатое',
    '19':'девятнадцатое',
    '20':'двадцатое',
    '22':'двадцать второе',
    '25':'двадцать пятое'
}
def random_peoples(peoples, count):
    return random.sample(peoples, count)

if __name__ == '__main__':
    while True:
        results = random_peoples(peoples, 5)
        kol = 0
        for people in results:
            question = input(f'Дата рождения {people} в формате dd.mm.yyyy? ')
            for i, answer in enumerate(peoples):
                if people == peoples[i]:
                    if question == answers[i]:
                        kol += 1
                    else:
                        day, month, year = answers[i].split('.')
                        print('Правильный ответ: ', days[day], months[month], year, 'года')
        print('Количество правильных ответов - ', kol)
        print('Количество ошибок - ', (5 - kol))
        the_end = input('Повторить игру? (да\нет) ')
        if the_end == 'нет':
            break
    print('Игра окончена')
