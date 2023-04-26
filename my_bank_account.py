import os
import pickle

balance = 0
FILE_BALANCE = 'my_balance.txt'
if os.path.exists(FILE_BALANCE):
    with open(FILE_BALANCE, 'r') as f:
        bal = f.read()
balance = int(bal)

history = []
FILE_HISTORY = 'my_history.data'
if os.path.exists(FILE_HISTORY):
    with open(FILE_HISTORY, 'rb') as f:
        history = pickle.load(f)
def buy(balance,purchase):
    balance -= purchase
    return balance

if __name__ == '__main__':
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
            purchase = int(input('Введите сумму покупки '))
            if purchase > balance:
                print('Недостаточно средств!')
            else:
                balance = buy(balance, purchase)
                name = input('Укажите название покупки ')
                history.append((name, purchase))
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open(FILE_BALANCE, 'w') as f:
                f.write(str(balance))
            with open(FILE_HISTORY, 'wb') as f:
                pickle.dump(history, f)
            break
        else:
            print('Неверный пункт меню')