import json
import time


def replenish_balance(username: str):
    transaction_set = {}

    with open("{0}_balance.data".format(username)) as balance_file:
        current_balance = balance_file.read()

    print("Balance: {0} USD".format(current_balance))  # for debug only
    entered_money = input("Enter amount : ")
    if entered_money.isdecimal():
        if (int(entered_money) != 0):
            new_balance = int(current_balance) + int(entered_money)
            print("Balance: {0} USD".format(new_balance))

            with open("{0}_balance.data".format(username), "w") as balance_file:
                balance_file.write(str(new_balance))

            with open("{0}_transactions.data".format(username)) as transaction_file:
                data = list(json.load(transaction_file))

            transaction_set = {"timestamp": int(time.time()), "old_balance": current_balance,
                               "new_balance": new_balance, "replenished": int(entered_money)}
            data.append(transaction_set)

            with open("{0}_transactions.data".format(username), "w") as js_file:
                json.dump(data, js_file, indent=4)
        else:
            print("Entered incorrect amount")
    else:
        print("Only digits allowed to enter")
