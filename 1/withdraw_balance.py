import json
import time
from collections import Counter


def get_currency(money: int):
    requested_amount: int = money
    temp_list: list = []
    available_money: list = []
    available_amount: list = []
    available_currency: dict = {}

    summ_value: int = 0

    with open("c_u_.json", "r") as f:
        data = json.load(f)

    money_list: dict = data

    if int(str(money)[-1]) != 0:
        print("value is not short 10")
        return False

    for nominal, amount in money_list.items():
        if int(amount) > 0:
            available_money.append(int(nominal))
            available_amount.append(int(amount))
            available_currency: dict = dict(zip(available_money, available_amount))

    if int(requested_amount) > 0:
        while int(requested_amount) > 0:
            for nominal, amount in money_list.items():
                if int(amount) > 0:
                    tmp_val: int = int(requested_amount) % int(nominal)
                    if tmp_val == 0:
                        requested_amount -= int(nominal)
                        temp_list.append(nominal)
                        money_list[nominal] -= 1
                    else:
                        continue
                else:
                    if int(amount) == 0:
                        for i in range(0, len(str(requested_amount))):
                            temp0: list = []
                            temp1: list = []
                            temp3: list = []
                            temp4: list = []
                            for nominal0, amount0 in available_currency.items():
                                pow_coefficient: int = int(len(str(requested_amount))) - (i + 1)
                                check_value: int = int(str(requested_amount)[i]) * (10 ** pow_coefficient)
                                if (check_value >= int(nominal0)) and int(amount0) > 0:
                                    amount_needed = int((check_value / int(nominal0)))
                                    if amount_needed <= int(amount0):
                                        temp0.append(int(nominal0))
                                        temp1.append(int(amount_needed))
                                        max_val = max(temp0)
                                        temp_dict: dict = dict(zip(temp0, temp1))
                                        for j in range(0, amount_needed):
                                            temp_list.append(nominal0)
                                            temp_money_value = money_list[str(nominal0)]
                                            if temp_money_value > 0:
                                                money_list[str(nominal0)] -= 1
                                            else:
                                                break
                                        for items, value in temp_dict.items():
                                            if (items * value) == check_value:
                                                pass
                                            elif check_value > items:
                                                for val, am in available_currency.items():
                                                    amount_needed0 = int((int(check_value - items) / int(val)))
                                                    if int(am) > 0:
                                                        if (int(max_val) + (int(val) * amount_needed0)) == check_value:
                                                            temp3.append(int(val))
                                                            temp4.append(int(amount_needed0))
                                                            temp_dict0: dict = dict(zip(temp3, temp4))
                                                            for val00 in range(0, amount_needed0):
                                                                temp_list.append(val)
                                                                temp_money_value = money_list[str(val)]
                                                                if temp_money_value > 0:
                                                                    money_list[str(val)] -= 1
                                                                else:
                                                                    break
                                                            break
                                                        elif (items * value) == check_value:
                                                            for val00 in range(0, amount_needed0):
                                                                temp_list.append(val)
                                                                temp_money_value = money_list[str(val)]
                                                                if temp_money_value > 0:
                                                                    money_list[str(val)] -= 1
                                                                else:
                                                                    break

                                    break

                        for i in temp_list:
                            summ_value += int(i)

                        if summ_value == int(money):
                            requested_amount = 0
                            break
                        else:
                            print(f"Cant withdraw requested amount: {int(money)}")
                            return False
                    continue
                break
    else:
        print("Entered incorrect amount")
        return False

    print("*" * 20)
    output: dict = dict(Counter(temp_list))
    for val, num in output.items().__reversed__():
        print(f"Nominal: {val} x {num}")
    print("*" * 20)

    with open("c_u_.json", "w") as f:
        json.dump(money_list, f, indent=4)

    return True


get_currency(180)

def withdraw_balance(username: str):
    transaction_set = {}

    with open("{0}_balance.data".format(username)) as balance_file:
        current_balance = balance_file.read()

    print("Balance: {0} USD".format(current_balance))  # for debug only
    entered_money = input("Enter amount : ")
    if entered_money.isdecimal():
        if (int(entered_money) != 0) and (int(entered_money) <= int(current_balance)):
            check_state: bool = get_currency(int(entered_money))

            if check_state:
                new_balance = int(current_balance) - int(entered_money)
                print("Balance: {0} USD".format(new_balance))

                with open("{0}_balance.data".format(username), "w") as balance_file:
                    balance_file.write(str(new_balance))

                with open("{0}_transactions.data".format(username)) as transaction_file:
                    data = list(json.load(transaction_file))

                transaction_set = {"timestamp": int(time.time()), "old_balance": current_balance,
                                   "new_balance": new_balance, "withdraw": int(entered_money)}
                data.append(transaction_set)

                with open("{0}_transactions.data".format(username), "w") as js_file:
                    json.dump(data, js_file, indent=4)
            else:
                print("Operation unsuccessful")
        else:
            print("Entered incorrect amount")
    else:
        print("Only digits allowed to enter")
