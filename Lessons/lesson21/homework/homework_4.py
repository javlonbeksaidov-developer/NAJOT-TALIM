"""4)Expense Tracker - har safar xarajat nomi va narxi kiritaladi va json faylga yoziladi ,
kunlik va haftalik , va oylik harajatlarni korish imkoniyati bo'lsin"""

import json
from datetime import date
from uuid import uuid4

FILENAME = "xarajat.json"


def load():
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    return data


def save(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add():
    data = load()

    name = input("Xarajat nomi: ")
    price = int(input("Xarajat narxi: "))

    xarajat = {
        "id": str(uuid4()),
        "name": name,
        "price": price,
        "date": str(date),
    }
    data.append(xarajat)

    save(data)

    return f"{name} saqlandi."


def show():
    data = load()

    for index, xarajat in enumerate(data, start=1):
        print(f"{index}-xarajat. {xarajat['name']} -- {xarajat['price']} so'm")


def main():
    while True:
        tanlov = input("""
===== Kunlik xarajatlar =====

1. add
2. show
0. exit
>>> """)

        if tanlov == "0":
            break
        elif tanlov == "1":
            print(add())
        elif tanlov == "2":
            show()
        else:
            print("Xato bo'lim.")


if __name__ == "__main__":
    main()
