<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2017%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Python'da vaqt bilan ishlash (`datetime`)

**`datetime`** — Python'ning standart moduli bo'lib, sana va vaqt bilan ishlash uchun ishlatiladi. Uni alohida o'rnatish shart emas, faqat import qilinadi.

```python
from datetime import datetime, date, time, timedelta
```

**Asosiy klasslar:**

| Klass | Vazifasi | Misol |
|-------|----------|-------|
| `date` | Faqat **sana** (yil, oy, kun) | `2026-11-27` |
| `time` | Faqat **vaqt** (soat, daqiqa, soniya) | `14:30:00` |
| `datetime` | **Sana va vaqt** birgalikda | `2026-11-27 14:30:00` |
| `timedelta` | Ikki vaqt orasidagi **farq** (davomiylik) | `5 days, 0:00:00` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📅 1. `date`

**Ta'rif:** faqat sana (yil, oy, kun) bilan ishlaydi.

```python
from datetime import date

bugun = date.today()
print(bugun)             # 2026-11-27

d = date(2026, 11, 27)
print(d)                 # 2026-11-27
```

**Xususiyatlari:**

```python
d = date(2026, 11, 27)

print(d.year)         # 2026
print(d.month)        # 11
print(d.day)          # 27
print(d.weekday())    # 4  (0 = Dushanba, 6 = Yakshanba)
```

| Atribut / Metod | Vazifasi |
|-----------------|----------|
| `date.today()` | Bugungi sana |
| `.year`, `.month`, `.day` | Yil, oy, kun |
| `.weekday()` | Hafta kuni (`0` = Dushanba, `6` = Yakshanba) |
| `.isoweekday()` | Hafta kuni (`1` = Dushanba, `7` = Yakshanba) |
| `.isoformat()` | `YYYY-MM-DD` ko'rinishidagi matn |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⏰ 2. `time`

**Ta'rif:** faqat vaqt (soat, daqiqa, soniya) bilan ishlaydi.

```python
from datetime import time

t = time(14, 30, 45)
print(t)             # 14:30:45

print(t.hour)        # 14
print(t.minute)      # 30
print(t.second)      # 45
```

**Parametrlari:**

| Parametr | Oraliq |
|----------|--------|
| `hour` | `0` – `23` |
| `minute` | `0` – `59` |
| `second` | `0` – `59` |
| `microsecond` | `0` – `999999` |

> ⚠️ `time.now()` degan metod **yo'q**. Hozirgi vaqtni olish uchun `datetime.now().time()` ishlatiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🕒 3. `datetime`

**Ta'rif:** sana va vaqtni birgalikda saqlaydi.

```python
from datetime import datetime

hozir = datetime.now()
print(hozir)    # 2026-11-27 14:30:45.123456

d = datetime(2026, 11, 27, 14, 30, 0)
print(d)        # 2026-11-27 14:30:00
```

**Atribut va metodlari:**

```python
hozir = datetime.now()

print(hozir.year)       # yil
print(hozir.month)      # oy
print(hozir.day)        # kun
print(hozir.hour)       # soat
print(hozir.minute)     # daqiqa
print(hozir.second)     # soniya

print(hozir.date())     # faqat sana
print(hozir.time())     # faqat vaqt
```

| Metod | Vazifasi |
|-------|----------|
| `datetime.now()` | Hozirgi sana va vaqt |
| `datetime.today()` | Hozirgi sana va vaqt |
| `.date()` | Faqat sana qismi |
| `.time()` | Faqat vaqt qismi |
| `.replace(...)` | Ayrim qismlarni almashtirib, yangi obyekt qaytaradi |
| `.timestamp()` | Soniyalardagi vaqt (1970-yildan boshlab) |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⏳ 4. `timedelta`

**Ta'rif:** ikki vaqt orasidagi **farq** yoki qo'shiladigan/ayiriladigan **davomiylik**.

```python
from datetime import timedelta

farq = timedelta(days=5, hours=3, minutes=30)
print(farq)    # 5 days, 3:30:00
```

**Parametrlari:**

| Parametr | Ma'nosi |
|----------|---------|
| `weeks` | Hafta |
| `days` | Kun |
| `hours` | Soat |
| `minutes` | Daqiqa |
| `seconds` | Soniya |

> `timedelta` da `months` va `years` **yo'q**, chunki oy va yilning kunlari soni o'zgaruvchan.

## Sanaga qo'shish va ayirish

```python
from datetime import datetime, timedelta

bugun = datetime(2026, 11, 27)

print(bugun + timedelta(days=7))      # 2026-12-04 00:00:00
print(bugun - timedelta(days=30))     # 2026-10-28 00:00:00
print(bugun + timedelta(hours=5))     # 2026-11-27 05:00:00
```

## Ikki sana orasidagi farq

