


with open('word.txt', 'r') as file:
    data = file.readlines()

with open('oxshash.txt', 'w') as file:
    for word in data:
        word = word.rstrip().lower()

        if word == word[::-1]:
            file.write(word + '\n')


