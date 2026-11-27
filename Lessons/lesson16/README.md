<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2016%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da to'plamlar (`set`)

**To'plam (set)** — **tartiblanmagan** va **takrorlanmaydigan** (noyob) elementlar to'plami. Elementlarga indeks orqali murojaat qilib bo'lmaydi.

```python
mevalar = {"olma", "anor", "uzum"}

print(mevalar)          # {'anor', 'olma', 'uzum'} (tartib har xil bo'lishi mumkin)
print(type(mevalar))    # <class 'set'>
```

**Xususiyatlari:**

| Xususiyat | Tavsif |
|-----------|--------|
| Qavs | Figurali qavs `{ }` |
| Tartibsiz | Elementlar tartibi kafolatlanmaydi, indeks yo'q |
| Noyob elementlar | Takrorlangan qiymatlar avtomatik o'chiriladi |
| Elementlari o'zgarmas | Ichida `int`, `str`, `tuple` bo'ladi. `list` va `dict` bo'lmaydi |
| To'plamning o'zi | O'zgaruvchan: element qo'shish va o'chirish mumkin |
| Tezlik | Elementni qidirish (`in`) juda tez |

> ⚠️ **Eslatma:** to'plam elementlari o'zgarmas turda bo'lishi kerak, lekin to'plamning o'zi o'zgaradi. Butunlay o'zgarmas to'plam kerak bo'lsa, `frozenset` ishlatiladi.

```python
sonlar = {1, 2, 2, 3, 3, 3}
print(sonlar)    # {1, 2, 3}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ To'plam yaratish

```python
# 1. Figurali qavs bilan
a = {1, 2, 3}

# 2. set() funksiyasi bilan
b = set([1, 2, 2, 3])      # {1, 2, 3}
c = set("salom")           # {'s', 'a', 'l', 'o', 'm'}
d = set(range(5))          # {0, 1, 2, 3, 4}

# 3. Bo'sh to'plam
e = set()
```

> ⚠️ `{}` bo'sh **lug'at** yaratadi. Bo'sh to'plam faqat `set()` bilan yaratiladi.

```python
x = {}
y = set()
print(type(x))    # <class 'dict'>
print(type(y))    # <class 'set'>
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 Elementlarga murojaat

To'plamda indeks yo'q, shuning uchun `s[0]` xato beradi.

```python
s = {10, 20, 30}
print(s[0])    # TypeError: 'set' object is not subscriptable
```

**Sikl orqali:**

```python
for element in s:
    print(element)
```

**Mavjudligini tekshirish:**

```python
print(20 in s)        # True
print(50 not in s)    # True
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ Element qo'shish

| Metod | Vazifasi |
|-------|----------|
| `add(x)` | Bitta element qo'shadi |
| `update(iterable)` | Bir nechta element qo'shadi |

```python
s = {1, 2}

s.add(3)
s.add(2)                 # allaqachon bor, o'zgarmaydi
s.update([4, 5, 6])

print(s)    # {1, 2, 3, 4, 5, 6}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗑️ Element o'chirish

| Metod | Vazifasi | Element yo'q bo'lsa |
|-------|----------|---------------------|
| `remove(x)` | `x` ni o'chiradi | `KeyError` xatosi |
| `discard(x)` | `x` ni o'chiradi | Xato bermaydi |
| `pop()` | Tasodifiy elementni o'chirib, qaytaradi | Bo'sh to'plamda xato |
| `clear()` | Hamma elementni o'chiradi | Xato bermaydi |

```python
s = {1, 2, 3, 4, 5}

s.remove(1)
s.discard(10)       # xato bermaydi
x = s.pop()         # tasodifiy element
s.clear()           # set()
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔗 To'plamlar ustida amallar

Matematikadagi to'plamlar nazariyasi amallari qo'llab-quvvatlanadi.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

| Amal | Operator | Metod | Natija |
|------|----------|-------|--------|
| Birlashma | `a \| b` | `a.union(b)` | `{1, 2, 3, 4, 5, 6}` |
| Kesishma | `a & b` | `a.intersection(b)` | `{3, 4}` |
| Ayirma | `a - b` | `a.difference(b)` | `{1, 2}` |
| Simmetrik ayirma | `a ^ b` | `a.symmetric_difference(b)` | `{1, 2, 5, 6}` |

```python
print(a | b)    # {1, 2, 3, 4, 5, 6}
print(a & b)    # {3, 4}
print(a - b)    # {1, 2}
print(a ^ b)    # {1, 2, 5, 6}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✅ To'plamlarni taqqoslash

