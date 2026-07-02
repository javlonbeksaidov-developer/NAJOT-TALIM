''' 1-mashq: Sonlarni yig'ish 
*args yordamida istalgan sondagi argumentlarni
qabul qiladigan va ularning yig'indisini qaytaradigan yigindi() funksiyasini yozing.'''

def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(summa(1, 2, 3))
print(summa())   


'''2-mashq: Eng katta sonni topish
*args yordamida berilgan sonlar orasidan eng kattasini topadigan eng_katta() funksiyasini yozing 
(max() funksiyasidan foydalanmasdan, if orqali solishtiring).'''

def eng_katta(*numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

print(f"Eng kattasi: {eng_katta(1, 2, 3, 4, 19, 6, 7, 8, 9)}")


'''3-mashq: Foydalanuvchi ma'lumotlarini chiqarish
**kwargs yordamida istalgan sondagi kalit-qiymat juftliklarini qabul qiladigan va ularni 
chiroyli qilib ekranga chiqaradigan malumot_chiqar() funksiyasini yozing.'''

def malumot_chiqar(**kwargs):
    for key, value in kwargs.items():
        print(f"'{key.title()}' - '{value}'")

malumot_chiqar(ota = "father", ona = "mother", aka = "brother", uka = "brother", opa = "sister", singil = "sister")


'''4-mashq: Ikkalasini birga ishlatish
*args va **kwargsni birgalikda qabul qiladigan mashq() funksiyasini yozing. 
Funksiya avval oddiy argumentlarni, keyin esa kalit-qiymatli argumentlarni chiqarsin.'''

def mashq(*args, **kwargs):
    i = 0
    for arg in args:
        print(f"{i+1}-son: {arg}")
        i += 1

    j = 0
    for key, value in kwargs.items():
        print(f"{j + 1}. '{key.title()}' - '{value}'")
        j += 1

mashq(87, 23, 31, 65, olma = "apple", banan = "banana")


'''5-mashq: Ortacha qiymatni hisoblash
*args yordamida sonlarni qabul qilib, 
ularning ortacha arifmetigini hisoblaydigan ortacha() funksiyasini yozing. 
Agar hech qanday son berilmasa, 0 qaytarsin.'''

def ortacha(*args):
    # 1-usul
    if args:
        return sum(args) / len(args)
    else:
        return 0
    
    # 2-usul
    # return sum(args) / len(args) if args else 0

print(ortacha())
print(ortacha(1, 12, 43, 65))
print(ortacha(1, 2, 3, 4))