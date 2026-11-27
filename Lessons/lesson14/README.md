<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2014%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da lug'atlar (`dict`)

**Lug'at (dictionary)** — ma'lumotlarni **kalit : qiymat** juftliklari ko'rinishida saqlaydigan ma'lumot turi. Elementlarga indeks bilan emas, **kalit** orqali murojaat qilinadi.

```python
talaba = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 2
}

print(talaba["ism"])    # Ali
print(type(talaba))     # <class 'dict'>
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Qavs | Figurali qavs `{ }` |
| Tuzilishi | `kalit: qiymat` juftliklari |
| Kalit | **Noyob** bo'lishi kerak, o'zgarmas turda bo'ladi (`str`, `int`, `tuple`) |
| Qiymat | Istalgan turda bo'lishi mumkin, takrorlanishi mumkin |
| O'zgaruvchan | Element qo'shish, o'zgartirish, o'chirish mumkin (mutable) |
| Tartib | Elementlar **qo'shilgan tartibda** saqlanadi (Python 3.7+) |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ Lug'at yaratish

```python
# 1. Figurali qavs bilan
a = {"ism": "Ali", "yosh": 20}

# 2. dict() funksiyasi bilan
b = dict(ism="Ali", yosh=20)

# 3. Kalit-qiymat juftliklari ro'yxatidan
c = dict([("ism", "Ali"), ("yosh", 20)])

# 4. Bo'sh lug'at
d = {}
e = dict()
```

> ⚠️ `{}` bo'sh **lug'at** yaratadi, bo'sh to'plam (`set`) emas.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 Qiymatga murojaat qilish

## Kalit orqali `[ ]`

```python
talaba = {"ism": "Ali", "yosh": 20}

print(talaba["ism"])      # Ali
print(talaba["manzil"])   # KeyError: kalit mavjud emas
```

## `get()` metodi

Kalit topilmasa xato bermaydi, `None` yoki berilgan qiymatni qaytaradi.

```python
print(talaba.get("ism"))              # Ali
print(talaba.get("manzil"))           # None
print(talaba.get("manzil", "Yo'q"))   # Yo'q
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✏️ Element qo'shish va o'zgartirish

```python
talaba = {"ism": "Ali", "yosh": 20}

talaba["kurs"] = 2          # yangi kalit qo'shish
talaba["yosh"] = 21         # mavjud qiymatni o'zgartirish

print(talaba)
# {'ism': 'Ali', 'yosh': 21, 'kurs': 2}
```

## `update()` metodi

Bir nechta juftlikni birdan qo'shadi yoki yangilaydi.

```python
talaba.update({"shahar": "Toshkent", "yosh": 22})
print(talaba)
# {'ism': 'Ali', 'yosh': 22, 'kurs': 2, 'shahar': 'Toshkent'}
```

## `setdefault()` metodi

Kalit **yo'q bo'lsa** qo'shadi, bor bo'lsa o'zgartirmaydi.

```python
talaba.setdefault("guruh", "PY-12")   # qo'shiladi
talaba.setdefault("ism", "Vali")      # o'zgarmaydi
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗑️ Element o'chirish

| Usul | Vazifasi |
|------|----------|
| `del lugat[kalit]` | Kalit bo'yicha o'chiradi |
| `pop(kalit)` | O'chiradi va qiymatini qaytaradi |
| `popitem()` | Oxirgi qo'shilgan juftlikni o'chiradi va qaytaradi |
| `clear()` | Lug'atni butunlay bo'shatadi |

```python
talaba = {"ism": "Ali", "yosh": 20, "kurs": 2, "guruh": "PY-12"}

del talaba["kurs"]
qiymat = talaba.pop("yosh")      # 20
oxirgi = talaba.popitem()        # ('guruh', 'PY-12')
talaba.clear()                   # {}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔑 Asosiy metodlar

| Metod | Vazifasi |
|-------|----------|
| `keys()` | Barcha kalitlarni qaytaradi |
| `values()` | Barcha qiymatlarni qaytaradi |
| `items()` | `(kalit, qiymat)` juftliklarini qaytaradi |
| `get(k, d)` | Kalit bo'yicha qiymat, topilmasa `d` |
| `update(d)` | Lug'atni yangilaydi |
| `pop(k)` | Kalitni o'chirib, qiymatini qaytaradi |
| `copy()` | Lug'at nusxasini yaratadi |
| `clear()` | Barcha elementlarni o'chiradi |

