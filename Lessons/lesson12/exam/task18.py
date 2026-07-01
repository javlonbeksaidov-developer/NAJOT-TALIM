
'''
🔹 18. 1 dan N gacha bo‘lgan sonlar yig‘indisi
🧮 Vazifa: Foydalanuvchi kiritgan N sonigacha bo‘lgan barcha sonlarning yig‘indisini for loop yordamida hisoblang. 
📥 Kirish: N = 5 📤 Chiqish: 15 (1+2+3+4+5)
'''
stop = int(input("Son: "))
total = 0
ifoda = ""

for i in range(1, stop + 1):
    total += i

    if i == 1:
        ifoda = "1"
    else: 
        ifoda = ifoda + "+" + str(i)

    i += 1

print(f"{total} ({ifoda})")