<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2020%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Virtual muhit, `pip` va `BeautifulSoup`

Python'da tayyor **tashqi kutubxonalar** juda ko'p. Ularni o'rnatish uchun **`pip`**, loyihalarni bir-biridan ajratish uchun **virtual muhit** ishlatiladi.

| Tushuncha | Tavsif |
|-----------|--------|
| **Virtual muhit (venv)** | Har bir loyiha uchun alohida, izolyatsiya qilingan Python muhiti |
| **`pip`** | Python kutubxonalarini o'rnatuvchi paket menejeri |
| **`.env` fayli** | Maxfiy sozlamalar (parol, API kalit) saqlanadigan fayl |
| **`python-decouple`** | `.env` faylidan sozlamalarni o'qiydigan kutubxona |
| **BeautifulSoup** | HTML sahifalardan ma'lumot ajratib oluvchi kutubxona |

> 💡 `.env` nomi ikki ma'noda uchraydi: ba'zan **virtual muhit papkasi** nomi sifatida (`.env` yoki `.venv`), ba'zan **maxfiy sozlamalar fayli** sifatida. Ikkalasi ham quyida ko'rsatilgan.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧪 Virtual muhit nima uchun kerak?

Aytaylik, 1-loyiha `requests 2.25` ni, 2-loyiha `requests 2.31` ni talab qiladi. Hammasi bitta joyga o'rnatilsa, versiyalar to'qnashadi.

| Muammo | Virtual muhit yechimi |
|--------|-----------------------|
| Versiyalar to'qnashuvi | Har bir loyihaning o'z kutubxonalari bor |
| Tizim Python'i ifloslanadi | Kutubxonalar faqat loyiha ichiga o'rnatiladi |
| Loyihani boshqaga berish qiyin | `requirements.txt` orqali bir buyruq bilan tiklanadi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ Virtual muhit yaratish

Loyiha papkasida terminalni oching:

```bash
python -m venv .venv
```

> Windows'da `python`, ba'zi tizimlarda (macOS/Linux) `python3` yoziladi. `.venv` — papka nomi (xohlagan nom berish mumkin: `venv`, `.env`).

Natijada loyiha ichida `.venv` papkasi paydo bo'ladi.

## Faollashtirish (activate)

| Operatsion tizim | Buyruq |
|------------------|--------|
| **Windows (CMD)** | `.venv\Scripts\activate` |
| **Windows (PowerShell)** | `.venv\Scripts\Activate.ps1` |
| **macOS / Linux** | `source .venv/bin/activate` |

Faollashgach, terminal oldida muhit nomi ko'rinadi:

```
(.venv) C:\loyiha>
```

> ⚠️ PowerShell'da xato chiqsa, bir marta shu buyruqni bajaring:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## O'chirish (deactivate)

```bash
deactivate
```

**Ish tartibi:**

```bash
python -m venv .venv         # 1. yaratish
.venv\Scripts\activate       # 2. faollashtirish
pip install requests         # 3. kutubxona o'rnatish
python main.py               # 4. dasturni ishga tushirish
deactivate                   # 5. tugatgach o'chirish
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📦 `pip` bilan ishlash

**`pip`** Python bilan birga o'rnatilgan. Kutubxonalar **PyPI** (pypi.org) saytidan yuklanadi.

| Buyruq | Vazifasi |
|--------|----------|
| `pip install nom` | Kutubxona o'rnatadi |
| `pip install nom==1.2.3` | Aniq versiyani o'rnatadi |
| `pip install --upgrade nom` | Kutubxonani yangilaydi |
| `pip uninstall nom` | Kutubxonani o'chiradi |
| `pip list` | O'rnatilgan kutubxonalar ro'yxati |
| `pip show nom` | Kutubxona haqida ma'lumot |
| `pip freeze` | Kutubxonalar va versiyalari ro'yxati |
| `pip --version` | `pip` versiyasi |

```bash
pip install requests
pip install beautifulsoup4
pip list
```

> ⚠️ O'rnatishdan oldin virtual muhit **faollashtirilganini** tekshiring, aks holda kutubxona butun tizimga o'rnatiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📄 `requirements.txt`

Loyihadagi barcha kutubxonalar ro'yxati. Loyihani boshqa kompyuterda tiklash uchun ishlatiladi.

**Yaratish:**

```bash
pip freeze > requirements.txt
```

**Fayl ko'rinishi:**

```
beautifulsoup4==4.12.3
python-decouple==3.8
requests==2.31.0
```

**Boshqa kompyuterda tiklash:**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔐 `.env` fayli va `python-decouple`

Parol, token, API kalit kabi ma'lumotlarni **kod ichiga yozish xavfli**. Ular `.env` faylida saqlanadi va kod orqali o'qiladi.

**1. Kutubxonani o'rnatish:**

```bash
pip install python-decouple
```

> ⚠️ O'rnatishda nom `python-decouple`, import qilishda esa `decouple`.

**2. `.env` fayl yaratish** (loyiha papkasida, `main.py` bilan bir joyda):

```
BOT_TOKEN=123456:ABC-DEF
API_KEY=mening_maxfiy_kalitim
DEBUG=True
MAX_URINISH=3
```

> Qiymatlar tirnoqsiz, `=` atrofida probelsiz yoziladi.

**3. Kodda o'qish:**

```python
from decouple import config

