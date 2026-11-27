<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2025%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 OOP ning 4 ta ustuni

Obyektga yo'naltirilgan dasturlash to'rtta asosiy prinsipga tayanadi:

| Ustun | Ma'nosi | Asosiy g'oya |
|-------|---------|--------------|
| **Encapsulation** (inkapsulyatsiya) | Ma'lumotni yashirish va himoyalash | Atributlarga to'g'ridan-to'g'ri emas, metod orqali murojaat |
| **Abstraction** (abstraksiya) | Keraksiz tafsilotni yashirib, faqat muhimini ko'rsatish | "Nima qiladi" ma'lum, "qanday qiladi" yashirin |
| **Inheritance** (meros olish) | Bir klass boshqa klassning xususiyatlarini oladi | Kodni qayta ishlatish |
| **Polymorphism** (polimorfizm) | Bir xil nom, turlicha ishlash | Bitta metod, ko'p shakl |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔒 1. Encapsulation (inkapsulyatsiya)

**Ta'rif:** ma'lumotlar (atributlar) va ular bilan ishlovchi metodlarni **bitta klass ichida birlashtirish** hamda ma'lumotga **tashqaridan nazoratsiz kirishni cheklash**.

## Kirish darajalari

| Yozilishi | Daraja | Ma'nosi |
|-----------|--------|---------|
| `nom` | Public (ochiq) | Hamma joydan foydalanish mumkin |
| `_nom` | Protected (himoyalangan) | "Ichki foydalanish uchun" degan kelishuv, majburiy emas |
| `__nom` | Private (yopiq) | Tashqaridan oddiy yo'l bilan olinmaydi |

```python
class Hisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi          # public
        self._tarif = "oddiy"       # protected
        self.__balans = balans      # private

    def balans_korish(self):
        return self.__balans

    def pul_qosh(self, summa):
        if summa > 0:
            self.__balans += summa

h = Hisob("Ali", 1000)
h.pul_qosh(500)

print(h.egasi)               # Ali
print(h.balans_korish())     # 1500
print(h.__balans)            # AttributeError
```

> ⚠️ Python'da `__nom` aslida nomini `_Hisob__balans` ga o'zgartiradi (name mangling). Bu mutlaq himoya emas, faqat tasodifiy o'zgartirishdan saqlaydi.

## Getter va Setter

Atributni o'qish va o'zgartirishni metodlar orqali nazorat qilish:

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.__yosh = yosh

    def get_yosh(self):
        return self.__yosh

    def set_yosh(self, yosh):
        if 0 < yosh < 120:
            self.__yosh = yosh
        else:
            print("Yosh noto'g'ri!")

t = Talaba("Ali", 20)
t.set_yosh(-5)           # Yosh noto'g'ri!
t.set_yosh(21)
print(t.get_yosh())      # 21
```

## `@property` (Python usuli)

Getter va setter ni oddiy atribut kabi ishlatish imkonini beradi. Bu Python'da **eng ko'p ishlatiladigan** usul.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh            # setter ishga tushadi

    @property
    def yosh(self):                 # getter
        return self.__yosh

    @yosh.setter
    def yosh(self, qiymat):         # setter
        if not 0 < qiymat < 120:
            raise ValueError("Yosh noto'g'ri!")
        self.__yosh = qiymat

t = Talaba("Ali", 20)
print(t.yosh)        # 20   (get_yosh() emas, oddiy atribut kabi)
t.yosh = 25          # setter ishlaydi
t.yosh = -3          # ValueError: Yosh noto'g'ri!
```

| Dekorator | Vazifasi |
|-----------|----------|
| `@property` | Getter: qiymatni o'qish |
| `@nom.setter` | Setter: qiymatni o'zgartirish (tekshiruv bilan) |
| `@nom.deleter` | Deleter: atributni o'chirish |

**Faqat o'qish uchun atribut:** setter yozilmasa, qiymatni o'zgartirib bo'lmaydi.