| Metod | Vazifasi |
|-------|----------|
| `issubset(b)` | `a` to'plam `b` ning qism to'plami ekanini tekshiradi |
| `issuperset(b)` | `a` to'plam `b` ni o'z ichiga olishini tekshiradi |
| `isdisjoint(b)` | Umumiy element yo'qligini tekshiradi |

```python
a = {1, 2}
b = {1, 2, 3, 4}
c = {7, 8}

print(a.issubset(b))      # True
print(b.issuperset(a))    # True
print(a.isdisjoint(c))    # True
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔑 Asosiy metodlar va funksiyalar

| Metod / Funksiya | Vazifasi |
|------------------|----------|
| `add(x)` | Element qo'shadi |
| `update(it)` | Bir nechta element qo'shadi |
| `remove(x)` | Elementni o'chiradi (yo'q bo'lsa xato) |
| `discard(x)` | Elementni o'chiradi (yo'q bo'lsa xato yo'q) |
| `pop()` | Tasodifiy elementni o'chiradi |
| `clear()` | To'plamni bo'shatadi |
| `copy()` | To'plam nusxasini yaratadi |
| `len(s)` | Elementlar soni |
| `min(s)`, `max(s)`, `sum(s)` | Eng kichik, eng katta, yig'indi |
| `sorted(s)` | Tartiblangan **ro'yxat** qaytaradi |

```python
s = {5, 2, 8, 1}

print(len(s))       # 4
print(sorted(s))    # [1, 2, 5, 8]
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧊 `frozenset` (o'zgarmas to'plam)

**Ta'rif:** yaratilgandan keyin o'zgartirib bo'lmaydigan to'plam.

```python
f = frozenset([1, 2, 3])

print(f)            # frozenset({1, 2, 3})
f.add(4)            # AttributeError
```

> `frozenset` lug'at kaliti yoki boshqa to'plam elementi bo'la oladi, oddiy `set` esa bo'la olmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚡ Set comprehension

```python
kvadratlar = {i ** 2 for i in range(1, 6)}
print(kvadratlar)    # {1, 4, 9, 16, 25}
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Ro'yxatdagi takrorlanuvchi elementlarni olib tashlash:**

```python
sonlar = [1, 2, 2, 3, 3, 3, 4]
noyob = list(set(sonlar))
print(noyob)    # [1, 2, 3, 4]
```

**Ikki ro'yxatdagi umumiy elementlar:**

```python
a = ["Ali", "Vali", "Sardor"]
b = ["Vali", "Aziz", "Sardor"]

print(set(a) & set(b))    # {'Vali', 'Sardor'}
```

**Matndagi noyob harflar soni:**

```python
matn = "assalomu alaykum"
print(len(set(matn)))
```

**Takrorlanuvchi element bor-yo'qligini tekshirish:**

```python
sonlar = [1, 2, 3, 2]

if len(sonlar) != len(set(sonlar)):
    print("Takrorlanuvchi element bor")
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. 5 ta elementdan iborat to'plam yarating va unga yangi element qo'shing.
2. Ro'yxatdagi takrorlanuvchi elementlarni `set` yordamida olib tashlang.
3. Ikki to'plamning birlashmasi, kesishmasi va ayirmasini toping.
4. `remove()` va `discard()` farqini misol bilan ko'rsating.
5. Foydalanuvchidan so'z kiriting va undagi noyob harflarni chiqaring.
6. Ikki ro'yxatdagi umumiy elementlarni toping.
7. Bir to'plam ikkinchisining qism to'plami ekanini tekshiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- To'plam `{ }` qavs bilan yoziladi, **tartibsiz** va **noyob** elementlardan iborat.
- Indeks va kesim (slice) ishlamaydi.
- Bo'sh to'plam faqat `set()` bilan yaratiladi, `{}` lug'at hisoblanadi.
- `add()`, `update()` bilan qo'shiladi, `remove()`, `discard()`, `pop()` bilan o'chiriladi.
- `|`, `&`, `-`, `^` operatorlari birlashma, kesishma, ayirma va simmetrik ayirmani bajaradi.
- O'zgarmas to'plam kerak bo'lsa, `frozenset` ishlatiladi.

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