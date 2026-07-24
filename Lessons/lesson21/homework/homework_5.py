"""5) Contact Book - Add, Search, Delete , Update , Exit"""

import json
from datetime import date
from uuid import uuid4

FILENAME = "contack.json"


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

    name = input("Ism: ")
    surname = input("Familiya: ")
    phone = input("Telefon raqam:")

    contack = {
        'id' : str(uuid4()),
        'name' : name,
        'surname' : surname,
        'phone' : phone,
        'date' : str(date.today()),
    }
    data.append(contack)

    save(data)


def search():
    data = load()
    search = input("Search: ")
    for contack in data:
        if search in (contack['name'] or contack['surname'] or contack['id'] or contack['phone']):
            print(f"{contack['name']} {contack['surname']}. {contack['phone']}.")


def delete():
    data = load()
    id = input("Delete (ID): ")
    for contack in data:
        if id == contack['id']:
            data.remove(contack)

    save(data)


def update():
    data = load()
    id = input("Delete (ID): ")
    for contack in data:
        if id == contack['id']:
            name = input("New name: ")
            surname = input("New surname: ")
            phone = input("New phone: ")

            contack['name'] = name
            contack['surname'] = surname
            contack['phone'] = phone

    save(data)


def main():
    while True:
        print("""
==== Contack menu ====

1. add
2. search
3. delete
4. update
0. exit
""")

        tanlov = input(">>> ")
        if tanlov == '0':
            break
        elif tanlov == '1':
            add()
        elif tanlov == '2':
            search()
        elif tanlov == '3':
            delete()
        elif tanlov == '4':
            print(update())
        else:
            print("Xato")


if __name__ == "__main__":
    main()