```python
class Doira:
    def __init__(self, radius):
        self.radius = radius

    @property
    def yuza(self):
        return 3.14 * self.radius ** 2

d = Doira(5)
print(d.yuza)        # 78.5  (qavssiz)
d.yuza = 10          # AttributeError
```

**Foydasi:**

| Afzallik | Tavsif |
|----------|--------|
| Himoya | Noto'g'ri qiymat kiritilishining oldi olinadi |
| Nazorat | Qiymat o'zgarganda tekshiruv va qo'shimcha amal bajariladi |
| Erkinlik | Ichki tuzilma o'zgarsa ham, tashqi kod buzilmaydi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎭 2. Abstraction (abstraksiya)

**Ta'rif:** murakkab ichki ishlashni yashirib, foydalanuvchiga faqat **kerakli interfeysni** ko'rsatish. Masalan, mashinani haydashda `gaz` bosasiz, dvigatel ichida nima bo'layotganini bilishingiz shart emas.

Python'da abstraksiya `abc` (Abstract Base Class) moduli orqali amalga oshiriladi.

```python
from abc import ABC, abstractmethod
```

## Abstrakt klass

**Ta'rif:** to'liq tugallanmagan klass. Undan **obyekt yaratib bo'lmaydi**, faqat **meros olish uchun** ishlatiladi. Ichida **abstrakt metodlar** (tanasi yo'q, faqat nomi) bo'ladi. Bola klass ularni **albatta yozishi** shart.

```python
from abc import ABC, abstractmethod

class Shakl(ABC):
    @abstractmethod
    def yuza(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def tavsif(self):                       # oddiy metod ham bo'ladi
        return f"Yuza: {self.yuza()}, perimetr: {self.perimetr()}"


class Togri(Shakl):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi

    def perimetr(self):
        return 2 * (self.eni + self.boyi)


class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2

    def perimetr(self):
        return 2 * 3.14 * self.radius


t = Togri(4, 6)
print(t.tavsif())        # Yuza: 24, perimetr: 20

s = Shakl()              # TypeError: abstrakt klassdan obyekt yaratib bo'lmaydi
```

**Bola klass abstrakt metodni yozmasa:**

```python
class Uchburchak(Shakl):
    def yuza(self):
        return 10

u = Uchburchak()    # TypeError: perimetr metodi yozilmagan
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Meros | `ABC` dan meros olinadi |
| `@abstractmethod` | Metodni abstrakt qiladi |
| Obyekt | Abstrakt klassdan yaratib bo'lmaydi |
| Majburiyat | Bola klass barcha abstrakt metodlarni yozishi shart |
| Oddiy metod | Abstrakt klass ichida oddiy metod ham bo'lishi mumkin |
| Vazifasi | Barcha bola klasslar uchun **umumiy qoida (shartnoma)** belgilash |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧬 3. Inheritance (meros olish)

**Ta'rif:** yangi klass (**bola, child**) mavjud klassning (**ota, parent**) atribut va metodlarini **tayyor holda oladi**. Kodni qayta yozish shart emas.

**Sintaksis:**

```python
class Bola(Ota):
    pass
```

```python
class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def ovqatlan(self):
        print(f"{self.ism} ovqatlanyapti")


class It(Hayvon):
    def vovulla(self):
        print(f"{self.ism}: Vov-vov!")


class Mushuk(Hayvon):
    def miyovla(self):
        print(f"{self.ism}: Miyov!")


it = It("Rex")
it.ovqatlan()      # Rex ovqatlanyapti  (otadan olingan)
it.vovulla()       # Rex: Vov-vov!      (o'zining metodi)

m = Mushuk("Barsik")
m.ovqatlan()       # Barsik ovqatlanyapti
m.miyovla()        # Barsik: Miyov!
```

**Atamalar:**

| Atama | Ma'nosi |
|-------|---------|
| **Parent / Base / Super klass** | Ota klass (`Hayvon`) |
| **Child / Derived / Sub klass** | Bola klass (`It`, `Mushuk`) |

## `super()` funksiyasi

Ota klassning metodini (ko'pincha `__init__`) bola klass ichidan chaqiradi.

```python
class Hayvon:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class It(Hayvon):
    def __init__(self, ism, yosh, zot):
        super().__init__(ism, yosh)     # ota klassning __init__ ini chaqirish
        self.zot = zot


