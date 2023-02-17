balance = 0
history = []

def buy(balance):
    purchase = int(input('Введите сумму покупки '))
    if purchase > balance:
        print('Недостаточно средств!')
    else:
        balance -= purchase
        name = input('Укажите название покупки ')
        history.append((name, purchase))
    return balance

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        sum = int(input('Введите сумму пополнения '))
        balance += sum
    elif choice == '2':
        balance = buy(balance)
    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')