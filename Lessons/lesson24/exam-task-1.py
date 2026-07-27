''' 1-task. Son tahlili'''

def is_even(n):
    return bool(n % 2 == 0)


def classify_sign(n):
    if n == 0:
        return f"{n} 0 ga teng."
    elif n > 0:
        return f"{n} musbat son"
    else:
        return f"{n} manfiy son"


def main():
    marta = 0
    sonlar = []
    while True:
        son = input("Son kiriting ('stop' - to'xtatish):\n>>>").strip().lower()
        if son == 'stop':
            print("Dastur tugadi.")
            break
        else:
            try:
                son = int(son)
            except ValueError:
                print("Butun son kiriting.")
            else:
                if is_even(son):
                    print(f"{son} juft son.")
                else:
                    print(f"{son} toq son.")

                print(classify_sign(son))

                sonlar.append(son)

        marta += 1

    print(f'''=== Dastur yakunlandi ===

Dasturga {marta} marta son kiritldi.

Kiritilgan sonlarning umumiy yig'indisi {sum(sonlar)}.

Kiritilgan sonlarning o'rtacha qiymati {sum(sonlar) / len(sonlar)}.

Kiritilgan sonlar ichidagi eng katta qiymat {max(sonlar)}.

Kiritilgan sonlar ichidagi eng kichik qiymat {min(sonlar)}.
''')





if __name__ == '__main__':
    main()