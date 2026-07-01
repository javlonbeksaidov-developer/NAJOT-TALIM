
'''
🔹 12. So‘zning boshlanish pozitsiyasi (o'rni) ni topish
🧮 Vazifa: Ma’lum bir so‘z matn ichida qayerdan boshlanishini toping.
📥 Kirish: "Men Python dasturlash tilini o‘rganaman", "Python"
📤 Chiqish: 4
'''

text = input("Matn: ")
joy = input("So'z: ")
result = text.find(joy)
print(result)