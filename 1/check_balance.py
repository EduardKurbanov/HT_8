def check_balance(username: str) -> object:
    try:
        file = open("{0}_balance.data".format(username), "r")
        money = file.read()
    except IOError:
        raise IOError("File does not appear to exist.")

    print("Balance: {0} USD".format(money))
    file.close()