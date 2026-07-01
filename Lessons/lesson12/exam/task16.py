
'''
🔹 16. Yoshga bog‘liq chegirma
🧮 Vazifa: Chipta narxi 100 000 so‘m. Yoshga qarab chegirma qo‘llang. 
Yosh kiritilganda aynan shu yoshdagi insonlar uchun chipta narxi qancha bo'lishi 
va qancha chegirma berilishini aniqlovchi dastur yarating.

7 yoshgacha (0-6): 50% chegirma
7-17 yosh: 20% chegirma
60 yoshdan katta: 30% chegirma
📥 Kirish: 5
📤 Chiqish: Yakuniy narx: 50 so'm (50% chegirma qo'llanildi)
'''

chipta_narxi = 100_000

yosh = int(input("Yosh: "))
format = "Yakuniy narx: {} so'm ({}% chegirma qo'llanildi)"

if  yosh < 7:
    foiz = 50
    result = chipta_narxi * (1 - foiz / 100)
    print(format.format(result, foiz))
elif yosh < 18:
    foiz = 20
    result = chipta_narxi * (1 - foiz / 100)
    print(format.format(result, foiz))
elif yosh < 60:
    foiz = 0
    result = chipta_narxi * (1 - foiz / 100)
    print(format.format(result, foiz))
else:
    foiz = 30
    result = chipta_narxi * (1 - foiz / 100)
    print(format.format(result, foiz))
