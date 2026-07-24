"""3) Password Validator
Parol:
8 tadan uzun
katta harf
kichik harf
son
maxsus belgi
"""


def check(password):
    if (
        (len(password) >= 8)
        and (any(i.isdigit() for i in password))
        and (any(i in "!@#$%^&*()" for i in password))
        and (any(i.isalpha for i in password))
        and (any(i.islower for i in password))
        and (any(i.isupper for i in password))
    ):
        return True


def main():
    while True:
        password = input("Password:\n>>> ")
        if check(password):
            print("Tabriklaymiz, parol qabul qilindi.")
            break
        else:
            print("Xato! qaytadan urunib ko'ring.")


if __name__ == "__main__":
    main()