it = It("Rex", 3, "Ovcharka")
print(it.ism, it.yosh, it.zot)    # Rex 3 Ovcharka
```

> ⚠️ Bola klassda `__init__` yozilsa, ota klassning `__init__` i **avtomatik ishlamaydi**. Uni `super().__init__()` bilan chaqirish kerak.

## Metodni qayta yozish (method overriding)

Bola klass ota klassdagi metodni o'zicha **qayta yozishi** mumkin.

```python
class Hayvon:
    def ovoz(self):
        print("Hayvon ovozi")


class It(Hayvon):
    def ovoz(self):
        print("Vov-vov!")


class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()            # avval ota klass metodi
        print("Miyov!")           # keyin o'zinikini qo'shadi


It().ovoz()        # Vov-vov!
Mushuk().ovoz()    # Hayvon ovozi
                   # Miyov!
```

## Meros turlari

| Tur | Tavsif | Ko'rinishi |
|-----|--------|------------|
| **Single** | Bitta otadan | `class B(A)` |
| **Multilevel** | Zanjir (bobo → ota → bola) | `class C(B)`, `class B(A)` |
| **Hierarchical** | Bitta otadan bir nechta bola | `class B(A)`, `class C(A)` |
| **Multiple** | Bir nechta otadan | `class C(A, B)` |

```python
# Multilevel
class A:
    def a(self): print("A")

class B(A):
    def b(self): print("B")

class C(B):
    def c(self): print("C")

x = C()
x.a(); x.b(); x.c()      # A B C
```

```python
# Multiple
class Uchuvchi:
    def uch(self):
        print("Uchyapti")

class Suzuvchi:
    def suz(self):
        print("Suzyapti")

class Ordak(Uchuvchi, Suzuvchi):
    pass

o = Ordak()
o.uch()      # Uchyapti
o.suz()      # Suzyapti
```

## MRO (Method Resolution Order)

Metod qaysi klassdan qidirilish **tartibi**. Bir nechta otadan meros olganda muhim.

```python
print(Ordak.__mro__)
# (<class 'Ordak'>, <class 'Uchuvchi'>, <class 'Suzuvchi'>, <class 'object'>)
```

> Qidiruv chapdan o'ngga: avval o'z klassi, keyin `Uchuvchi`, keyin `Suzuvchi`, oxirida `object`.

## `isinstance()` va `issubclass()`

| Funksiya | Vazifasi |
|----------|----------|
| `isinstance(obj, Klass)` | Obyekt shu klass (yoki uning bolasi) ekanini tekshiradi |
| `issubclass(Bola, Ota)` | Bir klass boshqasining bolasi ekanini tekshiradi |

```python
it = It("Rex", 3, "Ovcharka")

print(isinstance(it, It))          # True
print(isinstance(it, Hayvon))      # True  (ota klassga ham tegishli)
print(isinstance(it, Mushuk))      # False
print(issubclass(It, Hayvon))      # True
```

> 💡 Python'dagi har bir klass yashirin ravishda `object` klassidan meros oladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎪 4. Polymorphism (polimorfizm)

**Ta'rif:** "ko'p shakllilik". **Bir xil nomdagi metod** turli obyektlarda **turlicha ishlaydi**.

## 1. Meros orqali polimorfizm (overriding)

```python
class Hayvon:
    def ovoz(self):
        pass

class It(Hayvon):
    def ovoz(self):
        return "Vov-vov!"

class Mushuk(Hayvon):
    def ovoz(self):
        return "Miyov!"

class Sigir(Hayvon):
    def ovoz(self):
        return "Mooo!"

hayvonlar = [It(), Mushuk(), Sigir()]

for h in hayvonlar:
    print(h.ovoz())      # har biri o'zicha javob beradi
