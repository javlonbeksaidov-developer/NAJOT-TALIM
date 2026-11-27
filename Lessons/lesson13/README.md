<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2013%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da funksiyalar (2-qism)

Bu darsda funksiyalar mavzusi davom ettiriladi: **argument va parametr** turlari, **`return`** va **`*args`**, **`**kwargs`** bilan ishlash.

**Qisqa eslatma:**

```python
def salom(ism):          # ism — parametr
    return f"Salom, {ism}!"

print(salom("Ali"))      # "Ali" — argument
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📥 Argument va parametr

| Tushuncha | Tavsif | Qayerda yoziladi |
|-----------|--------|------------------|
| **Parametr** | Funksiya qabul qiladigan o'zgaruvchi | `def` qatorida |
| **Argument** | Funksiyaga beriladigan haqiqiy qiymat | Funksiya chaqirilganda |

## 1. Pozitsion argumentlar

Qiymatlar **tartib** bo'yicha mos parametrga tushadi.

```python
def tanishtir(ism, yosh):
    print(f"{ism}, {yosh} yosh")

tanishtir("Ali", 20)    # Ali, 20 yosh
tanishtir(20, "Ali")    # 20, Ali yosh  (tartib buzilsa, ma'no buziladi)
```

## 2. Nomli (keyword) argumentlar

Parametr nomi bilan beriladi, **tartib muhim emas**.

```python
tanishtir(yosh=20, ism="Ali")    # Ali, 20 yosh
```

> ⚠️ Pozitsion argument nomli argumentdan **oldin** yoziladi: `tanishtir("Ali", yosh=20)` to'g'ri, `tanishtir(ism="Ali", 20)` xato.

## 3. Standart (default) parametr

```python
def daraja(son, d=2):
    return son ** d

print(daraja(5))      # 25
print(daraja(2, 3))   # 8
```

> Standart qiymatli parametrlar **oxirida** yoziladi.

## 4. Faqat pozitsion va faqat nomli parametrlar

| Belgi | Ma'nosi | Misol |
|-------|---------|-------|
| `/` | O'ngacha bo'lganlar faqat pozitsion | `def f(a, b, /)` |
| `*` | Undan keyingilar faqat nomli | `def f(a, *, b)` |

```python
def f(a, *, b):
    return a + b

print(f(1, b=2))    # 3
print(f(1, 2))      # TypeError
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📤 `return` operatori

**Ta'rif:** natijani chaqirilgan joyga qaytaradi va funksiyani **darhol tugatadi**.

```python
def kvadrat(n):
    return n * n

x = kvadrat(4)
print(x)    # 16
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Funksiyani tugatadi | `return` dan keyingi kod bajarilmaydi |
| `return` yo'q bo'lsa | Funksiya `None` qaytaradi |
| Bo'sh `return` | `None` qaytaradi va funksiyani tugatadi |
| Bir nechta qiymat | Kortej sifatida qaytariladi |

**Bir nechta qiymat qaytarish:**

```python
def min_max(sonlar):
    return min(sonlar), max(sonlar)

kichik, katta = min_max([4, 9, 1, 7])
print(kichik, katta)    # 1 9
```

**Shart ichida `return`:**

```python
def tekshir(yosh):
    if yosh < 0:
        return "Noto'g'ri yosh"
    if yosh >= 18:
        return "Voyaga yetgan"
    return "Voyaga yetmagan"

print(tekshir(20))    # Voyaga yetgan
```

**`print` va `return` farqi:**

```python
def a(x):
    print(x * 2)

def b(x):
    return x * 2

print(a(3))    # 6, keyin None
print(b(3))    # 6
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✨ `*args`

**Ta'rif:** nomi oldindan noma'lum, **ixtiyoriy sondagi pozitsion** argumentlarni qabul qiladi. Qiymatlar **kortej (tuple)** ko'rinishida keladi.

```python
def jami(*args):
    print(args)
    return sum(args)

print(jami(1, 2, 3))
```

**Natija:**

```
(1, 2, 3)
6
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Belgi | Bitta yulduzcha `*` |
| Ichki tur | `tuple` (kortej) |
| Argument soni | 0 ta ham, ko'p ham bo'lishi mumkin |
| Nom | `args` odat, istalgan nom mumkin (`*sonlar`) |

**Oddiy parametr bilan birga:**

```python
def salomlash(salom, *ismlar):
    for ism in ismlar:
        print(f"{salom}, {ism}!")

