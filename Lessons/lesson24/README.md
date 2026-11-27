<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2024%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 OOP metodlari

Klass ichida yozilgan funksiyalar **metod** deyiladi. Python'da metodlarning bir nechta turi bor:

| Metod turi | Birinchi parametr | Dekorator | Nimaga murojaat qiladi |
|------------|-------------------|-----------|------------------------|
| **Instance method** | `self` | Yo'q | Obyektga (uning atributlariga) |
| **Class method** | `cls` | `@classmethod` | Klassga (klass atributlariga) |
| **Static method** | Yo'q | `@staticmethod` | Hech nimaga, mustaqil funksiya |
| **Dunder method** | `self` | Yo'q | Python'ning maxsus `__nom__` metodlari |

```python
class Talaba:
    maktab = "Najot Ta'lim"

    def __init__(self, ism):             # dunder method
        self.ism = ism

    def salom(self):                     # instance method
        return f"Salom, {self.ism}"

    @classmethod
    def maktab_nomi(cls):                # class method
        return cls.maktab

    @staticmethod
    def yosh_togrimi(yosh):              # static method
        return 0 < yosh < 120
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 1️⃣ Instance method (obyekt metodi)

**Ta'rif:** eng oddiy metod turi. Birinchi parametri `self`, ya'ni **aniq bir obyekt** bilan ishlaydi. Obyektning atributlarini o'qiy va o'zgartira oladi.

```python
class Hisob:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def qosh(self, summa):
        self.balans += summa

    def korsat(self):
        print(f"{self.egasi}: {self.balans} so'm")

h = Hisob("Ali", 1000)
h.qosh(500)
h.korsat()          # Ali: 1500 so'm
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Chaqirilishi | `obyekt.metod()` |
| `self` | Python o'zi uzatadi, chaqirishda yozilmaydi |
| Kirish huquqi | Obyekt atributlari va klass atributlari |
| Obyektsiz | `Klass.metod()` ko'rinishida chaqirib bo'lmaydi (`self` yetishmaydi) |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 2️⃣ `@classmethod` (klass metodi)

