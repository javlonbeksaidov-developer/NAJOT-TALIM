''' 2-task. Matn tahlili'''

FILENAME = "matn.txt"


def count_words():
    with open(FILENAME, "r") as file:
        data = file.readline()

        return len(data.split())


def find_longest_word():
    with open(FILENAME, "r") as file:
        data = file.readline()

    min_soz = ""
    max_soz = ""
    for soz in data.split():
        if len(soz) < len(min_soz):
            min_soz = soz

        if len(soz) > len(max_soz):
            max_soz = soz

    return max_soz


def word_dict():
    with open(FILENAME, "r") as file:
        data = file.readline()

    word_dict = {}

    for soz in data.split():
        if soz in word_dict:
            word_dict[soz] += 1
        else:
            word_dict[soz] = 1

    return word_dict


def main():
    count = count_words()
    max_soz = find_longest_word()
    word = word_dict()

    with open('natija.txt', "w") as file:
        file.write(f"matn.txt faylidagi sozlar soni {count} ta.\n")
        file.write(
            f"matn.txt faylidagi sozlar ichida eng uzun so'z: {max_soz}, uzunligi: {len(max_soz)}.\n"
        )

        file.write(
            f"matn.txt faylidagi sozlar matn ichida nechi marta takrorlangani {word}"
        )


if __name__ == "__main__":
    main()
