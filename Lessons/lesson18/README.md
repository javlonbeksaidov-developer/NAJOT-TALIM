<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2018%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da xatolar bilan ishlash

Dastur ishlash vaqtida xato yuz bersa, u **to'xtab qoladi**. Xatolarni oldindan ushlab, dasturni to'xtatmasdan davom ettirish uchun **`try-except`** konstruksiyasi ishlatiladi.

```python
son = int(input("Son kiriting: "))    # "abc" kiritilsa, dastur to'xtaydi
print(son)
```

```
ValueError: invalid literal for int() with base 10: 'abc'
```

**Xato turlari:**

| Tur | Tavsif | Misol |
|-----|--------|-------|
| **Sintaksis xatosi** | Kod noto'g'ri yozilgan, dastur umuman ishga tushmaydi | `print("Salom"` |
| **Ishlash vaqti xatosi (exception)** | Dastur ishlayotganda yuz beradi | `10 / 0` |
| **Mantiqiy xato** | Dastur ishlaydi, lekin natija noto'g'ri | Yig'indi o'rniga ayirma yozish |

> `try-except` faqat **ishlash vaqti xatolarini** (exception) ushlaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 `try-except`

**Sintaksis:**

```python
try:
    xavfli_kod
except:
    xato_bo'lsa_bajariladigan_kod
```

**Misol:**

```python
try:
    son = int(input("Son kiriting: "))
    print("Siz kiritdingiz:", son)
except:
    print("Xato: faqat son kiriting!")
```

**Natija (`abc` kiritilsa):**

```
Son kiriting: abc
Xato: faqat son kiriting!
```

**Ishlash tartibi:**

| Holat | Nima bo'ladi |
|-------|--------------|
| Xato **bo'lmasa** | `try` bloki oxirigacha bajariladi, `except` o'tkazib yuboriladi |
| Xato **bo'lsa** | `try` darhol to'xtaydi va `except` bloki bajariladi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎯 Aniq xato turini ushlash

Barcha xatoni umumiy `except:` bilan ushlash tavsiya etilmaydi. **Aniq xato turi** ko'rsatilgani yaxshi.

```python
try:
    a = int(input("Birinchi son: "))
    b = int(input("Ikkinchi son: "))
    print(a / b)
except ValueError:
    print("Faqat son kiriting!")
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
```

**Eng ko'p uchraydigan xatolar:**

| Xato | Qachon yuz beradi | Misol |
|------|-------------------|-------|
| `ValueError` | Qiymat turi to'g'ri, lekin mazmuni noto'g'ri | `int("abc")` |
| `TypeError` | Amal noto'g'ri turga qo'llanilgan | `"5" + 3` |
| `ZeroDivisionError` | Nolga bo'lish | `10 / 0` |
| `IndexError` | Ro'yxatda mavjud bo'lmagan indeks | `[1, 2][5]` |
| `KeyError` | Lug'atda mavjud bo'lmagan kalit | `{"a": 1}["b"]` |
| `NameError` | E'lon qilinmagan o'zgaruvchi | `print(x)` |
| `FileNotFoundError` | Fayl topilmadi | `open("yoq.txt")` |
| `AttributeError` | Obyektda bunday atribut/metod yo'q | `"salom".qosh()` |

**Bir nechta xatoni birga ushlash:**

```python
try:
    son = int(input("Son: "))
    print(10 / son)
except (ValueError, ZeroDivisionError):
    print("Noto'g'ri qiymat kiritildi!")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 Xato xabarini olish: `as`

```python
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Xato yuz berdi:", e)
```

**Natija:**

```
Xato yuz berdi: division by zero
```

**Barcha xatoni `Exception` bilan ushlash:**

```python
try:
    x = int("abc")
except Exception as e:
    print("Xato turi:", type(e).__name__)
    print("Xabar:", e)
```

> `Exception` deyarli barcha xatolarning asosiy klassi. U orqali istalgan xatoni ushlash va uning xabarini ko'rish mumkin.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✅ `else`

**Ta'rif:** `try` blokida xato **bo'lmasa** bajariladi.

```python
try:
    son = int(input("Son kiriting: "))
except ValueError:
    print("Xato: faqat son kiriting!")
else:
    print(f"Siz {son} kiritdingiz")
