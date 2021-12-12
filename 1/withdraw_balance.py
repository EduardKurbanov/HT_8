import json
import time
from collections import Counter


def get_currency(money: int):
    requested_amount: int = money
    temp_list: list = []

    with open("c_u_.json", "r") as f:
        data = json.load(f)

    money_list: dict = data

    if int(str(money)[-1]) != 0:
        print("value is not short 10")
        return

    if int(requested_amount) > 0:
        while int(requested_amount) > 0:
            for nominal, amount in money_list.items():
                if int(amount) != 0:
                    tmp_val: int = int(requested_amount) % int(nominal)
                    if tmp_val == 0:
                        requested_amount -= int(nominal)
                        temp_list.append(nominal)
                        money_list[nominal] -= 1
                    else:
                        continue
                else:
                    if int(amount) == 0:
                        print(f"Cant withdraw requested amount: {requested_amount}")
                        return
                    continue
                break
    else:
        print("Entered incorrect amount")

    print("*" * 20)
    output: dict = dict(Counter(temp_list))
    for val, num in output.items().__reversed__():
        print(f"Nominal: {val} x {num}")
    print("*" * 20)

    with open("c_u_.json", "w") as f:
        json.dump(money_list, f, indent=4)


def withdraw_balance(username: str):
    transaction_set = {}

    with open("{0}_balance.data".format(username)) as balance_file:
        current_balance = balance_file.read()

    print("Balance: {0} USD".format(current_balance))  # for debug only
    entered_money = input("Enter amount : ")
    if entered_money.isdecimal():
        if (int(entered_money) != 0) and (int(entered_money) <= int(current_balance)):
            new_balance = int(current_balance) - int(entered_money)
            print("Balance: {0} USD".format(new_balance))

            with open("{0}_balance.data".format(username), "w") as balance_file:
                balance_file.write(str(new_balance))

            with open("{0}_transactions.data".format(username)) as transaction_file:
                data = list(json.load(transaction_file))

            get_currency(int(entered_money))

            transaction_set = {"timestamp": int(time.time()), "old_balance": current_balance,
                               "new_balance": new_balance, "withdraw": int(entered_money)}
            data.append(transaction_set)

            with open("{0}_transactions.data".format(username), "w") as js_file:
                json.dump(data, js_file, indent=4)
        else:
            print("Entered incorrect amount")
    else:
        print("Only digits allowed to enter")
