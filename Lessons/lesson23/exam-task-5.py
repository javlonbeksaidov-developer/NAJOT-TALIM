"""5-task. tug'ilgan kun eslatmachisi"""

import calendar
from datetime import datetime, timedelta

NOW = datetime.now()  # noqa: DTZ005


def calculate_age():
    while True:
        try:
            year = int(input("Year: "))
        except ValueError:
            print(f"Yil 1900-{NOW.year} yillar oralig'ida bo'lsin.")
        else:
            if 1900 <= year <= NOW.year:
                break
            else:
                print(f"Yil 1900-{NOW.year} yillar oralig'ida bo'lsin.")

    print(f"{NOW.year - year} yoshdasiz")


def birth_day():
    while True:
        try:
            year = int(input("Year: "))
        except ValueError:
            print(f"Yil 1900-{NOW.year} yillar oralig'ida bo'lsin.")
        else:
            if 1900 <= year <= NOW.year:
                break
            else:
                print(f"Yil 1900-{NOW.year} yillar oralig'ida bo'lsin.")

    while True:
        try:
            month = int(input("Month: "))
        except ValueError:
            print("Oy 1-12 oralig'ida bo'lsin.")
        else:
            if 1 <= month <= 12:
                break
            else:
                print("Oy 1-12 oralig'ida bo'lsin.")

    _, max_day = calendar.monthrange(year, month)
    while True:
        try:
            day = int(input("Day: "))
        except ValueError:
            print(f"Kun 1-{max_day} oralig'ida bo'lsin.")
        else:
            if 1 <= day <= max_day:
                break
            else:
                print(f"Kun 1-{max_day} oralig'ida bo'lsin.")

    return year, month, day


def birthday():
    year, month, day = birth_day()
    birthday = datetime(year=year, month=month, day=day)  # noqa: DTZ001
    new_year = datetime(year=2026, month=month, day=day)  # noqa: DTZ001
    now = datetime(year=NOW.year, month=NOW.month, day=NOW.day)  # noqa: DTZ001

    farq = abs(now - new_year)
    days = timedelta(farq.days)

    if birthday == now:
        print("Tug'ilgan kuningiz bilan tabriklayman.")

    if new_year > now:
        print(f"{days} kun qoldi.")
    elif new_year < now:
        print(f"{days} kun o'tdi.")


def main():
    while True:
        tanlov = input("""
===== tug'ilgan kun eslatmachisi =====

1. yosh hisoblash
2. tug'ilgan kungacha
0. exit
>>> """)
        if tanlov == "0":
            print("The end")
            break
        elif tanlov == "1":
            calculate_age()
        elif tanlov == "2":
            birthday()


if __name__ == "__main__":
    main()
