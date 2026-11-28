<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2028%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 FastAPI frameworkiga kirish

**FastAPI** — Python'da **web API** yaratish uchun zamonaviy, tez va qulay framework. U Python'ning **tip ko'rsatkichlari** (type hints) asosida ishlaydi, ma'lumotlarni avtomatik tekshiradi va **avtomatik hujjat** (Swagger) yaratadi.

| Xususiyat | Tavsif |
|-----------|--------|
| Tezlik | Eng tez Python frameworklaridan biri |
| Avtomatik hujjat | `/docs` sahifasida tayyor Swagger UI |
| Validatsiya | Kiruvchi ma'lumot turi avtomatik tekshiriladi (**Pydantic**) |
| Type hints | `son: int` yozilsa, FastAPI uni `int` ga o'tkazadi |
| Async | `async def` ni qo'llab-quvvatlaydi |
| Qachon ishlatiladi | Backend API, Telegram bot uchun server, mobil ilova backend'i |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🌐 API va HTTP nima?

**API (Application Programming Interface)** — dasturlar bir-biri bilan gaplashadigan **interfeys**. Masalan, mobil ilova serverdan ma'lumot so'raydi, server **JSON** ko'rinishida javob beradi.

```
Mijoz (brauzer, ilova)  --- so'rov (request) --->  Server (FastAPI)
Mijoz (brauzer, ilova)  <--- javob (response) ---  Server (FastAPI)
```

## HTTP metodlari va CRUD

| HTTP metod | CRUD | Vazifasi | Misol |
|------------|------|----------|-------|
| **GET** | Read | Ma'lumotni **olish** | Talabalar ro'yxatini olish |
| **POST** | Create | Yangi ma'lumot **yaratish** | Yangi talaba qo'shish |
| **PUT** | Update | Mavjud ma'lumotni **to'liq yangilash** | Talaba ma'lumotini almashtirish |
| **DELETE** | Delete | Ma'lumotni **o'chirish** | Talabani o'chirish |

> 💡 26-darsdagi CRUD (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) shu HTTP metodlariga mos keladi.

## Eng ko'p uchraydigan status kodlar

| Kod | Ma'nosi | Qachon |
|-----|---------|--------|
| `200` | OK | So'rov muvaffaqiyatli |
| `201` | Created | Yangi ma'lumot yaratildi |
| `204` | No Content | Muvaffaqiyatli, javob tanasi yo'q (odatda `DELETE`) |
| `400` | Bad Request | So'rov noto'g'ri |
| `404` | Not Found | Ma'lumot topilmadi |
| `422` | Unprocessable Entity | Ma'lumot validatsiyadan o'tmadi (FastAPI avtomatik beradi) |
| `500` | Internal Server Error | Serverda xato |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ O'rnatish

Avval virtual muhit yarating va faollashtiring (20-dars):

```bash
python -m venv .venv
.venv\Scripts\activate
```

FastAPI'ni o'rnating:

```bash
pip install "fastapi[standard]"
```

> `fastapi[standard]` FastAPI bilan birga serverni (`uvicorn`), `fastapi` buyruq qatori vositasini va boshqa kerakli kutubxonalarni o'rnatadi. Tirnoq ichida yozing.

| Kutubxona | Vazifasi |
|-----------|----------|
| `fastapi` | Frameworkning o'zi |
| `pydantic` | Ma'lumotlarni tekshirish (FastAPI bilan birga keladi) |
| `uvicorn` | FastAPI ilovasini ishga tushiruvchi server |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🚀 Birinchi ilova

`main.py` fayl yarating:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def bosh_sahifa():
    return {"xabar": "Salom, FastAPI!"}
```

**Qismlari:**

| Qism | Tavsif |
|------|--------|
| `app = FastAPI()` | Ilova obyekti |
| `@app.get("/")` | Dekorator: `GET` so'rov `/` manziliga kelsa, funksiya ishlaydi |
| `return {...}` | Lug'at avtomatik **JSON** ga aylantiriladi |

## Ishga tushirish

```bash
fastapi dev main.py
```

Yoki `uvicorn` bilan:

```bash
uvicorn main:app --reload
```

| Qism | Ma'nosi |
|------|---------|
| `main` | Fayl nomi (`main.py`) |
| `app` | Fayl ichidagi `FastAPI()` obyekti nomi |
| `--reload` | Kod o'zgarganda server o'zi qayta ishga tushadi |

Server `http://127.0.0.1:8000` manzilida ishlaydi.