token = config("BOT_TOKEN")
api_key = config("API_KEY")

print(token)      # 123456:ABC-DEF
```

> `python-dotenv` dan farqi: `load_dotenv()` chaqirish **shart emas**, `config()` o'zi `.env` faylini topadi.

## Standart qiymat berish

Kalit `.env` da topilmasa, `default` qiymat ishlatiladi. `default` berilmasa, `UndefinedValueError` xatosi chiqadi.

```python
til = config("TIL", default="uz")
print(til)    # uz
```

## Tur o'zgartirish: `cast`

`.env` dagi barcha qiymatlar dastlab **matn (`str`)** bo'ladi. `cast` ularni kerakli turga o'tkazadi.

```python
from decouple import config

debug = config("DEBUG", default=False, cast=bool)
urinish = config("MAX_URINISH", default=3, cast=int)

print(debug, type(debug))        # True <class 'bool'>
print(urinish, type(urinish))    # 3 <class 'int'>
```

| `cast` | Natija | Misol |
|--------|--------|-------|
| `cast=int` | Butun son | `MAX_URINISH=3` → `3` |
| `cast=float` | Kasr son | `NARX=9.5` → `9.5` |
| `cast=bool` | `True` / `False` | `DEBUG=True` → `True` |

> `cast=bool` uchun `True`, `true`, `1`, `yes`, `on` qiymatlari `True`, `False`, `false`, `0`, `no`, `off` qiymatlari `False` bo'ladi.

## Ro'yxat (`Csv`)

Vergul bilan ajratilgan qiymatlarni ro'yxatga aylantiradi.

```
ADMINLAR=Ali,Vali,Sardor
```

```python
from decouple import config, Csv

adminlar = config("ADMINLAR", cast=Csv())
print(adminlar)    # ['Ali', 'Vali', 'Sardor']
```

**Asosiy usullar:**

| Usul | Vazifasi |
|------|----------|
| `config("KALIT")` | Qiymatni o'qiydi (yo'q bo'lsa xato) |
| `config("KALIT", default=...)` | Yo'q bo'lsa, standart qiymat |
| `config("KALIT", cast=int)` | Qiymatni turga o'tkazadi |
| `config("KALIT", cast=Csv())` | Vergul bilan ajratilgan ro'yxat |

## `.gitignore`

`.env` va virtual muhitni **GitHub'ga yuklamaslik** kerak. `.gitignore` fayliga yozing:

```
.env
.venv/
__pycache__/
```

> ⚠️ `.env` ichidagi maxfiy ma'lumotlar GitHub'ga tushib qolsa, ularni boshqalar ko'ra oladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🍜 BeautifulSoup kutubxonasi

**BeautifulSoup** — HTML va XML hujjatlarni tahlil qilib, kerakli ma'lumotni (matn, havola, rasm) ajratib olish uchun kutubxona. Bu jarayon **web scraping** deyiladi.

**O'rnatish:**

```bash
pip install beautifulsoup4 requests
```

| Kutubxona | Vazifasi |
|-----------|----------|
| `requests` | Internetdan sahifa HTML'ini yuklab oladi |
| `beautifulsoup4` | HTML'ni tahlil qilib, kerakli qismini topadi |

> ⚠️ O'rnatishda nom `beautifulsoup4`, import qilishda esa `bs4`.

**Import:**

```python
from bs4 import BeautifulSoup
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 Asosiy foydalanish

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Mening sahifam</h1>
    <p class="matn">Birinchi paragraf</p>
    <p class="matn">Ikkinchi paragraf</p>
    <a href="https://example.com">Havola</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.h1)           # <h1>Mening sahifam</h1>
print(soup.h1.text)      # Mening sahifam
```

> `"html.parser"` — Python'ning ichki tahlilchisi, qo'shimcha o'rnatish shart emas.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔎 Elementlarni qidirish

| Metod | Vazifasi | Qaytaradi |
|-------|----------|-----------|
| `find()` | Birinchi mos elementni topadi | Element yoki `None` |
| `find_all()` | Barcha mos elementlarni topadi | Ro'yxat |
| `select_one()` | CSS selektor bilan birinchisini topadi | Element yoki `None` |
| `select()` | CSS selektor bilan hammasini topadi | Ro'yxat |

```python
# Teg nomi bo'yicha
print(soup.find("h1").text)             # Mening sahifam

# Barcha paragraflar
for p in soup.find_all("p"):
    print(p.text)

# Klass bo'yicha (class_ — pastki chiziq bilan)
print(soup.find("p", class_="matn").text)

