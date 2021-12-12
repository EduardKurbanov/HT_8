"""
1. Програма-банкомат.

   Створити програму з наступним функціоналом:

      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);

      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);

      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).

   Особливості реалізації:

      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);

      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;

      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)

   Особливості функціонала:

      - за кожен функціонал відповідає окрема функція;

      - основна функція - <start()> - буде в собі містити весь workflow банкомата:

      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )

      - потім - елементарне меню типа:

        Введіть дію:

           1. Продивитись баланс

           2. Поповнити баланс

           3. Вихід

      - далі - фантазія і креатив :)
"""

from verification_password_login import verification_password_login
from check_balance import check_balance
from replenish_balance import replenish_balance
from withdraw_balance import withdraw_balance
from count_currency import console_admin


def start():
    count = 3
    while True:
        try:
            login = input("enter login: ")
            password = input("enter password: ")
            print("if there is no additional key press skip the step: ")
            special_key = input("enter additional key: ")
            valid = verification_password_login(login, password,special_key)
            while count > 0:
                if valid == "incasation":
                    console_admin(valid)

                if valid:
                    print("1. Look at the balance")
                    print("2. Replenish the balance")  # пополнить счет
                    print("3. Withdraw cash")  # снять наличные
                    print("4. Exit")
                    menu_item = input("Choose : ")
                    if int(menu_item) == 1:
                        check_balance(login)
                    elif int(menu_item) == 2:
                        replenish_balance(login)
                    elif int(menu_item) == 3:
                        withdraw_balance(login)
                    else:
                        exit()
                else:
                    count -= 1
                    print(f"attempt -> {count}")
                    break

                if count > 0:
                    continue
                else:
                    print("exit the program automatically")
            if count == 0:
                break

        except Exception as err:
            print(f"error -> {err}")


# if __name__ in "__main__":
start()
