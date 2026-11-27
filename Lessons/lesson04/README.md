<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2003%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da ma'lumot turlari

**Ma'lumot turi** — o'zgaruvchida qanday qiymat saqlanishini va u bilan qanday amallar bajarilishini belgilaydi.

Eng asosiy turlar:

- **`int`** — butun sonlar
- **`float`** — kasr sonlar
- **`str`** — matn (satr)

Turni aniqlash uchun `type()` funksiyasi ishlatiladi:

```python
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Salom"))   # <class 'str'>
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 `int` (butun son)

**Ta'rif:** kasr qismi yo'q butun sonlar (musbat, manfiy va nol).

```python
a = 25
b = -7
c = 0
print(a, b, c)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Kasr qismi | Yo'q |
| Hajm chegarasi | Yo'q (xotira yetguncha katta son saqlash mumkin) |
| Amallar | `+`, `-`, `*`, `//` (butun bo'lish), `%` (qoldiq), `**` (daraja) |
| `/` amali | Natija doim `float` bo'ladi |

```python
print(10 + 3)    # 13
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 5)    # 32
print(10 / 2)    # 5.0
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔣 `float` (kasr son)

**Ta'rif:** kasr qismi bor sonlar. Kasr qismi nuqta (`.`) bilan ajratiladi.

```python
narx = 12.5
pi = 3.14
manfiy = -0.75
print(narx, pi, manfiy)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Ajratgich | Vergul emas, **nuqta** (`3.14`) |
| Aniqlik | Taxminiy, kichik xatolik bo'lishi mumkin |
| Yaxlitlash | `round(son, xona)` |
| Aralash amal | `int` va `float` birga ishlatilsa, natija `float` bo'ladi |

```python
print(0.1 + 0.2)           # 0.30000000000000004
print(round(0.1 + 0.2, 2)) # 0.3
print(5 + 2.5)             # 7.5
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔤 `str` (matn)

**Ta'rif:** tirnoq ichiga olingan belgilar ketma-ketligi.

```python
ism = "Ali"
fam = 'Valiyev'
matn = """Ko'p
qatorli matn"""
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Tirnoq | `' '`, `" "` yoki `""" """` |
| Birlashtirish | `+` operatori: `"Sa" + "lom"` → `"Salom"` |
| Takrorlash | `*` operatori: `"Ha" * 3` → `"HaHaHa"` |
| Uzunlik | `len("Salom")` → `5` |
| Indeks | Belgilar `0` dan boshlab raqamlanadi: `"Salom"[0]` → `"S"` |
| O'zgarmas | Satrni o'zgartirib bo'lmaydi (immutable) |

```python
s = "Python"
print(len(s))      # 6
print(s[0])        # P
print(s[-1])       # n
print(s * 2)       # PythonPython
```

> ⚠️ `"5"` va `5` bir xil emas: birinchisi `str`, ikkinchisi `int`.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 Turlarni o'zgartirish

| Funksiya | Vazifasi | Misol |
|----------|----------|-------|
| `int()` | Butun songa o'tkazadi | `int("25")` → `25` |
| `float()` | Kasr songa o'tkazadi | `float("3.5")` → `3.5` |
| `str()` | Matnga o'tkazadi | `str(100)` → `"100"` |

```python
print(int(7.9))        # 7 (kasr qismi tashlanadi)
print("5" + "3")       # 53
print(int("5") + 3)    # 8
```

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