**Ta'rif:** obyektga emas, **klassning o'ziga** tegishli metod. Birinchi parametri `cls` (klassning o'zi). `@classmethod` dekoratori bilan yoziladi.

```python
class Talaba:
    soni = 0

    def __init__(self, ism):
        self.ism = ism
        Talaba.soni += 1

    @classmethod
    def soni_korish(cls):
        return cls.soni

Talaba("Ali")
Talaba("Vali")

print(Talaba.soni_korish())    # 2
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Dekorator | `@classmethod` |
| Birinchi parametr | `cls` (klass) |
| Chaqirilishi | `Klass.metod()` yoki `obyekt.metod()` |
| Kirish huquqi | Klass atributlari. Obyekt atributlariga (`self.ism`) **kira olmaydi** |

## Muqobil konstruktor (eng ko'p ishlatiladigan holat)

Obyektni `__init__` dan boshqacha usulda yaratish uchun ishlatiladi.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    @classmethod
    def matndan(cls, matn):
        ism, yosh = matn.split("-")
        return cls(ism, int(yosh))

    @classmethod
    def lugatdan(cls, lugat):
        return cls(lugat["ism"], lugat["yosh"])

t1 = Talaba("Ali", 20)
t2 = Talaba.matndan("Vali-22")
t3 = Talaba.lugatdan({"ism": "Sardor", "yosh": 19})

print(t2.ism, t2.yosh)    # Vali 22
print(t3.ism, t3.yosh)    # Sardor 19
```

## Klass atributini o'zgartirish

```python
class Kompaniya:
    nom = "Najot Ta'lim"

    @classmethod
    def nom_ozgartir(cls, yangi_nom):
        cls.nom = yangi_nom

Kompaniya.nom_ozgartir("Yangi nom")
print(Kompaniya.nom)    # Yangi nom
```

> 💡 `cls` o'rniga klass nomini (`Talaba(...)`) yozish ham ishlaydi, lekin `cls` **meros olishda** to'g'ri ishlaydi: bola klassdan chaqirilsa, `cls` bola klass bo'ladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 3️⃣ `@staticmethod` (statik metod)

**Ta'rif:** `self` ham, `cls` ham **olmaydi**. Klass ichida yozilgan oddiy funksiya. Obyekt yoki klass ma'lumotlariga muhtoj bo'lmagan, lekin mavzu jihatidan shu klassga tegishli yordamchi amallar uchun ishlatiladi.

```python
class Matematika:
    @staticmethod
    def juftmi(son):
        return son % 2 == 0

    @staticmethod
    def kvadrat(son):
        return son ** 2

print(Matematika.juftmi(8))     # True
print(Matematika.kvadrat(5))    # 25

m = Matematika()
print(m.juftmi(7))              # False (obyekt orqali ham ishlaydi)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Dekorator | `@staticmethod` |
| Birinchi parametr | Maxsus parametr yo'q |
| Chaqirilishi | `Klass.metod()` yoki `obyekt.metod()` |
| Kirish huquqi | Obyekt va klass atributlariga **kira olmaydi** |
| Vazifasi | Yordamchi (utility) funksiya |

**Amaliy misol: tekshiruvchi metod**

```python
class Talaba:
    def __init__(self, ism, yosh):
        if not Talaba.yosh_togrimi(yosh):
            raise ValueError("Yosh noto'g'ri!")
        self.ism = ism
        self.yosh = yosh

    @staticmethod
    def yosh_togrimi(yosh):
        return 0 < yosh < 120

print(Talaba.yosh_togrimi(20))    # True
t = Talaba("Ali", 200)            # ValueError: Yosh noto'g'ri!
```

## Qaysi birini tanlash?

| Savol | Javob |
|-------|-------|
| Metod obyekt atributlari (`self.ism`) bilan ishlaydimi? | **Instance method** |
| Metod klass atributlari yoki yangi obyekt yaratish bilan ishlaydimi? | **`@classmethod`** |
| Metod klass ma'lumotlariga umuman muhtoj emasmi? | **`@staticmethod`** |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✨ 4️⃣ Dunder metodlar (magic methods)

**Ta'rif:** nomi **ikkita pastki chiziq bilan boshlanib, shunday tugaydigan** (`__nom__`) maxsus metodlar. **Double underscore** so'zidan **dunder** deyiladi. Ularni odatda o'zingiz chaqirmaysiz, Python **ma'lum vaziyatda o'zi chaqiradi**.

| Siz yozasiz | Python chaqiradi |
|-------------|------------------|
| `Talaba("Ali")` | `__init__` |
| `print(t)` | `__str__` |
| `len(t)` | `__len__` |
| `a + b` | `__add__` |
| `a == b` | `__eq__` |

## `__init__` va `__str__`

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __str__(self):
        return f"{self.ism} ({self.yosh} yosh)"

t = Talaba("Ali", 20)
print(t)         # Ali (20 yosh)
print(str(t))    # Ali (20 yosh)
```

## `__repr__`

Obyektning **dasturchi uchun** ko'rinishi. Konsolda va ro'yxat ichida shu ko'rinadi. Odatda obyektni qayta yaratish mumkin bo'lgan matn qaytariladi.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __str__(self):
        return f"{self.ism}, {self.yosh} yosh"

    def __repr__(self):
        return f"Talaba('{self.ism}', {self.yosh})"

t = Talaba("Ali", 20)
print(t)               # Ali, 20 yosh        (__str__)
print(repr(t))         # Talaba('Ali', 20)   (__repr__)
print([t])             # [Talaba('Ali', 20)] (ro'yxat ichida __repr__)
```

| | `__str__` | `__repr__` |
|---|-----------|------------|
| Kim uchun | Oddiy foydalanuvchi | Dasturchi |
| Chaqiriladi | `print()`, `str()` | `repr()`, ro'yxat ichida, konsolda |
| `__str__` yo'q bo'lsa | `__repr__` ishlatiladi | Standart ko'rinish |

## `__len__`, `__getitem__`, `__contains__`

```python
class Sinf:
    def __init__(self, talabalar):
        self.talabalar = talabalar

    def __len__(self):
        return len(self.talabalar)

    def __getitem__(self, indeks):
        return self.talabalar[indeks]

    def __contains__(self, ism):
        return ism in self.talabalar

s = Sinf(["Ali", "Vali", "Sardor"])

print(len(s))          # 3
print(s[0])            # Ali
print("Vali" in s)     # True

for t in s:            # __getitem__ bor bo'lsa, sikl ham ishlaydi
    print(t)
```

## Operatorlarni qayta aniqlash

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, boshqa):
        return Vektor(self.x + boshqa.x, self.y + boshqa.y)

    def __sub__(self, boshqa):
        return Vektor(self.x - boshqa.x, self.y - boshqa.y)

    def __mul__(self, son):
        return Vektor(self.x * son, self.y * son)

    def __eq__(self, boshqa):
        return self.x == boshqa.x and self.y == boshqa.y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

a = Vektor(1, 2)
b = Vektor(3, 4)

print(a + b)          # Vektor(4, 6)
print(b - a)          # Vektor(2, 2)
print(a * 3)          # Vektor(3, 6)
print(a == Vektor(1, 2))    # True
```

## Taqqoslash dunder metodlari

```python
class Talaba:
    def __init__(self, ism, ball):
        self.ism = ism
        self.ball = ball

    def __lt__(self, boshqa):
        return self.ball < boshqa.ball

    def __repr__(self):
        return f"{self.ism}({self.ball})"

royxat = [Talaba("Ali", 80), Talaba("Vali", 95), Talaba("Sardor", 70)]

print(sorted(royxat))    # [Sardor(70), Ali(80), Vali(95)]
print(max(royxat))       # Vali(95)  (__lt__ yetarli)
```

## `__call__`

Obyektni **funksiya kabi chaqirish** imkonini beradi.

```python
class Ko_paytiruvchi:
    def __init__(self, n):
        self.n = n

    def __call__(self, son):
        return son * self.n

ikki_marta = Ko_paytiruvchi(2)
print(ikki_marta(10))    # 20
```

## `__bool__`

```python
class Savat:
    def __init__(self):
        self.mahsulotlar = []

    def __bool__(self):
        return len(self.mahsulotlar) > 0

s = Savat()
print(bool(s))                  # False
s.mahsulotlar.append("Non")
print(bool(s))                  # True
```

## Eng ko'p ishlatiladigan dunder metodlar

| Metod | Qachon chaqiriladi | Misol |
|-------|--------------------|-------|
| `__init__` | Obyekt yaratilganda | `Klass()` |
| `__str__` | `print()`, `str()` | `print(obj)` |
| `__repr__` | `repr()`, konsol | `repr(obj)` |
| `__len__` | `len()` | `len(obj)` |
| `__getitem__` | Indeks bilan olish | `obj[0]` |
| `__setitem__` | Indeks bilan o'rnatish | `obj[0] = 5` |
| `__contains__` | `in` operatori | `x in obj` |
| `__call__` | Obyektni chaqirish | `obj()` |
| `__bool__` | `bool()`, `if obj:` | `if obj:` |
| `__add__` | `+` | `a + b` |
| `__sub__` | `-` | `a - b` |
| `__mul__` | `*` | `a * b` |
| `__eq__` | `==` | `a == b` |
| `__lt__` | `<` | `a < b` |
| `__gt__` | `>` | `a > b` |
| `__del__` | Obyekt o'chirilganda | `del obj` |

> ⚠️ **Eslatma:** `__eq__` yozilsa, Python obyektni avtomatik **hash qilib bo'lmaydigan** (to'plam elementi yoki lug'at kaliti bo'la olmaydigan) qilib qo'yadi. Kerak bo'lsa, `__hash__` ham yoziladi.

