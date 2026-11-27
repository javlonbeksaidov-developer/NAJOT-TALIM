<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2015%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da kortejlar (`tuple`)

**Kortej (tuple)** — elementlari **tartiblangan** va **o'zgarmas** ro'yxat. Kortej yaratilgandan keyin uning elementlarini o'zgartirib, qo'shib yoki o'chirib bo'lmaydi.

```python
rang = ("qizil", "yashil", "ko'k")

print(rang[0])       # qizil
print(type(rang))    # <class 'tuple'>
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Qavs | Oddiy qavs `( )` |
| Tartiblangan | Elementlar qo'shilgan tartibda saqlanadi, indeks bilan murojaat qilinadi |
| O'zgarmas (immutable) | Yaratilgandan keyin o'zgartirib bo'lmaydi |
| Takrorlanish | Bir xil qiymatlar bo'lishi mumkin |
| Tur | Turli xil ma'lumot turlarini saqlashi mumkin |
| Tezlik | Ro'yxatga (`list`) qaraganda tezroq va kam xotira egallaydi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ Kortej yaratish

```python
# 1. Oddiy qavs bilan
a = (1, 2, 3)

# 2. Qavssiz
b = 1, 2, 3

# 3. tuple() funksiyasi bilan
c = tuple([1, 2, 3])
d = tuple("salom")      # ('s', 'a', 'l', 'o', 'm')

# 4. Bo'sh kortej
e = ()
f = tuple()
```

> ⚠️ Bitta elementli kortejda **vergul** shart: `(5,)` kortej, `(5)` esa oddiy `int`.

```python
x = (5,)
y = (5)
print(type(x))    # <class 'tuple'>
print(type(y))    # <class 'int'>
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 Elementlarga murojaat

## Indeks

Indeks `0` dan boshlanadi, manfiy indeks oxiridan sanaydi.

```python
mevalar = ("olma", "anor", "uzum", "behi")

print(mevalar[0])     # olma
print(mevalar[-1])    # behi
```

## Kesim (slice)

```python
sonlar = (10, 20, 30, 40, 50)

print(sonlar[1:4])     # (20, 30, 40)
print(sonlar[:3])      # (10, 20, 30)
print(sonlar[::2])     # (10, 30, 50)
print(sonlar[::-1])    # (50, 40, 30, 20, 10)
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔒 O'zgarmaslik

Kortej elementini o'zgartirib bo'lmaydi.

```python
t = (1, 2, 3)
t[0] = 100       # TypeError: 'tuple' object does not support item assignment
```

**O'zgartirish kerak bo'lsa** — ro'yxatga aylantirib, o'zgartirib, qaytadan kortejga o'tkaziladi:

```python
t = (1, 2, 3)

r = list(t)
r[0] = 100
t = tuple(r)

print(t)    # (100, 2, 3)
```

> ⚠️ Agar kortej ichida o'zgaruvchan element (masalan, ro'yxat) bo'lsa, o'sha element ichini o'zgartirish mumkin:
> ```python
> t = (1, [2, 3])
> t[1].append(4)
> print(t)    # (1, [2, 3, 4])
> ```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔑 Kortej metodlari va funksiyalari

Kortej o'zgarmas bo'lgani uchun uning faqat **ikkita** metodi bor:

| Metod | Vazifasi |
|-------|----------|
| `count(x)` | `x` elementi necha marta uchrashini qaytaradi |
| `index(x)` | `x` elementining birinchi uchragan indeksini qaytaradi |

```python
t = (1, 2, 2, 3, 2)

print(t.count(2))    # 3
print(t.index(3))    # 3
```

**Umumiy funksiyalar:**

| Funksiya | Vazifasi |
|----------|----------|
| `len(t)` | Elementlar soni |
| `min(t)` | Eng kichik element |
| `max(t)` | Eng katta element |
| `sum(t)` | Elementlar yig'indisi |
| `sorted(t)` | Tartiblangan **ro'yxat** qaytaradi |

```python
t = (5, 2, 8, 1)

