"""4-task. Mini ombor tizimi"""

import json

FILENAME = "ombor.json"


def load():
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def print_data():
    data = load()
    print("=== Omborxona ===\n")
    for index, mahsulot in enumerate(data, start=1):
        print(
            f"{index}-mahsulot. {mahsulot['name']}. Narxi: {mahsulot['price']} so'm. Omborda {mahsulot['quantity']} ta qoldi."
        )


def sum_price():
    data = load()
    total = 0
    for mahsulot in data:
        total += mahsulot["price"]

    return f"Jami summa {total} so'm. {len(data)} ta mahsulot"


def add():
    data = load()

    name = input("Name: ")
    price = int(input("price: "))
    quantity = int(input("quantity: "))

    mahsulot = {"name": name, "price": price, "quantity": quantity}
    data.append(mahsulot)

    save(data)
    return f"({name}) mahsulot omborxonaga qo'shildi."


def main():
    print("=== Welcome to Omborxona ===\n")
    while True:
        tanlov = input("""
        Omborxona management

1. add product
2. sum product price
3. show product
0. exit
>>> """)
        if tanlov == "0":
            print("The end")
            break
        elif tanlov == "1":
            print(add())
        elif tanlov == "2":
            print(sum_price())
        elif tanlov == "3":
            print_data()


if __name__ == "__main__":
    main()
