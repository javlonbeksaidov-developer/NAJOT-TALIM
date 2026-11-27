<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2019%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da fayllar bilan ishlash

Dastur ishlashi tugagach, o'zgaruvchilardagi ma'lumotlar yo'qoladi. Ma'lumotni **doimiy saqlash** uchun u faylga yoziladi va kerak bo'lganda fayldan o'qiladi.

Bu darsda ikki turdagi fayl bilan ishlaymiz:

| Format | Tavsif | Qachon ishlatiladi |
|--------|--------|--------------------|
| **`.txt`** | Oddiy matn fayli | Oddiy matn, log, qisqa yozuvlar |
| **`.json`** | Tuzilgan ma'lumot (lug'at, ro'yxat) | Sozlamalar, ma'lumotlar bazasi o'rnida, API |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📂 Faylni ochish: `open()`

**Sintaksis:**

```python
open("fayl_nomi", "rejim", encoding="utf-8")
```

**Rejimlar:**

| Rejim | Ma'nosi | Fayl mavjud bo'lmasa | Eski ma'lumot |
|-------|---------|----------------------|---------------|
| `"r"` | O'qish (read), standart | `FileNotFoundError` | Saqlanadi |
| `"w"` | Yozish (write) | Yangi fayl yaratadi | **O'chiriladi** |
| `"a"` | Oxiriga qo'shish (append) | Yangi fayl yaratadi | Saqlanadi |
| `"x"` | Yangi fayl yaratish | Fayl bor bo'lsa xato | – |
| `"r+"` | O'qish va yozish | `FileNotFoundError` | Saqlanadi |

> ⚠️ `"w"` rejimi fayl ichidagi **barcha eski ma'lumotni o'chirib yuboradi**. Ehtiyot bo'ling!

> 💡 O'zbekcha harflar (`o'`, `g'`, `sh`) to'g'ri saqlanishi uchun doim `encoding="utf-8"` yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔒 `with` operatori

**Ta'rif:** faylni ochadi va ish tugagach **avtomatik yopadi**. Xato bo'lsa ham fayl yopiladi.

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Salom, Python!")
```

**`with`siz usul (tavsiya etilmaydi):**

```python
f = open("test.txt", "w", encoding="utf-8")
f.write("Salom, Python!")
f.close()    # yopishni unutmaslik kerak
```

> Doim `with` ishlatish tavsiya etiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ `.txt` faylga yozish

## `write()`

Faylga matn yozadi. Yangi qatorga o'tish uchun `\n` qo'yiladi.

```python
with open("ismlar.txt", "w", encoding="utf-8") as f:
    f.write("Ali\n")
    f.write("Vali\n")
    f.write("Sardor\n")
```

**`ismlar.txt` ichida:**

```
Ali
Vali
Sardor
```

## `writelines()`

Ro'yxatdagi qatorlarni yozadi. `\n` ni o'zingiz qo'shishingiz kerak.

```python
qatorlar = ["Olma\n", "Anor\n", "Uzum\n"]

with open("mevalar.txt", "w", encoding="utf-8") as f:
    f.writelines(qatorlar)
```

## Oxiriga qo'shish: `"a"`

```python
with open("ismlar.txt", "a", encoding="utf-8") as f:
    f.write("Aziz\n")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📖 `.txt` fayldan o'qish

| Metod | Vazifasi | Qaytaradi |
|-------|----------|-----------|
| `read()` | Butun faylni o'qiydi | `str` |
| `readline()` | Bitta qatorni o'qiydi | `str` |
| `readlines()` | Barcha qatorlarni o'qiydi | `list` |

```python
# 1. Butun faylni
with open("ismlar.txt", "r", encoding="utf-8") as f:
    matn = f.read()
    print(matn)
```

```python
# 2. Bitta qator
with open("ismlar.txt", "r", encoding="utf-8") as f:
    print(f.readline())    # Ali
    print(f.readline())    # Vali
```

```python
# 3. Qatorlar ro'yxati
with open("ismlar.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()
    print(qatorlar)    # ['Ali\n', 'Vali\n', 'Sardor\n']
```

## Qatorma-qator sikl bilan (eng qulay usul)

```python
with open("ismlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.strip())    # strip() — \n ni olib tashlaydi
```

> Katta fayllar uchun bu usul xotirani tejaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧩 JSON nima?

**JSON** (JavaScript Object Notation) — ma'lumotni matn ko'rinishida saqlash formati. Ko'rinishi Python lug'ati va ro'yxatiga juda o'xshash.

```json
{
    "ism": "Ali",
    "yosh": 20,
    "talaba": true,
    "fanlar": ["Python", "Matematika"]
}
```

**Python va JSON turlari mosligi:**

| Python | JSON |
|--------|------|
| `dict` | `object { }` |
| `list`, `tuple` | `array [ ]` |
| `str` | `string` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

> ⚠️ JSON'da matn faqat **ikkita tirnoq** `" "` bilan yoziladi.

JSON bilan ishlash uchun standart `json` moduli import qilinadi:

```python
import json
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💾 `.json` faylga yozish: `json.dump()`

```python
import json

talaba = {
    "ism": "Ali",
    "yosh": 20,
    "fanlar": ["Python", "Matematika"],
    "talaba": True
}

with open("talaba.json", "w", encoding="utf-8") as f:
    json.dump(talaba, f, ensure_ascii=False, indent=4)
