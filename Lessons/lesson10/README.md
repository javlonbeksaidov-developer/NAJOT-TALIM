<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2010%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da funksiyalar (1-qism)

**Funksiya** — ma'lum bir vazifani bajaradigan, nomi berilgan kod bloki. Funksiya bir marta yoziladi, keyin kerak bo'lgan joyda qayta-qayta chaqiriladi.

**Nima uchun kerak:**

| Afzallik | Tavsif |
|----------|--------|
| Kodni qayta ishlatish | Bir xil kodni takror yozish shart emas |
| Tushunarlilik | Katta dastur kichik qismlarga bo'linadi |
| Xatoni topish oson | Muammo aniq funksiya ichidan qidiriladi |
| Qulay o'zgartirish | Kod bitta joyda o'zgartiriladi |

> Siz allaqachon tayyor funksiyalardan foydalangansiz: `print()`, `input()`, `len()`, `range()`, `type()`.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ Funksiya yaratish: `def`

**Sintaksis:**

```python
def funksiya_nomi():
    bajariladigan_kod
```

**Misol:**

```python
def salom():
    print("Salom, Dunyo!")
```

**Qoidalar:**

| Qoida | Tavsif |
|-------|--------|
| `def` | Funksiya e'lon qilish uchun kalit so'z |
| Nom | Harf yoki `_` bilan boshlanadi, kichik harf va `_` tavsiya etiladi (`hisobla_yigindi`) |
| Qavs `()` | Nomdan keyin doim yoziladi |
| Ikki nuqta `:` | Sarlavha oxirida qo'yiladi |
| Indent | Funksiya tanasi **4 ta probel** bilan suriladi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📞 Funksiyani chaqirish

Funksiya faqat yozilgani bilan ishlamaydi, uni **chaqirish** kerak.

```python
def salom():
    print("Salom, Dunyo!")

salom()
salom()
salom()
```

**Natija:**

```
Salom, Dunyo!
Salom, Dunyo!
Salom, Dunyo!
```

> ⚠️ Funksiya chaqirilishidan **oldin** e'lon qilingan bo'lishi kerak, aks holda `NameError` chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📥 Parametrlar va argumentlar

**Parametr** — funksiya e'lonida qavs ichida yoziladigan o'zgaruvchi.
**Argument** — funksiya chaqirilganda beriladigan haqiqiy qiymat.

```python
def salom(ism):          # ism — parametr
    print(f"Salom, {ism}!")

salom("Ali")             # "Ali" — argument
salom("Vali")
```

**Natija:**

```
Salom, Ali!
Salom, Vali!
```

**Bir nechta parametr:**

```python
def yigindi(a, b):
    print(a + b)

yigindi(5, 3)    # 8
yigindi(10, 20)  # 30
```

> Argumentlar soni parametrlar soniga teng bo'lishi shart, aks holda `TypeError` chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📤 `return` operatori

**Ta'rif:** funksiya natijasini chaqirilgan joyga **qaytaradi** va funksiyani tugatadi.

```python
def kvadrat(son):
    return son * son

natija = kvadrat(5)
print(natija)           # 25
print(kvadrat(3) + 1)   # 10
```

**`print` va `return` farqi:**

| | `print()` | `return` |
|---|-----------|----------|
| Vazifasi | Ekranga chiqaradi | Qiymatni qaytaradi |
| Natijani o'zgaruvchiga saqlash | Mumkin emas | Mumkin |
| Keyingi amallarda ishlatish | Mumkin emas | Mumkin |

```python
def a(x):
    print(x * 2)

def b(x):
    return x * 2

r1 = a(5)    # ekranga 10 chiqadi
r2 = b(5)    # hech narsa chiqmaydi

print(r1)    # None
print(r2)    # 10
```

**Muhim qoidalar:**

- `return` ishlagandan keyingi kod **bajarilmaydi**.
- `return` bo'lmasa, funksiya `None` qaytaradi.

```python
def test():
    return "Birinchi"
    print("Bu qator bajarilmaydi")
```

