from datetime import datetime
from uuid import uuid4

from database import load, save


class Book:
    def __init__(self, name, author, price):
        self.id = str(uuid4())
        self.name = name
        self.author = author
        self.price = price
        self.date = str(datetime.today())  # noqa: DTZ002

    def info(self):
        return f"{self.name} kitob. Author: {self.author}. Narxi: {self.price}"

    def add(self):
        data = load()

        name = input("Name: ")
        author = input("Author: ")
        price = int(input("Price: "))

        kitob = {
            "id": self.id,
            "name": name,
            "author": author,
            "price": price,
            "date": self.date,
        }

        data.append(kitob)

        save(data)

        return f"{name} kitobi kutubxonaga qo'shildi."

    def delete(self):
        data = load()

        id = input("Kitobning IDsi: ").strip()

        for kitob in data:
            if id == kitob["id"]:
                data.remove(kitob)
                print(f"{kitob['name']} kitobi o'chirildi.")

        save(data)

    def update(self):
        data = load()

        id = input("Kitobning IDsi: ").strip()
        for kitob in data:
            if id == kitob["id"]:
                name = input("New name: ")
                author = input("New author: ")
                price = int(input("New price: "))
                kitob["name"] = name
                kitob["author"] = author
                kitob["price"] = price

        save(data)

    def show(self):
        data = load()
        print(f"=== Kutubxona kitoblari ===\n{len(data)} ta.")
        for index, book in enumerate(data, start=1):
            print(
                f"{index}. {book['name']} kitobi, Author: {book['author']}. Narxi: {book['price']} so'm."
            )
