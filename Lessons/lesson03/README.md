<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2003%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Kiritish va chiqarish operatorlari

Python'da dastur foydalanuvchi bilan ikki funksiya orqali muloqot qiladi:

- **`print()`** — ma'lumotni ekranga **chiqaradi**
- **`input()`** — foydalanuvchidan ma'lumot **qabul qiladi**

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🖨️ `print()`

**Ta'rif:** qavs ichidagi qiymatni ekranga chiqaradi.

```python
print("Salom, Dunyo!")
print("Ism:", "Ali", "Yosh:", 20)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Bir nechta qiymat | Vergul bilan ajratiladi, orasiga avtomatik probel qo'yiladi |
| `sep` | Qiymatlar orasidagi ajratgich (standart: probel) |
| `end` | Oxirgi belgi (standart: `\n`, ya'ni yangi qator) |
| Qaytaradigan qiymat | `None` |
| `\n`, `\t` | Yangi qator va tab belgilari |

```python
print("2026", "11", "27", sep="-")   # 2026-11-27
print("Salom", end=" ")
print("Dunyo")                        # Salom Dunyo
```

**O'zgaruvchini chiqarish (f-string):**

```python
ism = "Ali"
print(f"Salom, {ism}!")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⌨️ `input()`

**Ta'rif:** foydalanuvchi klaviaturadan kiritgan ma'lumotni o'qiydi.

```python
ism = input("Ismingizni kiriting: ")
print("Salom,", ism)
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Qaytaradigan tur | **Har doim `str`** (raqam kiritilsa ham) |
| Xabar (prompt) | Qavs ichida yoziladi, foydalanuvchiga ko'rsatiladi |
| Dastur to'xtaydi | Foydalanuvchi `Enter` bosguncha kutadi |

**Muhim qoida:** raqam kerak bo'lsa, turini o'zgartirish kerak.

```python
yosh = int(input("Yoshingiz: "))      # butun son
boy = float(input("Bo'yingiz: "))    # kasr son
```

| Funksiya | Vazifasi |
|----------|----------|
| `int()` | Butun songa o'tkazadi |
| `float()` | Kasr songa o'tkazadi |
| `str()` | Matnga o'tkazadi |

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