
from datetime import datetime, timedelta

olish = input("Olish kunini kiriting: (2026-07-13)\n>>> ")
day = int(input("Qancha muddatga olayapti: kun\n>>> "))
qaytarish = input("Qaytargan kunini kiriting: (2026-07-13)\n>>> ")


start = datetime.fromisoformat(olish)
oraliq = timedelta(days = day)
stop = datetime.fromisoformat(qaytarish)

deadline = start + oraliq

print(start)
print(stop)
print(oraliq)
print(deadline)

if deadline < stop:
    day = stop - deadline
    print(f"{day.days} kun o'tib ketgan.")
else:
    print("Rahmat")
