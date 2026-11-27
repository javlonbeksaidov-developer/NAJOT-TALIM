<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2009%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python `random` moduli

**`random`** — Python'ning standart moduli bo'lib, tasodifiy sonlar yaratish va ro'yxatdan tasodifiy element tanlash uchun ishlatiladi. Uni alohida o'rnatish shart emas, faqat import qilinadi.

```python
import random
```

**Asosiy funksiyalar:**

| Funksiya | Vazifasi |
|----------|----------|
| `random()` | `0` dan `1` gacha tasodifiy kasr son |
| `randint(a, b)` | `a` dan `b` gacha tasodifiy butun son |
| `choice(ro'yxat)` | Ro'yxatdan bitta tasodifiy element |
| `sample(ro'yxat, k)` | Ro'yxatdan `k` ta takrorlanmas element |
| `shuffle(ro'yxat)` | Ro'yxatni aralashtiradi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎲 1. `random()`

**Ta'rif:** `0.0` dan `1.0` gacha (`1.0` kirmaydi) tasodifiy `float` son qaytaradi.

```python
import random

son = random.random()
print(son)
```

**Natija (har safar boshqacha):**

```
0.7364712141640124
```

> Kattaroq oraliq kerak bo'lsa, ko'paytiriladi: `random.random() * 100`

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 2. `randint(a, b)`

**Ta'rif:** `a` va `b` oralig'ida tasodifiy **butun** son qaytaradi.

```python
import random

son = random.randint(1, 10)
print(son)
```

**Natija (masalan):**

```
7
```

> ⚠️ `randint` da ikkala chegara (`a` va `b`) **kiritiladi**. `range()` dan farqi shu.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎯 3. `choice()`

**Ta'rif:** ro'yxat, kortej yoki satrdan **bitta** tasodifiy element tanlaydi.

```python
import random

mevalar = ["olma", "anor", "uzum", "behi"]
print(random.choice(mevalar))
print(random.choice("Python"))
```

**Natija (masalan):**

```
uzum
h
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧺 4. `sample()`

**Ta'rif:** ro'yxatdan `k` ta **takrorlanmaydigan** tasodifiy element tanlaydi. Natija yangi ro'yxat bo'ladi.

```python
import random

sonlar = [10, 20, 30, 40, 50]
print(random.sample(sonlar, 3))
```

**Natija (masalan):**

```
[40, 10, 50]
```

> ⚠️ `k` ro'yxat uzunligidan katta bo'lsa, `ValueError` xatosi chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔀 5. `shuffle()`

**Ta'rif:** ro'yxat elementlarini **joyida** aralashtiradi. Yangi ro'yxat qaytarmaydi, `None` qaytaradi.

```python
import random

kartalar = [1, 2, 3, 4, 5]
random.shuffle(kartalar)
print(kartalar)
```

**Natija (masalan):**

```
[3, 5, 1, 4, 2]
```

> ⚠️ `shuffle` faqat o'zgartiriladigan ketma-ketlik (ro'yxat) bilan ishlaydi. Kortej va satr bilan ishlamaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧮 Xususiyatlari

| Funksiya | Qaytaradigan tur | Asl ro'yxatni o'zgartiradimi |
|----------|------------------|------------------------------|
| `random()` | `float` | Yo'q |
| `randint()` | `int` | Yo'q |
| `choice()` | Element | Yo'q |
| `sample()` | `list` | Yo'q |
| `shuffle()` | `None` | **Ha** |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol

**Son topish o'yini:**

```python
import random

yashirin = random.randint(1, 10)
taxmin = int(input("1 dan 10 gacha son kiriting: "))

if taxmin == yashirin:
    print("Topdingiz! 🎉")
else:
    print(f"Yutqazdingiz. Yashirin son: {yashirin}")
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