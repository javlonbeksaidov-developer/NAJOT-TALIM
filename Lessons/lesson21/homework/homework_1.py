"""1) Kursda 25 ta student bor.
Foydalanuvchi har kuni kelgan studentlarning ismlarini kiritadi.

Dastur:
takrorlangan ismlarni hisoblamasin
nechta student kelganini chiqarsin
kimlar kelmaganini chiqarsin
attendance foizini hisoblasin
"""

students = [
    "Ali Valiyev",
    "Sardor Rahimov",
    "Jasur Karimov",
    "Madina Umarova",
    "Nargiza Tosheva",
    "Otabek Soliyev",
    "Bekzod Xalilov",
    "Zilola Saidova",
    "Rustam Ismoilov",
    "Shahnoza Qosimova",
    "Diyorbek Axmedov",
    "Malika Nazarova",
    "Jahongir Yusupov",
    "Lola Turdiyeva",
    "Xurshid Rustamov",
    "G'allakor Mirzayev",
    "Nodira G'afurova",
    "Bobur Alimov",
    "Sevara Rahmatova",
    "Farrux Jamolov",
    "Dilnoza Hamdamova",
    "Sherzod Sobirov",
    "Aziza Ergasheva",
    "Ulug'bek Boboyev",
    "Kamola Mamadaliyeva",
]


def main():
    kelganlar = []
    kelmaganlar = []

    for student in students:
        davomad = input(f"{student} darsga qatnashdimi? (yes/no)\n>>> ").lower().strip()
        if davomad == "yes":
            kelganlar.append(student)
        else:
            kelmaganlar.append(student)

    print("\n=== Darsga qatnashganlar ===")
    for index, i in enumerate(kelganlar, start=1):
        print(f"{index}. {i}")

    print("\n=== Darsga qatnashmaganlar ===")
    for index, i in enumerate(kelmaganlar, start=1):
        print(f"{index}. {i}")

    for i in kelmaganlar:
        print(i)

    print("\nDavomat foizi.")
    print(f"{len(kelganlar) / 25 * 100}%")


if __name__ == "__main__":
    main()
