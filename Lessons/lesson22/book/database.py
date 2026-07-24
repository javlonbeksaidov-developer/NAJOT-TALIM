import json

FILENAME = 'books.json'

def load():
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    return data


def save(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)