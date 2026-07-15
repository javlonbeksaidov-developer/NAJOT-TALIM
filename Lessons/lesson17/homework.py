"""
3. "Kutubxona qarzini hisoblash"
Kitobni ijaraga olish sanasi va qaytarish kerak bo'lgan muddat berilgan.
Agar kitob kechiktirilsa, har bir kechikkan kun uchun bazaviy narx (masalan, 5000 so'm) va
har 3 kundan keyin oshib boradigan jarima tizimi asosida umumiy summani hisoblang.
"""

from datetime import datetime, timedelta
from uuid import uuid4
import calendar

TOLOV_KUNLIK = 5000
TOLOV_DARAJA = 1000

FILENAME = 'jarimalar.txt'


def sana():
    while True:
        try:
            yil = int(input("Yil: "))
        except ValueError:
            print("Butun son kiriting.")
        else:
            if 1900 <= yil <= datetime.now().year:
                break
            else:
                print(
                    f"Yil 1900-yildan {datetime.now().year}-gacha bo'lgan yilni kiriting."
                )

    while True:
        try:
            oy = int(input("Oy: "))
        except ValueError:
            print("Butun son kiriting.")
        else:
            if 1 <= oy <= 12:
                break
            else:
                print("Oy 1dan 12gacha bo'lgan qaiymatlarni kiriting.")

    max_day = calendar.monthrange(year=yil, month=oy)[1]        # yil va oyga qarab kunni hisoblaydi
    while True:
        try:
            kun = int(input(f"Kun (1-{max_day}):"))
        except ValueError:
            print("Butun son kiriting.")
        else:
            if 1 <= kun <= max_day:
                break
            else:
                print(f"KUn 1dan {max_day}gacha bo'lgan qaiymatlarni kiriting.")

    return yil, oy, kun


def qarz(kunlar):
    narx = 0
    for kun in range(1, kunlar + 1):
        daraja = (kun - 1) // 3
        tolov = TOLOV_KUNLIK + (daraja * TOLOV_DARAJA)
        narx += tolov

    return narx


def statistika():
    print("=== Statistika ===")
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            data = file.readlines()
    except FileNotFoundError:
        son = 0
        narx = 0
    else:
        son = 0
        narx = 0
        for qator in data:
            if "Kitob ID:" in qator:
                son += 1
            if "Hisoblangan jarima miqdori:" in qator:
                raqam = ''
                for belgi in qator:
                    if belgi.isdigit():
                            raqam += belgi
                
                if raqam:
                    pul = int(raqam)
                    narx += pul
    finally:
        print(f"Umumiy jarimalar soni: {son}")
        print(f"Umumiy jarimalar miqdori: {narx:,} so'm")


def main():
    print("==== Kutubxona kirim-chiqim boshqaruvi ===")
    while True:
        print("\nIjaraga olgan sanasini kiriting.")
        yil, oy, kun = sana()
        start = datetime(year=yil, month=oy, day=kun)

        while True:
            try:
                day = int(input("\nIjara qancha kun: "))
            except ValueError:
                print("Butun son kiriting.")
            else:
                if day > 0:
                    oraliq = timedelta(days=day)
                    break

        deadline = start + oraliq

        print("\nIjarani qaytargan sanasini kiriting.")
        yil, oy, kun = sana()
        stop = datetime(year=yil, month=oy, day=kun)

        if start <= stop:
            if stop > deadline:
                with open(FILENAME, 'a') as file:
                    farq = stop - deadline
                    kun = int(farq.days)
                    narx = qarz(kun)
                    file.write(f"\nKitob ID: {uuid4()}\n")
                    file.write(f"Ijaraga olingan sana: {start.date()}\n")
                    file.write(f"Qaytarish muddati: {deadline.date()}\n")
                    file.write(f"Haqiqatda qaytarilgan sana: {stop.date()}\n")
                    file.write(f"Kechikkan kunlar soni: {farq.days} kun\n")
                    file.write(f"Hisoblangan jarima miqdori: {narx:,} so'm\n")

                    print(f"{kun} kundan keyin topshirgani uchun {narx:,} so'm jarima.")
            else:
                print("Rahmat!")
        else:
            print("Noto'g'ri sana kirtingiz.")

        yana = input("\nYana ishlaysizmi (yes/no):\n>>> ").strip().lower()
        if yana in ["no", "n"]:
            print("Dastur tugatildi. Rahmat!\n")
            statistika()
            break


if __name__ == "__main__":
    main()