| Manzil | Nima ochiladi |
|--------|---------------|
| `http://127.0.0.1:8000/` | Sizning API javobingiz (JSON) |
| `http://127.0.0.1:8000/docs` | **Swagger UI**: API ni brauzerning o'zida sinash |
| `http://127.0.0.1:8000/redoc` | ReDoc: muqobil hujjat ko'rinishi |

> ⚠️ `--reload` va `fastapi dev` faqat **dasturlash** vaqtida ishlatiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📥 1. `GET` metodi

**Ta'rif:** serverdan ma'lumot **olish** uchun ishlatiladi. Ma'lumotni o'zgartirmaydi.

```python
from fastapi import FastAPI

app = FastAPI()

mevalar = ["olma", "anor", "uzum"]


@app.get("/mevalar")
def mevalar_royxati():
    return mevalar
```

`GET /mevalar` → `["olma", "anor", "uzum"]`

## Path parametr

URL ichidagi o'zgaruvchan qism `{}` bilan yoziladi:

```python
@app.get("/mevalar/{indeks}")
def bitta_meva(indeks: int):
    return {"meva": mevalar[indeks]}
```

`GET /mevalar/1` → `{"meva": "anor"}`

> `indeks: int` yozilgani uchun FastAPI uni avtomatik `int` ga o'tkazadi. `/mevalar/abc` yozilsa, **422** xato qaytaradi.

## Query parametr

URL dagi `?` dan keyingi qism:

```python
@app.get("/qidirish")
def qidirish(nom: str, limit: int = 10):
    return {"qidiruv": nom, "limit": limit}
```

`GET /qidirish?nom=olma&limit=5` → `{"qidiruv": "olma", "limit": 5}`

| Parametr turi | Qayerda | Majburiymi |
|---------------|---------|------------|
| **Path** | URL ichida `{nom}` | Ha |
| **Query** (standart qiymatsiz) | `?nom=...` | Ha |
| **Query** (standart qiymatli) | `?limit=5` | Yo'q (`limit: int = 10`) |
| **Query** (ixtiyoriy) | `?kurs=2` | Yo'q (`kurs: int | None = None`) |

```python
@app.get("/filtr")
def filtr(kurs: int | None = None):
    if kurs is None:
        return {"natija": "hammasi"}
    return {"natija": f"{kurs}-kurs"}
```

> ⚠️ **Tartib muhim:** aniq yo'l (`/talabalar/qidirish`) umumiy yo'ldan (`/talabalar/{id}`) **oldin** yozilishi kerak, aks holda `qidirish` so'zi `id` deb olinadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📦 Pydantic model

`POST` va `PUT` da ma'lumot so'rov **tanasida** (body) JSON ko'rinishida keladi. Uning tuzilishini **Pydantic** modeli bilan belgilaymiz.

```python
from pydantic import BaseModel


class Talaba(BaseModel):
    ism: str
    yosh: int
    kurs: int = 1
```

| Qoida | Tavsif |
|-------|--------|
| `BaseModel` dan meros | Har bir model shundan boshlanadi (OOP, 25-dars) |
| `ism: str` | Majburiy maydon, turi `str` |
| `kurs: int = 1` | Ixtiyoriy maydon, standart qiymati `1` |
| Validatsiya | Tur mos kelmasa, FastAPI avtomatik **422** xato qaytaradi |

```python
t = Talaba(ism="Ali", yosh=20)

print(t.ism)            # Ali
print(t.kurs)           # 1
print(t.model_dump())   # {'ism': 'Ali', 'yosh': 20, 'kurs': 1}
```

> `model_dump()` modelni oddiy lug'atga aylantiradi (Pydantic 2 da; eski versiyada `.dict()` edi).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ 2. `POST` metodi

**Ta'rif:** serverda **yangi ma'lumot yaratish** uchun ishlatiladi. Ma'lumot so'rov tanasida (JSON) yuboriladi.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Talaba(BaseModel):
    ism: str
    yosh: int
    kurs: int = 1


talabalar = []


@app.post("/talabalar", status_code=201)
def talaba_qosh(talaba: Talaba):
    talabalar.append(talaba.model_dump())
    return {"xabar": "Qo'shildi", "talaba": talaba}