print(len(t))       # 4
print(min(t))       # 1
print(max(t))       # 8
print(sum(t))       # 16
print(sorted(t))    # [1, 2, 5, 8]
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ Amallar

```python
a = (1, 2)
b = (3, 4)

print(a + b)         # (1, 2, 3, 4)   birlashtirish
print(a * 3)         # (1, 2, 1, 2, 1, 2)   takrorlash
print(2 in a)        # True   mavjudligini tekshirish
print(5 not in a)    # True
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 Kortej ustida sikl

```python
mevalar = ("olma", "anor", "uzum")

for meva in mevalar:
    print(meva)

for i in range(len(mevalar)):
    print(i, mevalar[i])

for i, meva in enumerate(mevalar):
    print(i, meva)
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📦 Ochib berish (unpacking)

Kortej elementlarini alohida o'zgaruvchilarga ajratish.

```python
t = ("Ali", 20, "Toshkent")

ism, yosh, shahar = t
print(ism)      # Ali
print(yosh)     # 20
print(shahar)   # Toshkent
```

**`*` bilan qolganini yig'ish:**

```python
sonlar = (1, 2, 3, 4, 5)

birinchi, *orta, oxirgi = sonlar
print(birinchi)    # 1
print(orta)        # [2, 3, 4]
print(oxirgi)      # 5
```

**O'zgaruvchilar qiymatini almashtirish:**

```python
a = 10
b = 20
a, b = b, a
print(a, b)    # 20 10
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪆 Ichma-ich kortej

```python
t = ((1, 2), (3, 4), (5, 6))

print(t[1])        # (3, 4)
print(t[1][0])     # 3
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚖️ Kortej va ro'yxat farqi

| Xususiyat | `tuple` | `list` |
|-----------|---------|--------|
| Qavs | `( )` | `[ ]` |
| O'zgartirish | Mumkin emas | Mumkin |
| Metodlar soni | 2 ta | Ko'p |
| Tezlik | Tezroq | Sekinroq |
| Lug'at kaliti bo'lishi | Mumkin | Mumkin emas |
| Qachon ishlatiladi | O'zgarmas ma'lumot (koordinata, sana) | O'zgaruvchan ma'lumot |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Koordinatalar:**

```python
nuqta = (41.31, 69.28)    # Toshkent: kenglik, uzunlik

kenglik, uzunlik = nuqta
print(f"Kenglik: {kenglik}, Uzunlik: {uzunlik}")
```

**Funksiyadan bir nechta qiymat qaytarish:**

```python
def min_max(sonlar):
    return min(sonlar), max(sonlar)    # kortej qaytaradi

natija = min_max((4, 9, 1, 7))
print(natija)          # (1, 9)

kichik, katta = natija
print(kichik, katta)   # 1 9
```

**Kortejni lug'at kaliti sifatida ishlatish:**

```python
shaharlar = {
    (41.31, 69.28): "Toshkent",
    (39.65, 66.96): "Samarqand"
}

print(shaharlar[(41.31, 69.28)])    # Toshkent
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. 5 ta mevadan iborat kortej yarating va uni chiqaring.
2. Kortejning birinchi va oxirgi elementini chiqaring.
3. Sonlar kortejining eng katta, eng kichik elementini va yig'indisini toping.
4. Kortejni teskari tartibda chiqaring.
5. Kortej elementlarini alohida o'zgaruvchilarga ochib bering (unpacking).
6. Ikki sonni qabul qilib, yig'indisi va ko'paytmasini kortej sifatida qaytaruvchi funksiya yozing.
7. Kortejni ro'yxatga aylantirib, bitta elementini o'zgartiring va yana kortejga qaytaring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- Kortej `( )` qavs bilan yoziladi, **tartiblangan** va **o'zgarmas**.
- Bitta elementli kortejda vergul shart: `(5,)`.
- Faqat `count()` va `index()` metodlari mavjud.
- Elementlarga indeks va kesim (slice) orqali murojaat qilinadi.
- Unpacking yordamida elementlarni o'zgaruvchilarga ajratish mumkin.
- O'zgarmas ma'lumotlar uchun `list` o'rniga `tuple` ishlatiladi.

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