
def plus(balance, pul):
    result = balance + pul
    return result

def minus(balance, pul):
    if balance < pul:
        return False
    else:
        result = balance - pul
        return result


def main():
    balance = 1

    while True:
        try:
            print("\n=== Bankomat ===\n")
            tanla = int(input("(1). Pul qo'shish.\n(2). Pul yechish.\n(3). Balance.\n(0). Exit.\n>>> "))
        except ValueError:
            print("(1) (2) (3) raqamlarini kiriting.")
        else:
            if tanla == 0:
                break
            elif tanla == 1:
                print("\n=== Pul qo'shish ===")
                try:
                    pul = int(input("Pul: "))
                except ValueError:
                    print("Xato.")
                else:
                    money = plus(balance, pul)
                    print(f"{pul} so'm qo'shildi.")
                    balance = money
            elif tanla == 2:
                print("\n=== Pul yechish ===")
                try:
                    pul = int(input("Pul: "))
                except ValueError:
                    print("Xato.")
                else:
                    money = minus(balance, pul)
                    if money:
                        print(f"{pul} so'm yechildi.")
                        balance = money
                    else:
                        print("Mablag' yetarlimas.")
            elif tanla == 3:
                print("\n=== Balance ===")
                print(f"Balance: {balance} so'm")
            else:
                print("(1) (2) (3) raqamlarini kiriting.")

        yana = input("\nDavom ettirasizmi (yes/no):\n>>> ")
        if yana == "no":
            break



if __name__ == "__main__":
    main()