**Bir nechta qiymat qaytarish:**

```python
def hisobla(a, b):
    return a + b, a - b, a * b

y, a, k = hisobla(10, 5)
print(y, a, k)   # 15 5 50
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚙️ Standart (default) parametr

Parametrga oldindan qiymat berilsa, argument yozilmaganda shu qiymat ishlatiladi.

```python
def salom(ism, til="uz"):
    if til == "uz":
        print(f"Salom, {ism}!")
    else:
        print(f"Hello, {ism}!")

salom("Ali")          # Salom, Ali!
salom("Ali", "en")    # Hello, Ali!
```

> ⚠️ Standart qiymatli parametrlar **oxirida** yoziladi: `def f(a, b=2)` to'g'ri, `def f(a=1, b)` xato.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏷️ Argument berish usullari

| Usul | Misol | Tavsif |
|------|-------|--------|
| Pozitsion | `ayir(10, 3)` | Argumentlar tartib bo'yicha beriladi |
| Nomli (keyword) | `ayir(b=3, a=10)` | Parametr nomi bilan beriladi, tartib muhim emas |

```python
def ayir(a, b):
    return a - b

print(ayir(10, 3))        # 7
print(ayir(b=3, a=10))    # 7
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✨ `*args` (ixtiyoriy sondagi argument)

Argumentlar soni oldindan noma'lum bo'lsa ishlatiladi. Qiymatlar **kortej** sifatida keladi.

```python
def jami(*sonlar):
    return sum(sonlar)

print(jami(1, 2))           # 3
print(jami(1, 2, 3, 4, 5))  # 15
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 O'zgaruvchi ko'lami (scope)

| Tur | Tavsif |
|-----|--------|
| **Lokal** | Funksiya ichida e'lon qilingan, faqat shu yerda ishlaydi |
| **Global** | Funksiyadan tashqarida e'lon qilingan, hamma joyda ko'rinadi |

```python
x = 10              # global

def test():
    y = 5           # lokal
    print(x, y)

test()              # 10 5
print(y)            # NameError: y faqat funksiya ichida mavjud
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Docstring (izoh)

Funksiya nima qilishini tushuntiruvchi matn, tanasining boshiga yoziladi.

```python
def doira_yuzi(r):
    """Doira yuzini hisoblaydi. r — radius."""
    return 3.14 * r ** 2

print(doira_yuzi(5))         # 78.5
help(doira_yuzi)             # docstring'ni ko'rsatadi
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 Bo'sh funksiya: `pass`

Funksiya tanasi hozircha bo'sh bo'lsa, `pass` yoziladi.

```python
def keyin_yozaman():
    pass
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Juft yoki toqligini aniqlash:**

```python
def juftmi(son):
    return son % 2 == 0

print(juftmi(4))   # True
print(juftmi(7))   # False
```

**Ikki sonning kattasi:**

```python
def katta(a, b):
    if a > b:
        return a
    return b

print(katta(8, 12))   # 12
```

**Faktorial:**

```python
def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

print(faktorial(5))   # 120
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Ismni qabul qilib, `Salom, <ism>!` chiqaradigan funksiya yozing.
2. Ikki sonning yig'indisini qaytaradigan funksiya yozing.
3. Sonning musbat, manfiy yoki nol ekanini aniqlovchi funksiya yozing.
4. 1 dan `n` gacha sonlar yig'indisini hisoblovchi funksiya yozing.
5. Ro'yxatdagi eng katta sonni topuvchi funksiya yozing.
6. Radius bo'yicha doira yuzi va aylana uzunligini qaytaruvchi funksiya yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- Funksiya `def` kalit so'zi bilan yaratiladi va **nomi bilan chaqiriladi**.
- **Parametr** e'londa, **argument** chaqirishda yoziladi.
- `return` natijani qaytaradi, `print` esa faqat ekranga chiqaradi.
- Standart qiymatli parametrlar eng oxirida yoziladi.
- Funksiya ichidagi o'zgaruvchilar **lokal** bo'ladi.

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