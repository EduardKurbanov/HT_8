import csv


class LoginException(Exception):
    pass


class PasswordException(Exception):
    pass


def verification_password_login(username="", password="", special_key=""):
    with open("users.csv", "r", encoding="utf-8") as file_user:
        reader = csv.DictReader(file_user)
        list_of_stuff = []

        for i in reader:
            list_of_stuff.append(i)

        data = {}
        for i in list_of_stuff:
            data[i["login"]] = [i["password"], i["special_key"]]

        try:
            if username in data.keys():
                if [password, None] == data[username]:
                    return True
                elif [password, special_key] == data[username]:
                    return "incasation"
                else:
                    raise PasswordException(f"incorrect password -> {password}")
            else:
                raise LoginException(f"incorrect login -> {username}")
        except LoginException as err:
            print(f"starus incorrect login -> {err}")
        except PasswordException as err:
            print(f"status incorrect password -> {err}")

#
# d = verification_password_login()
#
# print(d, "1t")
