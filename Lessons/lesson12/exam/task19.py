
'''
🔹 19. Matndagi unli harflarni sanash (for bilan)
🧮 Vazifa: Kiritilgan matn ichida a, e, i, o, u unlilar sonini for loop orqali sanang. 
📥 Kirish: "Salom Dunyo" 📤 Chiqish: 4
'''

text = input("Matn: ")

count = 0
for i in text:
    if i in "aeiouAEIOU":
        count += 1

print(count)
