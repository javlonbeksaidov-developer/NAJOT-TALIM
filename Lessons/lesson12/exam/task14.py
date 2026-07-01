
'''
🔹 14. Document type aniqlash
🧮 Vazifa: Fayl .pdf, .docx yoki .txt bilan tugashini tekshiring 
va uni anilovchi dastur yarating.
📥 Kirish: "report.pdf"
📤 Chiqish: Fayl turi: pdf
'''

fayl = input("Fayl: ")

if fayl.endswith(".pdf"):
    print("Fayl turi: pdf")
elif fayl.endswith(".docx"):
    print("Fayl turi: docx")
elif fayl.endswith(".txt"):
    print("Fayl turi: txt")
else:
    print("Fayl turini aniqlab bo'lmadi!")