```

**So'rov (JSON):**

```json
{
    "ism": "Ali",
    "yosh": 20
}
```

**Javob (`201`):**

```json
{
    "xabar": "Qo'shildi",
    "talaba": {"ism": "Ali", "yosh": 20, "kurs": 1}
}
```

**Noto'g'ri ma'lumot yuborilsa** (`"yosh": "yigirma"`), FastAPI `422` xatosini o'zi qaytaradi, funksiya umuman ishga tushmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✏️ 3. `PUT` metodi

**Ta'rif:** mavjud ma'lumotni **to'liq almashtirish** (yangilash) uchun ishlatiladi. Qaysi ma'lumot ekani **path parametr** orqali, yangi qiymatlar esa **tana** orqali beriladi.

```python
@app.put("/talabalar/{talaba_id}")
def talaba_yangila(talaba_id: int, talaba: Talaba):
    talabalar[talaba_id] = talaba.model_dump()
    return {"xabar": "Yangilandi", "talaba": talaba}
```

`PUT /talabalar/0` + tana:

```json
{
    "ism": "Ali",
    "yosh": 21,
    "kurs": 3
}
```

| | `PUT` | `PATCH` |
|---|-------|---------|
| Vazifasi | Ma'lumotni **to'liq** almashtiradi | Ma'lumotning **bir qismini** o'zgartiradi |
| Yuboriladigan maydonlar | Hammasi | Faqat o'zgargani |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗑️ 4. `DELETE` metodi

**Ta'rif:** ma'lumotni **o'chirish** uchun ishlatiladi.

```python
@app.delete("/talabalar/{talaba_id}", status_code=204)
def talaba_ochir(talaba_id: int):
    talabalar.pop(talaba_id)
```

> `204 No Content` — muvaffaqiyatli, lekin javob tanasi yo'q. Shuning uchun funksiya hech narsa qaytarmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Xatolarni qaytarish: `HTTPException`

Ma'lumot topilmasa yoki noto'g'ri bo'lsa, mijozga **to'g'ri status kod** bilan xato qaytariladi.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

mevalar = ["olma", "anor", "uzum"]


@app.get("/mevalar/{indeks}")
def bitta_meva(indeks: int):
    if indeks < 0 or indeks >= len(mevalar):
        raise HTTPException(status_code=404, detail="Meva topilmadi")
    return {"meva": mevalar[indeks]}
```

`GET /mevalar/10` javobi (`404`):

```json
{
    "detail": "Meva topilmadi"
}
```

> `return` emas, **`raise`** ishlatiladi (18-darsdagi xatolar bilan ishlash).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎯 `response_model`

Javob qanday ko'rinishda bo'lishini belgilaydi. Ortiqcha yoki maxfiy maydonlarni (masalan, parol) yashirish uchun ishlatiladi.

```python
from pydantic import BaseModel


class FoydalanuvchiKirish(BaseModel):
    ism: str
    parol: str


class FoydalanuvchiChiqish(BaseModel):
    ism: str


@app.post("/royxatdan-otish", response_model=FoydalanuvchiChiqish)
def royxatdan_otish(f: FoydalanuvchiKirish):
    return f          # parol javobda ko'rinmaydi
```

`POST` javobi: `{"ism": "Ali"}` (parol chiqmaydi).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol: to'liq CRUD API

Talabalar API'si: ma'lumotlar vaqtincha **lug'atda** saqlanadi (server o'chsa, yo'qoladi).

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Talabalar API")


class Talaba(BaseModel):
    ism: str
    yosh: int
    kurs: int = 1


talabalar: dict[int, dict] = {}
keyingi_id = 1


# READ (hammasi)
@app.get("/talabalar")
def hammasi(kurs: int | None = None):
    if kurs is None:
        return talabalar
    return {i: t for i, t in talabalar.items() if t["kurs"] == kurs}


# READ (bittasi)
@app.get("/talabalar/{talaba_id}")
def bittasi(talaba_id: int):
    if talaba_id not in talabalar:
        raise HTTPException(status_code=404, detail="Talaba topilmadi")
    return talabalar[talaba_id]


# CREATE
@app.post("/talabalar", status_code=201)
def qosh(talaba: Talaba):
    global keyingi_id
    talabalar[keyingi_id] = talaba.model_dump()
    yaratilgan_id = keyingi_id
    keyingi_id += 1
    return {"id": yaratilgan_id, **talabalar[yaratilgan_id]}