```python
talaba = {"ism": "Ali", "yosh": 20, "kurs": 2}

print(talaba.keys())     # dict_keys(['ism', 'yosh', 'kurs'])
print(talaba.values())   # dict_values(['Ali', 20, 2])
print(talaba.items())    # dict_items([('ism', 'Ali'), ('yosh', 20), ('kurs', 2)])
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 Lug'at ustida sikl

```python
talaba = {"ism": "Ali", "yosh": 20, "kurs": 2}

# Kalitlar bo'yicha
for kalit in talaba:
    print(kalit)

# Qiymatlar bo'yicha
for qiymat in talaba.values():
    print(qiymat)

# Kalit va qiymat birga
for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")
```

**Natija (oxirgi sikl):**

```
ism: Ali
yosh: 20
kurs: 2
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ❓ Kalit mavjudligini tekshirish

`in` operatori **kalitlar** orasidan qidiradi.

```python
talaba = {"ism": "Ali", "yosh": 20}

print("ism" in talaba)        # True
print("Ali" in talaba)        # False (Ali — qiymat, kalit emas)
print("Ali" in talaba.values())  # True
print("kurs" not in talaba)   # True
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪆 Ichma-ich lug'at

Lug'at qiymati sifatida boshqa lug'at ham bo'lishi mumkin.

```python
talabalar = {
    "t1": {"ism": "Ali", "yosh": 20},
    "t2": {"ism": "Vali", "yosh": 22}
}

print(talabalar["t1"]["ism"])    # Ali

talabalar["t2"]["yosh"] = 23
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📋 Nusxalash

```python
a = {"x": 1, "y": 2}

b = a            # nusxa emas, bitta lug'atga ikkita nom
c = a.copy()     # haqiqiy nusxa

a["x"] = 100
print(b["x"])    # 100 (a bilan birga o'zgardi)
print(c["x"])    # 1   (o'zgarmadi)
```

> ⚠️ `b = a` yangi lug'at yaratmaydi. Mustaqil nusxa uchun `copy()` ishlatiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚡ Dict comprehension

Lug'atni bitta qatorda yaratish usuli.

```python
kvadratlar = {i: i ** 2 for i in range(1, 6)}
print(kvadratlar)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Harflar sonini sanash:**

```python
matn = "salom"
sanoq = {}

for harf in matn:
    sanoq[harf] = sanoq.get(harf, 0) + 1

print(sanoq)
# {'s': 1, 'a': 1, 'l': 1, 'o': 1, 'm': 1}
```

**Ikkita ro'yxatdan lug'at yaratish:**

```python
kalitlar = ["ism", "yosh", "shahar"]
qiymatlar = ["Ali", 20, "Toshkent"]

lugat = dict(zip(kalitlar, qiymatlar))
print(lugat)
# {'ism': 'Ali', 'yosh': 20, 'shahar': 'Toshkent'}
```

**Mahsulotlar narxi:**

```python
narxlar = {"non": 4000, "sut": 12000, "tuxum": 15000}

for nom, narx in narxlar.items():
    print(f"{nom}: {narx} so'm")

print("Jami:", sum(narxlar.values()), "so'm")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. O'zingiz haqingizda (ism, yosh, shahar) lug'at yarating va chiqaring.
2. Lug'atga yangi kalit qo'shing, mavjud qiymatni o'zgartiring.
3. Lug'at kalitlari va qiymatlarini alohida sikl bilan chiqaring.
4. Foydalanuvchidan so'z kiriting va uning har bir harfi necha marta kelganini sanang.
5. 5 ta mahsulot narxlari lug'atini yarating va eng qimmat mahsulotni toping.
6. Foydalanuvchi kiritgan kalit lug'atda bor-yo'qligini tekshiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- Lug'at `{kalit: qiymat}` shaklida ma'lumot saqlaydi.
- Kalit **noyob** va **o'zgarmas** turda bo'lishi kerak.
- Qiymatga `lugat[kalit]` yoki xavfsiz `get()` orqali murojaat qilinadi.
- `keys()`, `values()`, `items()` metodlari sikl uchun qulay.
- Nusxa olish uchun `copy()` ishlatiladi.

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