```

**Natija:**

```
Vov-vov!
Miyov!
Mooo!
```

> Sikl ichida `h` ning aniq turi nima ekanini bilish shart emas, `ovoz()` chaqirilaveradi.

## 2. Polimorf funksiya

Turli obyektlar bilan bir xil ishlaydigan funksiya:

```python
def ovoz_chiqar(hayvon):
    print(hayvon.ovoz())

ovoz_chiqar(It())        # Vov-vov!
ovoz_chiqar(Mushuk())    # Miyov!
```

## 3. Duck typing ("o'rdak testi")

> *"Agar u o'rdakdek yursa va o'rdakdek vaqillasa, demak u o'rdak."*

Python'da obyekt **qaysi klassdan ekanligi** emas, **kerakli metodi borligi** muhim. Umumiy ota klass shart emas.

```python
class Ordak:
    def ovoz(self):
        return "Kvak!"

class Robot:
    def ovoz(self):
        return "Bip-bip!"

class Odam:
    def ovoz(self):
        return "Salom!"

for obj in [Ordak(), Robot(), Odam()]:
    print(obj.ovoz())    # hammasida ovoz() bor, shuning uchun ishlaydi
```

## 4. Operator polimorfizmi

Bir xil operator turli turlarda turlicha ishlaydi:

```python
print(5 + 3)              # 8        (son qo'shish)
print("Sa" + "lom")       # Salom    (matn birlashtirish)
print([1, 2] + [3, 4])    # [1, 2, 3, 4]   (ro'yxat birlashtirish)

print(len("Salom"))       # 5
print(len([1, 2, 3]))     # 3
print(len({"a": 1}))      # 1
```

Shuningdek, `__add__`, `__len__` kabi dunder metodlar orqali o'z klassingizda ham shunday qilish mumkin (24-darsda ko'rilgan).

## Polimorfizm turlari

| Tur | Tavsif | Python'da |
|-----|--------|-----------|
| **Method overriding** | Bola klass ota metodini qayta yozadi | Qo'llab-quvvatlanadi |
| **Duck typing** | Metodi bor har qanday obyekt ishlaydi | Qo'llab-quvvatlanadi |
| **Operator overloading** | Operatorni o'z klassga moslash | Dunder metodlar orqali |
| **Method overloading** | Bir xil nom, turli parametrlar soni | **Yo'q** (oxirgi yozilgani ustun, `*args` yoki default parametr ishlatiladi) |

```python
class Kalkulyator:
    def qosh(self, a, b, c=0):       # method overloading o'rniga default parametr
        return a + b + c

k = Kalkulyator()
print(k.qosh(1, 2))       # 3
print(k.qosh(1, 2, 3))    # 6
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol: 4 ustun birga

```python
from abc import ABC, abstractmethod


class Xodim(ABC):                                  # ABSTRACTION
    def __init__(self, ism, maosh):
        self.ism = ism
        self.__maosh = maosh                       # ENCAPSULATION

    @property
    def maosh(self):
        return self.__maosh

    @maosh.setter
    def maosh(self, qiymat):
        if qiymat < 0:
            raise ValueError("Maosh manfiy bo'lmaydi!")
        self.__maosh = qiymat

    @abstractmethod
    def vazifa(self):
        pass

    def tanishtir(self):
        return f"{self.ism} | {self.vazifa()} | {self.maosh} so'm"


class Dasturchi(Xodim):                            # INHERITANCE
    def vazifa(self):                              # POLYMORPHISM
        return "Kod yozadi"


class Dizayner(Xodim):
    def vazifa(self):
        return "Dizayn chizadi"


class Menejer(Xodim):
    def __init__(self, ism, maosh, jamoa_soni):
        super().__init__(ism, maosh)
        self.jamoa_soni = jamoa_soni

    def vazifa(self):
        return f"{self.jamoa_soni} kishilik jamoani boshqaradi"


xodimlar = [
    Dasturchi("Ali", 8000000),
    Dizayner("Vali", 6000000),
    Menejer("Sardor", 10000000, 5),
]

for x in xodimlar:
    print(x.tanishtir())

xodimlar[0].maosh = 9000000       # setter orqali
```

