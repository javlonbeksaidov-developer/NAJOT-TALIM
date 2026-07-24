"""2) Mahsulotlar

Apple : 12000
Banana : 17000
Cola : 15000
Bread : 5000

User mahsulot nomini yozadi.
Savatchaga qo'shiladi.

Oxirida :

Apple x2
Bread x3
Cola x1

Total:
54000
"""

mahsulotlar = {
    "Sut mahsulotlari": {
        "sut": 12000,
        "kefir": 14000,
        "tvorog": 18000,
        "smetana": 15000,
        "sariyog'": 32000,
        "pishloq": 16000,
    },
    "Un va non mahsulotlari": {
        "buxanka non": 3000,
        "yopqich non": 4000,
        "un": 9000,
        "makaron": 10000,
    },
    "Sabzavotlar": {
        "kartoshka": 6000,
        "piyoz": 4000,
        "pomidor": 15000,
        "bodring": 12000,
        "sabzi": 5000,
    },
    "Mevalar": {
        "olma": 18000,
        "banan": 22000,
        "orik": 20000,
        "uzum": 25000,
    },
    "Ichimliklar": {
        "choy": 15000,
        "kofe": 3000,
        "gazlangan suv": 5000,
        "meva sharbati": 16000,
        "pepsi": 14000,
        "kola": 14000,
        "fanta": 14000,
    },
    "Shirinliklar": {
        "shokolad": 18000,
        "pechenye": 35000,
        "marmelad": 24000,
    },
}

savat = {}


def menu(son):
    menu = [
        "Sut mahsulotlari",
        "Un va non mahsulotlari",
        "Sabzavotlar",
        "Mevalar",
        "Ichimliklar",
        "Shirinliklar",
    ]
    for index, mahsulot in enumerate(mahsulotlar[menu[son - 1]], start=1):
        print(f"{index}. {mahsulot} : {mahsulotlar[menu[son - 1]][mahsulot]} so'm")

    tanlov = input("Qaysi mahsulotni olasiz:\n>>> ")
    if tanlov in mahsulotlar[menu[son - 1]]:
        savat[tanlov] = mahsulotlar[menu[son - 1]][tanlov]
        print(f"{tanlov} savatga qo'shildi.")
    else:
        print("Mahsulot nomini xato kiritdingiz.")


def main():
    while True:
        print("""
======================
    Yashnar market
======================

1. Sut mahsulotlari
2. Un va non mahsulotlari
3. Sabzavotlar
4. Mevalar
5. Ichimliklar
6. Shirinliklar
7. Savat
0. Bekor qilish
""")

        tanlov = input(">>> ")
        if tanlov == "0":
            break
        elif tanlov in ["1", "2", "3", "4", "5", "6"]:
            menu(int(tanlov))
        elif tanlov == "7":
            print("=== Savat ===")
            total = 0
            for index, mahsulot in enumerate(savat, start=1):
                print(f"{index}. {mahsulot} - {savat[mahsulot]} so'm")
                total += savat[mahsulot]
            print(f"\nJami: {total} so'm")
        else:
            print("Xato bo'lim.")


if __name__ == "__main__":
    main()
