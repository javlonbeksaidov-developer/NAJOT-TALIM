<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2005%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Boolean ma'lumot turi

**Boolean (`bool`)** — mantiqiy qiymat turi. U faqat ikki qiymatdan birini oladi:

- **`True`** — rost (ha)
- **`False`** — yolg'on (yo'q)

```python
faol = True
tugagan = False

print(faol)           # True
print(type(faol))     # <class 'bool'>
```

> ⚠️ `True` va `False` **bosh harf bilan** yoziladi. `true` yoki `false` xato beradi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚖️ Taqqoslash operatorlari

Taqqoslash natijasi doim `bool` bo'ladi.

| Operator | Ma'nosi | Misol | Natija |
|----------|---------|-------|--------|
| `==` | Teng | `5 == 5` | `True` |
| `!=` | Teng emas | `5 != 3` | `True` |
| `>` | Katta | `7 > 10` | `False` |
| `<` | Kichik | `3 < 8` | `True` |
| `>=` | Katta yoki teng | `5 >= 5` | `True` |
| `<=` | Kichik yoki teng | `4 <= 2` | `False` |

```python
yosh = 20
print(yosh >= 18)   # True
print(yosh == 25)   # False
```

> `=` qiymat **beradi**, `==` esa qiymatlarni **taqqoslaydi**.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔗 Mantiqiy operatorlar

| Operator | Ma'nosi | Qoidasi |
|----------|---------|---------|
| `and` | VA | Ikkalasi ham `True` bo'lsa, `True` |
| `or` | YOKI | Kamida bittasi `True` bo'lsa, `True` |
| `not` | EMAS | Qiymatni teskarisiga o'zgartiradi |

```python
a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False
```

**Rostlik jadvali:**

| A | B | `A and B` | `A or B` |
|---|---|-----------|----------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 `bool()` funksiyasi

Istalgan qiymatni mantiqiy turga o'tkazadi.

**`False` deb hisoblanadigan qiymatlar:**

| Qiymat | Tavsif |
|--------|--------|
| `0` | Nol (int) |
| `0.0` | Nol (float) |
| `""` | Bo'sh satr |
| `None` | Qiymat yo'q |
| `[]`, `()`, `{}` | Bo'sh ro'yxat, kortej, lug'at |

Qolgan barcha qiymatlar `True` hisoblanadi.

```python
print(bool(0))        # False
print(bool(""))       # False
print(bool(5))        # True
print(bool("Salom"))  # True
print(bool(-1))       # True
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧮 Xususiyatlari

| Xususiyat | Tavsif |
|-----------|--------|
| Qiymatlari | Faqat `True` va `False` |
| Tur | `bool` (`int` turining qismi) |
| Raqamli qiymati | `True == 1`, `False == 0` |
| Yozilishi | Bosh harf bilan: `True`, `False` |
| Qayerda ishlatiladi | Shartlar (`if`), sikllar (`while`) |

```python
print(True + True)    # 2
print(False + 5)      # 5
print(int(True))      # 1
```

**Amaliy misol:**

```python
yosh = int(input("Yoshingiz: "))
print("Voyaga yetgan:", yosh >= 18)
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