# CSS selektor bilan
print(soup.select_one("p.matn").text)
print(len(soup.select("p")))            # 2
```

**Natija (paragraflar):**

```
Birinchi paragraf
Ikkinchi paragraf
```

## CSS selektor belgilari

| Selektor | Ma'nosi | Misol |
|----------|---------|-------|
| `tag` | Teg bo'yicha | `p` |
| `.klass` | Klass bo'yicha | `.matn` |
| `#id` | ID bo'yicha | `#asosiy` |
| `tag.klass` | Teg va klass | `p.matn` |
| `ota > bola` | To'g'ridan-to'g'ri bola | `div > p` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏷️ Matn va atributlarni olish

```python
havola = soup.find("a")

print(havola.text)         # Havola
print(havola["href"])      # https://example.com
print(havola.get("href"))  # https://example.com
print(havola.attrs)        # {'href': 'https://example.com'}
```

| Usul | Vazifasi |
|------|----------|
| `.text` yoki `.get_text()` | Teg ichidagi matn |
| `.get_text(strip=True)` | Matnning chetidagi bo'shliqlarni olib tashlaydi |
| `["href"]` | Atribut qiymati (yo'q bo'lsa `KeyError`) |
| `.get("href")` | Atribut qiymati (yo'q bo'lsa `None`) |
| `.attrs` | Barcha atributlar (lug'at) |
| `.name` | Teg nomi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🌐 Real sahifadan ma'lumot olish

`requests` bilan sahifani yuklab, `BeautifulSoup` bilan tahlil qilamiz.
Mashq uchun maxsus tayyorlangan sayt: **quotes.toscrape.com**

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
javob = requests.get(url)

print(javob.status_code)    # 200 — muvaffaqiyatli

soup = BeautifulSoup(javob.text, "html.parser")

for blok in soup.find_all("div", class_="quote"):
    matn = blok.find("span", class_="text").text
    muallif = blok.find("small", class_="author").text
    print(f"{muallif}: {matn}")
```

**Barcha havolalarni olish:**

```python
for a in soup.find_all("a"):
    href = a.get("href")
    if href:
        print(href)
```

**Natijani `.json` faylga saqlash:**

```python
import json

royxat = []
for blok in soup.find_all("div", class_="quote"):
    royxat.append({
        "matn": blok.find("span", class_="text").text,
        "muallif": blok.find("small", class_="author").text
    })

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(royxat, f, ensure_ascii=False, indent=4)
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Xatolarni ushlash

```python
import requests

try:
    javob = requests.get("https://quotes.toscrape.com/", timeout=10)
    javob.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Sahifani yuklab bo'lmadi:", e)
```

| Holat | Tavsif |
|-------|--------|
| `status_code == 200` | Sahifa muvaffaqiyatli yuklandi |
| `404` | Sahifa topilmadi |
| `403` | Kirish taqiqlangan |
| `timeout=10` | 10 soniyada javob kelmasa, xato beradi |
| `find()` → `None` | Element topilmadi, `.text` xato beradi |

> ⚠️ `find()` hech narsa topmasa `None` qaytaradi. `.text` dan oldin tekshiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚖️ Scraping qoidalari

- Saytning `robots.txt` fayli va foydalanish shartlarini tekshiring.
- So'rovlarni juda tez-tez yubormang, serverga zarar bo'lmasin.
- Shaxsiy va maxfiy ma'lumotlarni yig'maslik kerak.
- Imkon bo'lsa, saytning rasmiy **API** sidan foydalaning.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `venv` yordamida virtual muhit yarating va faollashtiring.
2. `pip` bilan `requests` va `beautifulsoup4` ni o'rnating.
3. `pip list` va `pip freeze > requirements.txt` buyruqlarini bajaring.
4. `.env` fayl yarating, ichiga `API_KEY` va `DEBUG=True` yozing va `python-decouple` bilan o'qing.
5. `config()` da `default` va `cast=int` parametrlarini ishlatib ko'ring.
6. `.gitignore` faylga `.env` va `.venv/` ni qo'shing.
7. HTML matnidan `find()` va `find_all()` bilan ma'lumot ajrating.
8. `quotes.toscrape.com` dan barcha iqtibos va mualliflarni chiqarib, `.json` faylga saqlang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Virtual muhit** har bir loyiha uchun alohida kutubxonalar muhitini yaratadi: `python -m venv .venv`.
- Muhit faollashtirilgach, `pip install` kutubxonani faqat shu loyihaga o'rnatadi.
- `pip freeze > requirements.txt` va `pip install -r requirements.txt` loyihani tiklashga yordam beradi.
- `.env` fayli maxfiy ma'lumotlarni saqlaydi va u **GitHub'ga yuklanmaydi**.
- `python-decouple` da `config("KALIT")` bilan o'qiladi, `default` va `cast` parametrlari bor.
- **BeautifulSoup** HTML'dan ma'lumot ajratadi: `find()`, `find_all()`, `select()`, `.text`, `.get()`.
- `requests` sahifani yuklaydi, `BeautifulSoup` uni tahlil qiladi.

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