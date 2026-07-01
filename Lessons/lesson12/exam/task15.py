
'''
🔹 15. Bo‘linuvchanlikni tekshirish
🧮 Vazifa: Kiritilgan sonning 2, 3 va 5 ga bo‘linishini aniqlang.
📥 Kirish: 30
📤 Chiqish:

30 soni 2 ga bo'linadi
30 soni 3 ga bo'linadi
30 soni 5 ga bo'linadi
'''

son = int(input("Son: "))
format = "{} soni {} ga bo'linadi"

if son % 2 == 0:
    print(format.format(son, 2))

if son % 3 == 0:
    print(format.format(son, 3))

if son % 5 == 0:
    print(format.format(son, 5))