# UPDATE
@app.put("/talabalar/{talaba_id}")
def yangila(talaba_id: int, talaba: Talaba):
    if talaba_id not in talabalar:
        raise HTTPException(status_code=404, detail="Talaba topilmadi")
    talabalar[talaba_id] = talaba.model_dump()
    return {"id": talaba_id, **talabalar[talaba_id]}


# DELETE
@app.delete("/talabalar/{talaba_id}", status_code=204)
def ochir(talaba_id: int):
    if talaba_id not in talabalar:
        raise HTTPException(status_code=404, detail="Talaba topilmadi")
    del talabalar[talaba_id]
```

## Sinab ko'rish

**1. Swagger orqali:** `http://127.0.0.1:8000/docs` oching, metodni tanlang, **Try it out** → **Execute** bosing.

**2. `curl` bilan (terminal):**

```bash
curl http://127.0.0.1:8000/talabalar

curl -X POST http://127.0.0.1:8000/talabalar \
     -H "Content-Type: application/json" \
     -d '{"ism": "Ali", "yosh": 20}'
```

> Windows CMD'da `curl` da tirnoqlar boshqacha ishlaydi, shuning uchun qulayi Swagger yoki quyidagi `requests` usuli.

**3. Python `requests` bilan (20-darsda o'rnatilgan):**

```python
import requests

url = "http://127.0.0.1:8000/talabalar"

# POST
javob = requests.post(url, json={"ism": "Ali", "yosh": 20})
print(javob.status_code, javob.json())    # 201 {'id': 1, 'ism': 'Ali', ...}

# GET
print(requests.get(url).json())

# PUT
requests.put(f"{url}/1", json={"ism": "Ali", "yosh": 21, "kurs": 3})

# DELETE
print(requests.delete(f"{url}/1").status_code)    # 204
```

> Ikkinchi terminal oching: birida server ishlab turadi, ikkinchisida `requests` kodini ishga tushiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧩 Loyiha tuzilishi (tavsiya)

Loyiha kattalashganda hammasini bitta faylga yozmaslik kerak:

```
loyiha/
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
└── main.py
```

```bash
pip freeze > requirements.txt
```

> `.env` va `.venv/` ni `.gitignore` ga qo'shishni unutmang (20-dars).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. FastAPI o'rnating va `GET /` da `{"xabar": "Salom"}` qaytaradigan ilova yozing.
2. `/docs` sahifasini oching va API'ni brauzerda sinab ko'ring.
3. `GET /salom/{ism}` yozing: `Salom, <ism>!` qaytarsin.
4. `GET /yigindi?a=5&b=3` yozing: ikki son yig'indisini qaytarsin.
5. `Mahsulot` modeli (`nom`, `narx`, `miqdor`) yarating va `POST /mahsulotlar` yozing.
6. `PUT /mahsulotlar/{id}` bilan mahsulotni yangilang.
7. `DELETE /mahsulotlar/{id}` bilan o'chiring, topilmasa `404` qaytaring.
8. Noto'g'ri turdagi ma'lumot yuborib, `422` xatosini kuzating.
9. `requests` kutubxonasi bilan o'z API'ingizga 4 ta metoddan so'rov yuboring.
10. `response_model` yordamida parolni javobdan yashiring.
11. Kitoblar API'sini yarating: to'liq CRUD, `GET` da `?muallif=` bo'yicha filtr bo'lsin.
12. Lug'at o'rniga **SQLite** (26 va 27-darslar) ishlatib, ma'lumotni bazaga saqlang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **FastAPI** — Python'da tez va qulay API yaratish frameworki, `/docs` da avtomatik hujjat beradi.
- Ishga tushirish: `fastapi dev main.py` yoki `uvicorn main:app --reload`.
- **GET** — olish, **POST** — yaratish, **PUT** — to'liq yangilash, **DELETE** — o'chirish.
- **Path parametr** (`/talabalar/{id}`) va **query parametr** (`?kurs=2`) type hints bilan avtomatik tekshiriladi.
- **Pydantic** (`BaseModel`) so'rov tanasi tuzilishini belgilaydi, noto'g'ri ma'lumotga `422` qaytaradi.
- Xato holatida `raise HTTPException(status_code=404, detail="...")` ishlatiladi.
- `status_code=201` (yaratildi) va `204` (o'chirildi) javoblarni to'g'ri ifodalaydi.
- `response_model` javobdagi maydonlarni nazorat qiladi.

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