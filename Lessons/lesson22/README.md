<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2022%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 OOP: Obyektga yo'naltirilgan dasturlash

**OOP (Object-Oriented Programming)** — dasturni **obyektlar** orqali tuzish usuli. Har bir obyekt o'z **ma'lumotlari** (atributlar) va **harakatlari** (metodlar) ga ega bo'ladi.

| Tushuncha | Tavsif | Misol |
|-----------|--------|-------|
| **Class (klass)** | Obyekt yaratish uchun **shablon** (chizma) | `Talaba` |
| **Object (obyekt)** | Klassdan yaratilgan **aniq nusxa** | `Ali`, `Vali` |
| **Attribut** | Obyektning xususiyati (ma'lumoti) | `ism`, `yosh` |
| **Metod** | Obyektning harakati (klass ichidagi funksiya) | `salom_ber()` |

> 💡 Masalan, "Mashina" — klass (shablon), "Cobalt", "Nexia" — obyektlar. Hammasida `rang`, `narx` (atribut) va `yurish()`, `toxta()` (metod) bor.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏗️ Klass yaratish: `class`

**Sintaksis:**

```python
class KlassNomi:
    # klass tanasi
```

**Eng oddiy klass:**

```python
class Talaba:
    pass

t1 = Talaba()
print(type(t1))    # <class '__main__.Talaba'>
```

**Qoidalar:**

| Qoida | Tavsif |
|-------|--------|
| `class` | Klass e'lon qilish uchun kalit so'z |
| Nom | **PascalCase** bilan yoziladi: `Talaba`, `BankHisobi` |
| Ikki nuqta `:` | Klass sarlavhasi oxirida qo'yiladi |
| Indent | Klass tanasi **4 ta probel** bilan suriladi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚙️ `__init__` metodi (konstruktor)

**Ta'rif:** obyekt yaratilganda **avtomatik** chaqiriladigan maxsus metod. Obyektning boshlang'ich atributlari shu yerda beriladi.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

t1 = Talaba("Ali", 20)
t2 = Talaba("Vali", 22)

print(t1.ism, t1.yosh)    # Ali 20
print(t2.ism, t2.yosh)    # Vali 22
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Nomi | Doim `__init__` (ikki tomondan ikkita pastki chiziq) |
| Chaqirilishi | `Talaba("Ali", 20)` yozilganda o'zi ishga tushadi |
| Qaytaradigan qiymat | Hech narsa qaytarmaydi (`return` yozilmaydi) |
| Vazifasi | Obyektning atributlarini o'rnatish |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪞 `self` nima?

**`self`** — joriy obyektning **o'ziga** havola. Metod qaysi obyekt uchun chaqirilsa, `self` shu obyekt bo'ladi.

```python
class Talaba:
    def __init__(self, ism):
        self.ism = ism      # self.ism — obyektning atributi, ism — parametr

t1 = Talaba("Ali")
t2 = Talaba("Vali")

print(t1.ism)    # Ali
print(t2.ism)    # Vali
```

**Qoidalar:**

- `self` har bir oddiy metodning **birinchi parametri** bo'lishi shart.
- Metod chaqirilganda `self` ni **yozmaysiz**, Python o'zi uzatadi.
- Nomi `self` bo'lishi odat (qoida), boshqa nom ham ishlaydi, lekin ishlatilmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏷️ Atributlar

## 1. Obyekt atributlari (instance attributes)

Har bir obyektning **o'z** qiymati bo'ladi. `__init__` ichida `self.nom` ko'rinishida yoziladi.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

t1 = Talaba("Ali", 20)
t2 = Talaba("Vali", 22)

t1.yosh = 21           # faqat t1 o'zgaradi
print(t1.yosh)         # 21
print(t2.yosh)         # 22
```

## 2. Klass atributlari (class attributes)

**Hamma** obyektlar uchun umumiy. Klass ichida, metodlardan tashqarida yoziladi.

```python
class Talaba:
    maktab = "Najot Ta'lim"        # klass atributi

    def __init__(self, ism):
        self.ism = ism

t1 = Talaba("Ali")
t2 = Talaba("Vali")

print(t1.maktab)       # Najot Ta'lim
print(t2.maktab)       # Najot Ta'lim
print(Talaba.maktab)   # Najot Ta'lim (klass nomi orqali ham)
```

| | Obyekt atributi | Klass atributi |
|---|-----------------|----------------|
| Qayerda yoziladi | `__init__` ichida, `self.nom` | Klass tanasida, metoddan tashqarida |
| Kimga tegishli | Har bir obyektga alohida | Barcha obyektlarga umumiy |
| Murojaat | `obyekt.nom` | `Klass.nom` yoki `obyekt.nom` |

## 3. Atributlar bilan ishlash

```python
t = Talaba("Ali")

t.yosh = 20                  # yangi atribut qo'shish
t.yosh = 21                  # o'zgartirish
print(t.yosh)                # 21

del t.yosh                   # o'chirish
```

| Funksiya | Vazifasi |
|----------|----------|
| `hasattr(obj, "nom")` | Atribut borligini tekshiradi (`True`/`False`) |
| `getattr(obj, "nom", default)` | Atribut qiymatini oladi |
| `setattr(obj, "nom", qiymat)` | Atributni o'rnatadi |
| `delattr(obj, "nom")` | Atributni o'chiradi |

```python
print(hasattr(t, "ism"))           # True
print(getattr(t, "kurs", 1))       # 1 (kurs yo'q, default qaytdi)
setattr(t, "kurs", 2)
print(t.kurs)                      # 2
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎬 Metodlar

**Ta'rif:** klass ichida e'lon qilingan funksiya. Obyektning **harakatini** bildiradi. Birinchi parametri doim `self`.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salom_ber(self):
        print(f"Salom, men {self.ism}man. Yoshim {self.yosh} da.")

    def yosh_oshir(self, necha=1):
        self.yosh += necha

t = Talaba("Ali", 20)

t.salom_ber()          # Salom, men Alim an. Yoshim 20 da.
t.yosh_oshir()
t.yosh_oshir(3)
print(t.yosh)          # 24
```

**Metod va oddiy funksiya farqi:**

| | Funksiya | Metod |
|---|----------|-------|
| Qayerda | Klassdan tashqarida | Klass ichida |
| Birinchi parametr | Ixtiyoriy | `self` |
| Chaqirilishi | `nom()` | `obyekt.nom()` |

**Metoddan qiymat qaytarish:**

```python
class Doira:
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2

    def uzunlik(self):
        return 2 * 3.14 * self.radius

d = Doira(5)
print(d.yuza())        # 78.5
print(d.uzunlik())     # 31.4
```

**Metod ichida boshqa metodni chaqirish:**

```python
class Talaba:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        return f"Salom, {self.ism}"

    def tanishtir(self):
        print(self.salom())      # self.metod_nomi()

Talaba("Ali").tanishtir()        # Salom, Ali
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🖨️ `__str__` metodi

Obyektni `print()` qilganda qanday ko'rinishda chiqishini belgilaydi.

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

t = Talaba("Ali", 20)
print(t)       # <__main__.Talaba object at 0x000001...>  (tushunarsiz)
```

`__str__` yozilgandan keyin:

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __str__(self):
        return f"Talaba: {self.ism}, {self.yosh} yosh"

t = Talaba("Ali", 20)
print(t)       # Talaba: Ali, 20 yosh
```

> `__str__` **matn (`str`) qaytarishi** shart, `print` qilmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔒 Atribut turlari (kirish darajasi)

Python'da qat'iy yopiq atribut yo'q, lekin **nom berish qoidasi** bor:

| Yozilishi | Ma'nosi | Misol |
|-----------|---------|-------|
| `nom` | Ochiq (public), hamma foydalanadi | `self.ism` |
| `_nom` | Himoyalangan (protected), "ichki foydalanish uchun" degan kelishuv | `self._yosh` |
| `__nom` | Yopiq (private), nomi o'zgartiriladi, tashqaridan to'g'ridan-to'g'ri olinmaydi | `self.__parol` |

```python
class Hisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans         # private

    def balans_korish(self):
        return self.__balans

    def pul_qosh(self, summa):
        if summa > 0:
            self.__balans += summa

h = Hisob("Ali", 1000)
h.pul_qosh(500)

print(h.balans_korish())     # 1500
print(h.__balans)            # AttributeError
```

> ⚠️ `_nom` Python tomonidan **majburan** yopilmaydi, bu faqat dasturchilar uchun kelishuv. `__nom` esa tashqaridan oddiy yo'l bilan olinmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 Obyektlarni sanash (klass atributi bilan)

```python
class Talaba:
    soni = 0                       # klass atributi

    def __init__(self, ism):
        self.ism = ism
        Talaba.soni += 1

t1 = Talaba("Ali")
t2 = Talaba("Vali")
t3 = Talaba("Sardor")

print(Talaba.soni)    # 3
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**1. Bank hisobi:**

```python
class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def qosh(self, summa):
        self.balans += summa
        print(f"{summa} so'm qo'shildi. Balans: {self.balans}")

    def yech(self, summa):
        if summa > self.balans:
            print("Mablag' yetarli emas!")
        else:
            self.balans -= summa
            print(f"{summa} so'm yechildi. Balans: {self.balans}")

h = BankHisobi("Ali", 10000)
h.qosh(5000)      # 5000 so'm qo'shildi. Balans: 15000
h.yech(20000)     # Mablag' yetarli emas!
h.yech(3000)      # 3000 so'm yechildi. Balans: 12000
```

**2. To'g'ri to'rtburchak:**

```python
class Togri:
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi

    def perimetr(self):
        return 2 * (self.eni + self.boyi)

    def __str__(self):
        return f"To'g'ri to'rtburchak {self.eni}x{self.boyi}"

t = Togri(4, 6)
print(t)               # To'g'ri to'rtburchak 4x6
print(t.yuza())        # 24
print(t.perimetr())    # 20
```

**3. Obyektlar ro'yxati:**

```python
class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    def __str__(self):
        return f"{self.nom}: {self.narx} so'm"

mahsulotlar = [
    Mahsulot("Non", 4000),
    Mahsulot("Sut", 12000),
    Mahsulot("Tuxum", 15000),
]

for m in mahsulotlar:
    print(m)

jami = sum(m.narx for m in mahsulotlar)
print("Jami:", jami, "so'm")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `Talaba` klassini yarating: `ism`, `yosh`, `kurs` atributlari bo'lsin.
2. `Talaba` klassiga `salom_ber()` metodini qo'shing.
3. `__str__` metodi yordamida obyektni chiroyli chiqaring.
4. `Mashina` klassini yarating: `nom`, `rang`, `tezlik` atributlari va `tezlashtir()`, `tormozla()` metodlari bo'lsin.
5. `Doira` klassini yarating: yuza va aylana uzunligini hisoblovchi metodlar yozing.
6. `BankHisobi` klassini yarating: pul qo'shish va yechish metodlari bo'lsin, balans private bo'lsin.
7. Klass atributi yordamida yaratilgan obyektlar sonini hisoblang.
8. Bir klassdan 3 ta obyekt yarating, ro'yxatga joylab, sikl bilan chiqaring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Klass** — shablon, **obyekt** — undan yaratilgan nusxa.
- `__init__` obyekt yaratilganda avtomatik ishlaydi va atributlarni o'rnatadi.
- `self` — joriy obyektning o'ziga havola, har bir metodning birinchi parametri.
- **Obyekt atributlari** har bir obyektga alohida, **klass atributlari** hammaga umumiy.
- **Metod** — klass ichidagi funksiya, `obyekt.metod()` ko'rinishida chaqiriladi.
- `__str__` obyektni `print()` qilganda ko'rinishini belgilaydi.
- `_nom` va `__nom` atributning ichki ekanini bildiradi.

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