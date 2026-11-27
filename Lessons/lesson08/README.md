<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2008%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python `for` operatori

**Sikl (loop)** — bir xil kodni bir necha marta takrorlash uchun ishlatiladi.

**`for`** sikli ketma-ketlikdagi (masalan, `range()`, satr, ro'yxat) har bir element ustida birma-bir yuradi.

**Sintaksis:**

```python
for i in range(n):
    bajariladigan_kod
```

```python
for i in range(5):
    print("Salom")
```

**Natija:**

```
Salom
Salom
Salom
Salom
Salom
```

**Qoidalar:**

| Qoida | Tavsif |
|-------|--------|
| Ikki nuqta | `for` qatoridan keyin `:` qo'yiladi |
| Indent | Sikl ichidagi kod **4 ta probel** bilan suriladi |
| `i` | Sikl o'zgaruvchisi, har aylanishda yangi qiymat oladi |
| Takrorlanish | Sikl tanasi har bir element uchun bir marta bajariladi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 `range()` funksiyasi

**Ta'rif:** sonlar ketma-ketligini hosil qiladi.

| Shakl | Ma'nosi | Misol | Hosil bo'ladigan sonlar |
|-------|---------|-------|-------------------------|
| `range(n)` | `0` dan `n-1` gacha | `range(5)` | `0, 1, 2, 3, 4` |
| `range(a, b)` | `a` dan `b-1` gacha | `range(2, 6)` | `2, 3, 4, 5` |
| `range(a, b, step)` | `step` qadam bilan | `range(1, 10, 2)` | `1, 3, 5, 7, 9` |

> ⚠️ `range` da oxirgi son **kiritilmaydi**: `range(5)` da `5` yo'q.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 1️⃣ `range(n)`

`0` dan boshlab `n-1` gacha:

```python
for i in range(5):
    print(i)
```

**Natija:**

```
0
1
2
3
4
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 2️⃣ `range(a, b)`

`a` dan boshlab `b-1` gacha:

```python
for i in range(1, 6):
    print(i)
```

**Natija:**

```
1
2
3
4
5
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 3️⃣ `range(a, b, step)`

Berilgan qadam bilan:

```python
for i in range(0, 11, 2):
    print(i, end=" ")
```

**Natija:**

```
0 2 4 6 8 10
```

**Teskari sanash (manfiy qadam):**

```python
for i in range(5, 0, -1):
    print(i, end=" ")
```

**Natija:**

```
5 4 3 2 1
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔤 Satr ustida sikl

```python
for harf in "Python":
    print(harf)
```

**Natija:**

```
P
y
t
h
o
n
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⏹️ `break` va `continue`

| Operator | Vazifasi |
|----------|----------|
| `break` | Siklni butunlay to'xtatadi |
| `continue` | Joriy aylanishni o'tkazib, keyingisiga o'tadi |

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

**Natija:** `1 2`

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Natija:** `1 2 4 5`

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**1 dan 10 gacha sonlar yig'indisi:**

```python
yigindi = 0
for i in range(1, 11):
    yigindi += i
print("Yig'indi:", yigindi)
```

**Natija:**

```
Yig'indi: 55
```

**Ko'paytirish jadvali:**

```python
n = int(input("Son kiriting: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
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