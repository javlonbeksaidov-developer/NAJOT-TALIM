
'''
🔹 20. 1 dan 10 gacha bo‘lgan sonlarning kvadratlarini chiqarish
🧮 Vazifa: For loop yordamida 1 dan 10 gacha bo‘lgan sonlarning kvadratini ekranga chiqaring. 
📤 Chiqish:

1 ning kvadrati: 1
2 ning kvadrati: 4
3 ning kvadrati: 9
...
10 ning kvadrati: 100
'''

format = "{} ning kvadrati: {}"

for i in range(1, 11):
    result = i ** 2
    print(format.format(i, result))