salomlash("Assalomu alaykum", "Ali", "Vali", "Sardor")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧩 `**kwargs`

**Ta'rif:** ixtiyoriy sondagi **nomli** argumentlarni qabul qiladi. Qiymatlar **lug'at (dict)** ko'rinishida keladi.

```python
def profil(**kwargs):
    print(kwargs)

profil(ism="Ali", yosh=20, shahar="Toshkent")
```

**Natija:**

```
{'ism': 'Ali', 'yosh': 20, 'shahar': 'Toshkent'}
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Belgi | Ikkita yulduzcha `**` |
| Ichki tur | `dict` (lug'at) |
| Kalit | Argument nomi (`ism`, `yosh`) |
| Nom | `kwargs` odat, istalgan nom mumkin |

**Lug'at bilan ishlash:**

```python
def profil(**kwargs):
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

profil(ism="Ali", yosh=20)
```

**Natija:**

```
ism: Ali
yosh: 20
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔗 `*args` va `**kwargs` birga

```python
def royxat(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

royxat(1, 2, 3, ism="Ali", yosh=20)
```

**Natija:**

```
args: (1, 2, 3)
kwargs: {'ism': 'Ali', 'yosh': 20}
```

**Parametrlar tartibi (qat'iy):**

```python
def f(oddiy, standart=0, *args, **kwargs):
    pass
```

| Tartib | Parametr turi |
|--------|---------------|
| 1 | Oddiy parametrlar |
| 2 | Standart qiymatli parametrlar |
| 3 | `*args` |
| 4 | `**kwargs` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📦 Ochib berish (unpacking)

Funksiya **chaqirilganda** `*` va `**` yordamida ro'yxat va lug'atni argumentlarga ajratish mumkin.

```python
def yigindi(a, b, c):
    return a + b + c

sonlar = [1, 2, 3]
print(yigindi(*sonlar))      # 6

malumot = {"a": 10, "b": 20, "c": 30}
print(yigindi(**malumot))    # 60
```

| Belgi | Nimani ochadi | Natija |
|-------|---------------|--------|
| `*royxat` | Ro'yxat, kortej | Pozitsion argumentlar |
| `**lugat` | Lug'at | Nomli argumentlar |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Istalgan sondagi sonlarning o'rtachasi:**

```python
def ortacha(*sonlar):
    if not sonlar:
        return 0
    return sum(sonlar) / len(sonlar)

print(ortacha(5, 10, 15))    # 10.0
```

**Talaba ma'lumotlari:**

```python
def talaba(ism, **malumot):
    print(f"Talaba: {ism}")
    for kalit, qiymat in malumot.items():
        print(f"  {kalit}: {qiymat}")

talaba("Ali", yosh=20, kurs=2, guruh="PY-12")
```

**Natija:**

```
Talaba: Ali
  yosh: 20
  kurs: 2
  guruh: PY-12
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Ixtiyoriy sondagi sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing (`*args`).
2. Ikki sonning yig'indisi va ko'paytmasini bir vaqtda qaytaruvchi funksiya yozing.
3. Ismlarni `*args` orqali qabul qilib, har biriga salom beruvchi funksiya yozing.
4. `**kwargs` orqali mahsulot ma'lumotlarini (nom, narx, miqdor) qabul qilib chiqaruvchi funksiya yozing.
5. Standart qiymatli parametr bilan `salom(ism, til="uz")` funksiyasini yozing.
6. `*args` va `**kwargs` ni birga ishlatadigan funksiya yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Parametr** — `def` qatorida, **argument** — chaqirishda yoziladi.
- Argumentlar **pozitsion** yoki **nomli** bo'lishi mumkin.
- `return` natijani qaytaradi va funksiyani tugatadi, bir nechta qiymat **kortej** bo'ladi.
- `*args` — ixtiyoriy sondagi pozitsion argumentlar (**tuple**).
- `**kwargs` — ixtiyoriy sondagi nomli argumentlar (**dict**).
- Tartib: oddiy → standart → `*args` → `**kwargs`.

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