```

**Parametrlari:**

| Parametr | Vazifasi |
|----------|----------|
| `ensure_ascii=False` | O'zbekcha va boshqa harflarni to'g'ri saqlaydi |
| `indent=4` | Faylni chiroyli, o'qiladigan ko'rinishda yozadi |

**`talaba.json` ichida:**

```json
{
    "ism": "Ali",
    "yosh": 20,
    "fanlar": [
        "Python",
        "Matematika"
    ],
    "talaba": true
}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📥 `.json` fayldan o'qish: `json.load()`

```python
import json

with open("talaba.json", "r", encoding="utf-8") as f:
    malumot = json.load(f)

print(malumot)             # {'ism': 'Ali', 'yosh': 20, ...}
print(type(malumot))       # <class 'dict'>
print(malumot["ism"])      # Ali
print(malumot["fanlar"])   # ['Python', 'Matematika']
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 `dump/load` va `dumps/loads` farqi

| Funksiya | Nima bilan ishlaydi | Vazifasi |
|----------|---------------------|----------|
| `json.dump(obj, f)` | **Fayl** | Python obyektini faylga yozadi |
| `json.load(f)` | **Fayl** | Fayldan o'qib, Python obyektiga aylantiradi |
| `json.dumps(obj)` | **Matn (str)** | Python obyektini JSON matniga aylantiradi |
| `json.loads(matn)` | **Matn (str)** | JSON matnini Python obyektiga aylantiradi |

> Qo'shimcha `s` harfi **string** (matn) degani.

```python
import json

lugat = {"ism": "Ali", "yosh": 20}

matn = json.dumps(lugat)
print(matn)              # {"ism": "Ali", "yosh": 20}
print(type(matn))        # <class 'str'>

yana_lugat = json.loads(matn)
print(yana_lugat)        # {'ism': 'Ali', 'yosh': 20}
print(type(yana_lugat))  # <class 'dict'>
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ JSON faylga ma'lumot qo'shish

JSON'da "oxiriga qo'shish" rejimi to'g'ri ishlamaydi. To'g'ri usul: **o'qish → o'zgartirish → qayta yozish**.

```python
import json

# 1. O'qish
with open("talabalar.json", "r", encoding="utf-8") as f:
    talabalar = json.load(f)

# 2. O'zgartirish
talabalar.append({"ism": "Vali", "yosh": 22})

# 3. Qayta yozish
with open("talabalar.json", "w", encoding="utf-8") as f:
    json.dump(talabalar, f, ensure_ascii=False, indent=4)
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Xatolarni ushlash

Fayl bilan ishlashda eng ko'p uchraydigan xatolar:

| Xato | Sababi |
|------|--------|
| `FileNotFoundError` | Fayl mavjud emas |
| `PermissionError` | Faylga kirish huquqi yo'q |
| `json.JSONDecodeError` | JSON fayl noto'g'ri tuzilgan yoki bo'sh |

```python
import json

try:
    with open("malumot.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(data)
except FileNotFoundError:
    print("Fayl topilmadi!")
except json.JSONDecodeError:
    print("JSON fayl noto'g'ri yozilgan!")
```

**Fayl mavjudligini tekshirish:**

```python
import os

if os.path.exists("ismlar.txt"):
    print("Fayl bor")
else:
    print("Fayl yo'q")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Eslatmalar daftari (`.txt`):**

```python
eslatma = input("Eslatma yozing: ")

with open("eslatmalar.txt", "a", encoding="utf-8") as f:
    f.write(eslatma + "\n")

print("Saqlandi!")
```

**Qatorlar sonini sanash:**

```python
with open("ismlar.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()

print("Qatorlar soni:", len(qatorlar))
```

**Kontaktlar (`.json`):**

```python
import json

kontaktlar = {
    "Ali": "+998901234567",
    "Vali": "+998931112233"
}

with open("kontaktlar.json", "w", encoding="utf-8") as f:
    json.dump(kontaktlar, f, ensure_ascii=False, indent=4)

with open("kontaktlar.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for ism, raqam in data.items():
    print(f"{ism}: {raqam}")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `.txt` faylga o'zingiz haqingizda 3 qator ma'lumot yozing.
2. Shu faylni o'qib, ekranga chiqaring.
3. Faylga `"a"` rejimi bilan yangi qator qo'shing.
4. `.txt` fayldagi qatorlar sonini hisoblang.
5. Foydalanuvchidan ism va yosh so'rab, `.json` faylga lug'at sifatida yozing.
6. `.json` faylni o'qib, ma'lumotlarini chiroyli ko'rinishda chiqaring.
7. `.json` fayldagi ro'yxatga yangi element qo'shing.
8. Fayl topilmasa, xato xabarini chiqaradigan dastur yozing (`try-except`).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- Fayl `open()` bilan ochiladi, `with` esa uni avtomatik yopadi.
- Rejimlar: `"r"` o'qish, `"w"` yozish (eski ma'lumot o'chadi), `"a"` oxiriga qo'shish.
- `.txt` uchun: `write()`, `writelines()`, `read()`, `readline()`, `readlines()`.
- `.json` uchun: `json.dump()` yozadi, `json.load()` o'qiydi.
- O'zbekcha harflar uchun `encoding="utf-8"` va `ensure_ascii=False` yoziladi.
- JSON'ga qo'shish uchun: **o'qish → o'zgartirish → qayta yozish**.

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