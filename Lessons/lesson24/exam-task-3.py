''' 3-task. Nar toshi'''

import json
import random

FILENAME = "natija.json"


def main():
    with open(FILENAME, "r") as file:
        data = json.load(file)

    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0
    for i in range(1000):
        x = random.randint(1, 6)
        y = random.randint(1, 6)

        yigindi = x + y

        if yigindi == 2:
            count_2 += 1
        elif yigindi == 3:
            count_3 += 1
        elif yigindi == 4:
            count_4 += 1
        elif yigindi == 5:
            count_5 += 1
        elif yigindi == 6:
            count_6 += 1
        elif yigindi == 7:
            count_7 += 1
        elif yigindi == 8:
            count_8 += 1
        elif yigindi == 9:
            count_9 += 1
        elif yigindi == 10:
            count_10 += 1
        elif yigindi == 11:
            count_11 += 1
        elif yigindi == 12:
            count_12 += 1

    natija = {
        "2": count_2,
        "3": count_3,
        "4": count_4,
        "5": count_5,
        "6": count_6,
        "7": count_7,
        "8": count_8,
        "9": count_9,
        "10": count_10,
        "11": count_11,
        "12": count_12,
    }
    data.append(natija)

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