**Natija:**

```
Ali | Kod yozadi | 8000000 so'm
Vali | Dizayn chizadi | 6000000 so'm
Sardor | 5 kishilik jamoani boshqaradi | 10000000 so'm
```

| Ustun | Kodda qayerda |
|-------|---------------|
| Encapsulation | `__maosh` private, `@property` va setter |
| Abstraction | `Xodim(ABC)`, `@abstractmethod vazifa()` |
| Inheritance | `Dasturchi(Xodim)`, `super().__init__()` |
| Polymorphism | Har bir klassda `vazifa()` turlicha ishlaydi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `BankHisobi` klassini yarating: balans private bo'lsin, `@property` orqali o'qilsin, manfiy qiymatga setter xato bersin.
2. `Talaba` klassida yosh uchun `@property` va `@yosh.setter` yozing.
3. `Shakl` abstrakt klassini yarating (`yuza()` abstrakt metod), undan `Kvadrat`, `Doira`, `Uchburchak` ni meros oling.
4. Abstrakt klassdan obyekt yaratishga urinib, xatoni kuzating.
5. `Hayvon` klassidan `It`, `Mushuk`, `Qush` ni meros oling, `super().__init__()` ishlating.
6. Ota klassning metodini bola klassda qayta yozing (overriding).
7. `isinstance()` va `issubclass()` bilan tekshiruvlar bajaring.
8. Bir nechta otadan meros oluvchi klass yarating va `__mro__` ni chiqaring.
9. Turli klasslarda bir xil nomli metod yozib, bitta sikl ichida chaqiring (polimorfizm, duck typing).
10. `Xodim` → `Dasturchi`, `Menejer` tizimini yarating: 4 ustunning hammasi ishlatilsin.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Encapsulation:** ma'lumotni yashirish (`_nom`, `__nom`), `@property` bilan nazorat qilish.
- **Abstraction:** `ABC` va `@abstractmethod` bilan umumiy "shartnoma" belgilash, abstrakt klassdan obyekt yaratib bo'lmaydi.
- **Inheritance:** `class Bola(Ota)`, `super()` bilan ota klassga murojaat, metodni qayta yozish mumkin.
- **Polymorphism:** bir xil nomdagi metod turli obyektlarda turlicha ishlaydi (overriding, duck typing, operator overloading).
- Python'da klasslar `object` dan meros oladi va bir nechta otadan meros olish (multiple inheritance) mumkin.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

<div align="center">

# 👨‍💻 Author

<table align="center">
<tr>
<td align="center" width="220">

<img src="https://github.com/javlonbeksaidov-developer.png" width="150" height="150" style="border-radius:50%;" />

</td>

<td align="center">

<h3>SOFTWARE ENGINEER</h3>

<h3>Connect with me</h3>

<p align="center"><a href="https://t.me/saidov_1701"><img src="https://img.icons8.com/fluency/64/telegram-app.png" width="45" alt="Telegram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://instagram.com/#"><img src="https://img.icons8.com/fluency/64/instagram-new.png" width="45" alt="Instagram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://facebook.com/javlonbeksaidov.developer"><img src="https://img.icons8.com/fluency/64/facebook-new.png" width="45" alt="Facebook"/></a>&nbsp;&nbsp;&nbsp;<a href="https://youtube.com/@JavlonbekSaidov-Developer"><img src="https://img.icons8.com/fluency/64/youtube-play.png" width="45" alt="YouTube"/></a>&nbsp;&nbsp;&nbsp;<a href="mailto:javlonbeksaidov09@gmail.com"><img src="https://img.icons8.com/fluency/64/gmail-new.png" width="45" alt="Gmail"/></a></p>

</td>
</tr>
</table>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2500&pause=1000&center=true&vCenter=true&width=650&lines=Javlonbek+Saidov+Alijon+o%27g%27li;Python+Backend+Developer" alt="Typing SVG" />

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=120&section=footer&animation=fadeIn" width="100%"/>