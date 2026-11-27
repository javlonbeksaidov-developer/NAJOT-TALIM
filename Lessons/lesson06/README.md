<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2006%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Shart operatorlari

**Shart operatori** — dastur qaysi kodni bajarishini shartga qarab tanlaydi. Shart `True` bo'lsa, tegishli kod bloki bajariladi.

Python'da uchta kalit so'z ishlatiladi:

- **`if`** — agar
- **`elif`** — aks holda, agar
- **`else`** — boshqa barcha holatda

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✅ `if` operatori

**Ta'rif:** shart `True` bo'lsagina blok bajariladi.

```python
yosh = 20

if yosh >= 18:
    print("Siz voyaga yetgansiz")
```

**Sintaksis:**

```python
if shart:
    bajariladigan_kod
```

**Qoidalar:**

| Qoida | Tavsif |
|-------|--------|
| Ikki nuqta | Shartdan keyin `:` qo'yiladi |
| Indent (tekislash) | Blok ichidagi kod **4 ta probel** bilan suriladi |
| Shart turi | Natija `bool` (`True` / `False`) bo'ladi |
| Qavs | Shartni qavsga olish shart emas |

> ⚠️ Indent noto'g'ri bo'lsa, `IndentationError` xatosi chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔀 `if-else` operatori

**Ta'rif:** shart `True` bo'lsa `if` bloki, aks holda `else` bloki bajariladi.

```python
yosh = 15

if yosh >= 18:
    print("Voyaga yetgan")
else:
    print("Voyaga yetmagan")
```

**Natija:**

```
Voyaga yetmagan
```

> `else` ga shart yozilmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 `if-elif-else` strukturasi

**Ta'rif:** bir nechta shartni ketma-ket tekshirish uchun ishlatiladi.

```python
ball = int(input("Ballni kiriting: "))

if ball >= 90:
    print("A'lo (5)")
elif ball >= 70:
    print("Yaxshi (4)")
elif ball >= 50:
    print("Qoniqarli (3)")
else:
    print("Qoniqarsiz (2)")
```

**Natija (`ball = 75` bo'lsa):**

```
Yaxshi (4)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Tekshirish tartibi | Yuqoridan pastga qarab |
| Bajariladigan blok | Faqat **birinchi** `True` bo'lgan blok |
| `elif` soni | Cheklanmagan |
| `else` | Ixtiyoriy, eng oxirida yoziladi |
| `if` | Doim birinchi bo'ladi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔗 Murakkab shartlar

Shartlarni `and`, `or`, `not` bilan birlashtirish mumkin.

```python
yosh = 25
guvohnoma = True

if yosh >= 18 and guvohnoma:
    print("Haydashga ruxsat bor")
else:
    print("Ruxsat yo'q")
```

| Operator | Vazifasi |
|----------|----------|
| `and` | Ikkala shart ham `True` bo'lishi kerak |
| `or` | Kamida bitta shart `True` bo'lishi kerak |
| `not` | Shartni teskarisiga o'zgartiradi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪆 Ichma-ich shart (nested if)

**Ta'rif:** shart ichida yana shart yoziladi.

```python
yosh = 20
pul = 5000

if yosh >= 18:
    if pul >= 3000:
        print("Chipta sotib oldingiz")
    else:
        print("Pul yetarli emas")
else:
    print("Yosh yetmaydi")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚡ Qisqa yozuv (ternary)

Bir qatorli `if-else`:

```python
yosh = 20
holat = "Voyaga yetgan" if yosh >= 18 else "Voyaga yetmagan"
print(holat)
```

**Sintaksis:**

```python
natija = qiymat1 if shart else qiymat2
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