```python
from datetime import date

a = date(2026, 1, 1)
b = date(2026, 11, 27)

farq = b - a
print(farq)              # 330 days, 0:00:00
print(farq.days)         # 330
```

```python
from datetime import timedelta

t = timedelta(days=1, hours=2)
print(t.days)              # 1
print(t.seconds)           # 7200
print(t.total_seconds())   # 93600.0
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎨 Formatlash: `strftime()`

**Ta'rif:** sana/vaqtni **matnga** aylantiradi (istalgan ko'rinishda).

```python
from datetime import datetime

hozir = datetime(2026, 11, 27, 14, 30, 45)

print(hozir.strftime("%d.%m.%Y"))            # 27.11.2026
print(hozir.strftime("%Y-%m-%d %H:%M:%S"))   # 2026-11-27 14:30:45
print(hozir.strftime("%H:%M"))               # 14:30
print(hozir.strftime("%A, %B %d"))           # Friday, November 27
```

**Format belgilari:**

| Belgi | Ma'nosi | Misol |
|-------|---------|-------|
| `%Y` | Yil (4 xonali) | `2026` |
| `%y` | Yil (2 xonali) | `26` |
| `%m` | Oy (raqam) | `11` |
| `%B` | Oy nomi (to'liq) | `November` |
| `%b` | Oy nomi (qisqa) | `Nov` |
| `%d` | Kun | `27` |
| `%A` | Hafta kuni (to'liq) | `Friday` |
| `%a` | Hafta kuni (qisqa) | `Fri` |
| `%H` | Soat (24 soatlik) | `14` |
| `%I` | Soat (12 soatlik) | `02` |
| `%M` | Daqiqa | `30` |
| `%S` | Soniya | `45` |
| `%p` | AM / PM | `PM` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 Matndan sanaga: `strptime()`

**Ta'rif:** **matnni** `datetime` obyektiga aylantiradi. Format matnga mos bo'lishi shart.

```python
from datetime import datetime

matn = "27.11.2026 14:30"
d = datetime.strptime(matn, "%d.%m.%Y %H:%M")

print(d)          # 2026-11-27 14:30:00
print(d.year)     # 2026
```

| Metod | Yo'nalish |
|-------|-----------|
| `strftime()` | `datetime` → **matn** |
| `strptime()` | **matn** → `datetime` |

> ⚠️ Format mos kelmasa, `ValueError` xatosi chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚖️ Sanalarni taqqoslash

Sana va vaqt obyektlarini `<`, `>`, `==` operatorlari bilan taqqoslash mumkin.

```python
from datetime import date

a = date(2026, 1, 1)
b = date(2026, 11, 27)

print(a < b)     # True
print(a == b)    # False
print(a > b)     # False
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misollar

**Yoshni hisoblash:**

```python
from datetime import date

tugilgan = date(2005, 5, 15)
bugun = date.today()

yosh = bugun.year - tugilgan.year
if (bugun.month, bugun.day) < (tugilgan.month, tugilgan.day):
    yosh -= 1

print("Yosh:", yosh)
```

**Yangi yilgacha necha kun qolganini hisoblash:**

```python
from datetime import date

bugun = date.today()
yangi_yil = date(bugun.year + 1, 1, 1)

print("Yangi yilgacha:", (yangi_yil - bugun).days, "kun")
```

**Dastur bajarilish vaqtini o'lchash:**

```python
from datetime import datetime

boshlandi = datetime.now()

for i in range(1000000):
    pass

tugadi = datetime.now()
print("Sarflangan vaqt:", tugadi - boshlandi)
```

**Foydalanuvchi kiritgan sanani tekshirish:**

```python
from datetime import datetime

matn = input("Sanani kiriting (kun.oy.yil): ")
d = datetime.strptime(matn, "%d.%m.%Y")

print("Hafta kuni:", d.strftime("%A"))
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Bugungi sana va hozirgi vaqtni chiqaring.
2. Bugungi sanani `kun.oy.yil` ko'rinishida chiqaring.
3. Bugundan 100 kun keyingi sanani toping.
4. Tug'ilgan sanangizni kiriting va yoshingizni hisoblang.
5. Ikki sana orasida necha kun borligini toping.
6. Foydalanuvchi kiritgan sana qaysi hafta kuniga to'g'ri kelishini aniqlang.
7. Yangi yilgacha necha kun, soat qolganini hisoblang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- `date` faqat sana, `time` faqat vaqt, `datetime` ikkalasini saqlaydi.
- `datetime.now()` va `date.today()` joriy vaqtni beradi.
- `timedelta` kun, soat, daqiqa kabi **davomiylik** bilan ishlaydi (oy va yil yo'q).
- Ikki sana ayirmasi `timedelta` obyektini qaytaradi.
- `strftime()` sanani matnga, `strptime()` matnni sanaga aylantiradi.

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