```

| Kiritilgan | Natija |
|------------|--------|
| `25` | `Siz 25 kiritdingiz` |
| `abc` | `Xato: faqat son kiriting!` |

> `else` bloki doim `except` dan **keyin** yoziladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏁 `finally`

**Ta'rif:** xato bo'lsa ham, bo'lmasa ham **har doim** bajariladi. Odatda fayl yopish, ulanishni uzish kabi yakuniy ishlar uchun ishlatiladi.

```python
try:
    son = int(input("Son kiriting: "))
    print(10 / son)
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
except ValueError:
    print("Faqat son kiriting!")
finally:
    print("Dastur yakunlandi")
```

**Natija (`0` kiritilsa):**

```
Nolga bo'lib bo'lmaydi!
Dastur yakunlandi
```

**Fayl bilan ishlashda:**

```python
try:
    f = open("malumot.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi!")
finally:
    print("Tekshiruv tugadi")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧩 To'liq struktura

```python
try:
    # xavfli kod
except XatoTuri:
    # xato bo'lsa
else:
    # xato bo'lmasa
finally:
    # har doim
```

| Blok | Qachon bajariladi | Majburiymi |
|------|-------------------|------------|
| `try` | Doim, birinchi bo'lib | Ha |
| `except` | `try` ichida xato bo'lsa | Ha (`finally` bo'lmasa) |
| `else` | `try` ichida xato **bo'lmasa** | Yo'q |
| `finally` | **Har doim** | Yo'q |

**Misol:**

```python
try:
    a = int(input("Birinchi son: "))
    b = int(input("Ikkinchi son: "))
    natija = a / b
except ValueError:
    print("Faqat son kiriting!")
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
else:
    print("Natija:", natija)
finally:
    print("Dastur tugadi")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🚨 `raise`

**Ta'rif:** xatoni **o'zingiz** chaqirish uchun ishlatiladi.

```python
def yosh_tekshir(yosh):
    if yosh < 0:
        raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
    return yosh

try:
    yosh_tekshir(-5)
except ValueError as e:
    print("Xato:", e)
```

**Natija:**

```
Xato: Yosh manfiy bo'lishi mumkin emas!
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔁 Sikl bilan birga ishlatish

To'g'ri qiymat kiritilguncha qayta so'rash:

```python
while True:
    try:
        son = int(input("Butun son kiriting: "))
    except ValueError:
        print("Noto'g'ri! Qaytadan urinib ko'ring.")
    else:
        print("To'g'ri:", son)
        break
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Xavfsiz bo'lish funksiyasi:**

```python
def bol(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Nolga bo'lib bo'lmaydi"

print(bol(10, 2))    # 5.0
print(bol(10, 0))    # Nolga bo'lib bo'lmaydi
```

**Ro'yxat elementiga xavfsiz murojaat:**

```python
mevalar = ["olma", "anor", "uzum"]

try:
    indeks = int(input("Indeks: "))
    print(mevalar[indeks])
except ValueError:
    print("Indeks son bo'lishi kerak!")
except IndexError:
    print("Bunday indeks mavjud emas!")
```

**Lug'atdan xavfsiz qiymat olish:**

```python
talaba = {"ism": "Ali", "yosh": 20}

try:
    print(talaba["manzil"])
except KeyError:
    print("Bunday kalit mavjud emas!")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Foydalanuvchidan son so'rang. Son kiritilmasa, xato xabarini chiqaring (`ValueError`).
2. Ikki sonni bo'ling va nolga bo'lish xatosini (`ZeroDivisionError`) ushlang.
3. Ro'yxat indeksini so'rang va `IndexError` ni ushlang.
4. Lug'atdan kalit bo'yicha qiymat oling va `KeyError` ni ushlang.
5. `else` va `finally` bloklarini ishlatadigan dastur yozing.
6. To'g'ri son kiritilguncha qayta so'raydigan sikl yozing.
7. `raise` yordamida yoshi manfiy bo'lsa xato chiqaruvchi funksiya yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- `try` ichiga xavfli kod yoziladi, xato bo'lsa `except` bajariladi.
- Umumiy `except:` o'rniga **aniq xato turini** ko'rsatish yaxshi.
- `as e` orqali xato xabarini olish mumkin.
- `else` xato **bo'lmasa**, `finally` esa **har doim** bajariladi.
- `raise` bilan xatoni o'zingiz chaqirishingiz mumkin.

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