> ⚠️ Faqat Python'da bor dunder nomlaridan foydalaning. O'zingiz `__mening_metodim__` kabi nom o'ylab topmang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol: hammasi birga

```python
class Mahsulot:
    soni = 0

    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx
        Mahsulot.soni += 1

    # instance method
    def chegirma(self, foiz):
        return self.narx * (100 - foiz) / 100

    # class method
    @classmethod
    def matndan(cls, matn):
        nom, narx = matn.split(":")
        return cls(nom, int(narx))

    @classmethod
    def jami_soni(cls):
        return cls.soni

    # static method
    @staticmethod
    def narx_togrimi(narx):
        return narx > 0

    # dunder methods
    def __str__(self):
        return f"{self.nom}: {self.narx} so'm"

    def __repr__(self):
        return f"Mahsulot('{self.nom}', {self.narx})"

    def __add__(self, boshqa):
        return self.narx + boshqa.narx

    def __lt__(self, boshqa):
        return self.narx < boshqa.narx


m1 = Mahsulot("Non", 4000)
m2 = Mahsulot.matndan("Sut:12000")

print(m1)                         # Non: 4000 so'm
print(m2.chegirma(10))            # 10800.0
print(m1 + m2)                    # 16000
print(m1 < m2)                    # True
print(Mahsulot.jami_soni())       # 2
print(Mahsulot.narx_togrimi(-5))  # False
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `Talaba` klassiga `salom_ber()` instance metodini yozing.
2. `@classmethod` yordamida `"Ali-20"` matnidan `Talaba` obyekti yaratadigan metod yozing.
3. Klass atributi bilan yaratilgan obyektlar sonini hisoblab, `@classmethod` orqali qaytaring.
4. `@staticmethod` yordamida sonning tubligini tekshiruvchi metod yozing.
5. `__str__` va `__repr__` metodlarini yozib, farqini ko'rsating.
6. `Vektor` klassi uchun `__add__`, `__sub__` va `__eq__` metodlarini yozing.
7. `__len__` va `__getitem__` yordamida `len(obyekt)` va `obyekt[0]` ishlaydigan klass yarating.
8. `__lt__` yordamida talabalar ro'yxatini ball bo'yicha `sorted()` bilan tartiblang.
9. `__call__` yordamida funksiya kabi chaqiriladigan klass yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Instance method** (`self`) obyekt ma'lumotlari bilan ishlaydi.
- **`@classmethod`** (`cls`) klass ma'lumotlari bilan ishlaydi va muqobil konstruktor yaratishda ishlatiladi.
- **`@staticmethod`** `self` va `cls` ni olmaydi, klass ichidagi yordamchi funksiya.
- **Dunder metodlar** (`__nom__`) ni Python ma'lum vaziyatlarda o'zi chaqiradi.
- `__str__` oddiy foydalanuvchi uchun, `__repr__` dasturchi uchun ko'rinish.
- `__add__`, `__eq__`, `__lt__` kabi metodlar bilan operatorlarni o'z klassingizga moslash mumkin.

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