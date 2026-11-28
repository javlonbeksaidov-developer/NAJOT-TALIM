<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2036%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 PostgreSQL bilan tanishuv

**PostgreSQL** (qisqacha **Postgres**) — kuchli, ochiq kodli (open source) **relyatsion ma'lumotlar bazasi boshqarish tizimi (DBMS)**. U 30 yildan ortiq rivojlanib kelmoqda va backend loyihalarda eng ko'p tanlanadigan bazalardan biri.

| Xususiyat | Tavsif |
|-----------|--------|
| Turi | Relyatsion (SQL) DBMS |
| Litsenziya | Bepul, ochiq kodli |
| Arxitektura | **Mijoz-server**: baza alohida server jarayoni sifatida ishlaydi |
| Standart port | `5432` |
| Ishonchlilik | **ACID** tranzaksiyalar, ma'lumot yo'qolishidan himoya |
| Kengayuvchanlik | Katta hajm, ko'p foydalanuvchi, murakkab so'rovlar |
| Qo'shimcha turlar | `JSONB`, massivlar, `UUID`, sana/vaqt turlari |
| Qachon ishlatiladi | Haqiqiy (production) loyihalar, veb-saytlar, API, bot backend'lari |

**ACID nima?**

| Harf | Ma'nosi | Tavsif |
|------|---------|--------|
| **A** | Atomicity | Amallar yo to'liq bajariladi, yo umuman bajarilmaydi |
| **C** | Consistency | Ma'lumot doim cheklovlarga mos qoladi |
| **I** | Isolation | Bir vaqtda ishlayotgan so'rovlar bir-biriga halaqit bermaydi |
| **D** | Durability | Saqlangan ma'lumot server o'chsa ham yo'qolmaydi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🆚 SQLite dan farqi

26-30 darslarda **SQLite** bilan ishladik. Endi loyiha kattalashganda PostgreSQL kerak bo'ladi.

| | SQLite | PostgreSQL |
|---|--------|------------|
| Ishlash usuli | Bitta `.db` fayl, server yo'q | Alohida server jarayoni |
| O'rnatish | Shart emas (Python bilan keladi) | Alohida o'rnatiladi |
| Ko'p foydalanuvchi | Cheklangan (yozishda bitta) | Yuzlab bir vaqtdagi ulanish |
| Foydalanuvchi va huquqlar | Yo'q | Bor (`USER`, `ROLE`, `GRANT`) |
| Ma'lumot turlari | Oddiy, erkin tiplash | Qat'iy va boy turlar |
| Qachon | O'rganish, kichik ilova, bot | Production, katta loyiha |

> 💡 SQL tili asosan bir xil: `SELECT`, `INSERT`, `UPDATE`, `DELETE` ni bilsangiz, PostgreSQL'ga o'tish oson. SQLAlchemy ishlatsangiz, kodning katta qismi o'zgarmaydi, asosan ulanish manzili almashadi (30-dars).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 Asosiy tushunchalar

| Tushuncha | Tavsif |
|-----------|--------|
| **Server (cluster)** | Ishlab turgan PostgreSQL jarayoni, ichida bir nechta baza bo'ladi |
| **Database** | Alohida baza (masalan, `maktab`, `dukon`) |
| **Schema** | Baza ichidagi "papka"; standart nomi `public` |
| **Table** | Jadval (qator va ustunlar) |
| **Role / User** | Bazaga kiruvchi foydalanuvchi (huquqlari bilan) |
| **`postgres`** | O'rnatishda yaratiladigan standart **superuser** (bosh administrator) |
| **psql** | Terminalda ishlaydigan PostgreSQL mijozi |
| **pgAdmin** | Grafik (oynali) boshqaruv dasturi |

**Ierarxiya:**

```
Server (5432-port)
 └── Database (maktab)
      └── Schema (public)
           └── Table (talabalar)
                └── Row / Column
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ O'rnatish

> ℹ️ Versiya raqami vaqt o'tishi bilan o'zgaradi. Oxirgi barqaror versiyani **postgresql.org/download** sahifasidan tekshiring. Quyidagi qadamlar versiyaga bog'liq emas.

## 🪟 Windows

**1. O'rnatuvchini yuklab olish:** `postgresql.org/download/windows` sahifasidan **EDB installer** (`.exe`) ni yuklab oling.

**2. O'rnatuvchini ishga tushirib, qadamlarni bajaring:**

| Qadam | Nima qilish kerak |
|-------|-------------------|
| Komponentlar | **PostgreSQL Server**, **pgAdmin 4**, **Command Line Tools** belgilangan bo'lsin |
| Papka | Standart joyni qoldiring |
| **Parol** | `postgres` foydalanuvchisi uchun **parol o'ylab toping va eslab qoling** |
| **Port** | Standart `5432` ni qoldiring |
| Locale | Standart (Default locale) |
| Stack Builder | Boshida kerak emas, o'tkazib yuborish mumkin |

> 🚨 **Parolni unutmang!** Uni qayta tiklash ancha murakkab. Bu parol `postgres` superuser'ga tegishli.

**3. Tekshirish:** Start menyusidan **SQL Shell (psql)** ni oching. `Server`, `Database`, `Port`, `Username` so'ralganda **Enter** bosib standartni qoldiring, `Password` ga o'rnatishdagi parolni kiriting:

```
postgres=#
```

Shu belgi chiqsa, o'rnatish muvaffaqiyatli.

**4. `psql` ni oddiy terminaldan ishlatish (PATH):**

Agar CMD/PowerShell'da `psql` buyrug'i topilmasa, `bin` papkasini **PATH** ga qo'shing:

```
C:\Program Files\PostgreSQL\<versiya>\bin
```

`<versiya>` o'rniga o'rnatilgan versiya raqami yoziladi. Terminalni qayta ochib tekshiring:

```bash
psql --version
```

## 🍎 macOS

**1-usul: Postgres.app** (eng oson): `postgresapp.com` dan yuklab, `Applications` papkasiga ko'chiring va oching.

**2-usul: Homebrew**

```bash
brew install postgresql@<versiya>
brew services start postgresql@<versiya>
```

```bash
psql postgres
```

> Homebrew'da superuser nomi odatda **tizimdagi foydalanuvchi nomingiz** bo'ladi.

## 🐧 Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**Xizmatni boshqarish:**

```bash
sudo systemctl status postgresql      # holat
sudo systemctl start postgresql       # ishga tushirish
sudo systemctl enable postgresql      # tizim yoqilganda avtomatik ishlash
sudo systemctl restart postgresql     # qayta ishga tushirish
```

**`postgres` foydalanuvchisi bilan kirish:**

```bash
sudo -u postgres psql
```

**`postgres` ga parol o'rnatish:**

```sql
ALTER USER postgres WITH PASSWORD 'kuchli_parol';
```

## 🐳 Docker orqali (muqobil, barcha tizimlarda)

O'rnatmasdan, konteynerda ishga tushirish:

```bash
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=kuchli_parol \
  -p 5432:5432 \
  -d postgres
```

| Qism | Ma'nosi |
|------|---------|
| `--name my-postgres` | Konteyner nomi |
| `-e POSTGRES_PASSWORD=...` | `postgres` foydalanuvchisi paroli |
| `-p 5432:5432` | Portni tashqariga ochish |
| `-d` | Fonda ishlatish |

```bash
docker exec -it my-postgres psql -U postgres
```

> Ma'lumot konteyner o'chganda yo'qolmasligi uchun `-v pgdata:/var/lib/postgresql/data` (volume) qo'shiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💻 `psql` bilan ishlash

**`psql`** — PostgreSQL'ga terminaldan ulanish vositasi.

**Ulanish:**

```bash
psql -U postgres                          # postgres foydalanuvchisi
psql -U postgres -h localhost -p 5432     # server va port bilan
psql -U ali -d maktab                     # foydalanuvchi va baza bilan
```

| Parametr | Ma'nosi |
|----------|---------|
| `-U` | Foydalanuvchi nomi |
| `-d` | Baza nomi |
| `-h` | Server manzili (`localhost`) |
| `-p` | Port (`5432`) |

## Meta-buyruqlar (`\` bilan boshlanadi)

Bular SQL emas, `psql` ning o'z buyruqlari. Oxiriga `;` qo'yilmaydi.

| Buyruq | Vazifasi |
|--------|----------|
| `\l` | Barcha bazalar ro'yxati |
| `\c nom` | Boshqa bazaga o'tish (connect) |
| `\dt` | Joriy bazadagi jadvallar |
| `\d jadval` | Jadval tuzilishi (ustunlar, turlar) |
| `\du` | Foydalanuvchilar (role'lar) ro'yxati |
| `\dn` | Sxemalar ro'yxati |
| `\conninfo` | Joriy ulanish haqida ma'lumot |
| `\x` | Natijani kengaytirilgan (vertikal) ko'rinishda ko'rsatish |
| `\i fayl.sql` | SQL fayldagi buyruqlarni bajarish |
| `\?` | Barcha `psql` buyruqlari yordami |
| `\q` | `psql` dan chiqish |

> ⚠️ **SQL buyruqlar oxirida `;` shart.** Qo'ymasangiz, `psql` davomini kutib, `postgres-#` ko'rsatib turadi.

```
postgres=# SELECT version();
postgres=# \l
postgres=# \q
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗄️ Baza va foydalanuvchi yaratish

Loyiha uchun alohida **baza** va **foydalanuvchi** yaratish yaxshi odat. Hamma narsani `postgres` superuser bilan qilish xavfsiz emas.

**1. `psql` ga `postgres` sifatida kiring:**

```bash
psql -U postgres
```

**2. Foydalanuvchi yarating:**

```sql
CREATE USER ali WITH PASSWORD 'mening_parolim';
```

**3. Shu foydalanuvchi egasi bo'lgan baza yarating:**

```sql
CREATE DATABASE maktab OWNER ali;
```

**4. Tekshirish:**

```
postgres=# \l
postgres=# \du
```

**5. Yangi foydalanuvchi bilan ulanish:**

```bash
psql -U ali -d maktab -h localhost
```

**Boshqa foydali buyruqlar:**

| SQL buyruq | Vazifasi |
|------------|----------|
| `CREATE DATABASE nom;` | Baza yaratadi |
| `DROP DATABASE nom;` | Bazani **butunlay o'chiradi** |
| `CREATE USER nom WITH PASSWORD '...';` | Foydalanuvchi yaratadi |
| `ALTER USER nom WITH PASSWORD '...';` | Parolni o'zgartiradi |
| `DROP USER nom;` | Foydalanuvchini o'chiradi |
| `GRANT ALL PRIVILEGES ON DATABASE nom TO user;` | Bazaga huquq beradi |

> ⚠️ PostgreSQL 15 dan boshlab oddiy foydalanuvchi `public` sxemada jadval yarata olmasligi mumkin. Shuning uchun bazani `OWNER` bilan yaratish eng sodda yechim.

> 🚨 `DROP DATABASE` va `DROP USER` qaytarib bo'lmaydi. Ishlatishdan oldin ikki marta o'ylang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧪 Birinchi jadval va SQL

`maktab` bazasiga ulangan holda:

```sql
CREATE TABLE talabalar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    yosh INTEGER,
    kurs INTEGER DEFAULT 1,
    ball NUMERIC(5, 2) DEFAULT 0
);
```

```sql
INSERT INTO talabalar (ism, yosh, kurs, ball)
VALUES ('Ali', 20, 2, 85.50),
       ('Vali', 22, 3, 92.00),
       ('Sardor', 19, 1, 70.00);
```

```sql
SELECT * FROM talabalar;
SELECT ism, ball FROM talabalar WHERE ball > 80 ORDER BY ball DESC;
UPDATE talabalar SET ball = 95 WHERE id = 1;
DELETE FROM talabalar WHERE id = 3;
```

```
maktab=> \dt
maktab=> \d talabalar
```

> 26-darsdagi SQL buyruqlar PostgreSQL'da deyarli o'zgarishsiz ishlaydi. Asosiy farqlardan biri: SQLite'dagi `INTEGER PRIMARY KEY AUTOINCREMENT` o'rniga PostgreSQL'da `SERIAL PRIMARY KEY` yoziladi.

## Ma'lumot turlari

| Tur | Ma'nosi | SQLite'dagi analogi |
|-----|---------|---------------------|
| `SERIAL` | Avtomatik oshuvchi butun son (ko'pincha `id` uchun) | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| `INTEGER` | Butun son | `INTEGER` |
| `BIGINT` | Katta butun son | `INTEGER` |
| `NUMERIC(p, s)` | Aniq kasr son (pul uchun yaxshi) | `REAL` |
| `REAL`, `DOUBLE PRECISION` | Taxminiy kasr son | `REAL` |
| `VARCHAR(n)` | Uzunligi cheklangan matn | `TEXT` |
| `TEXT` | Uzunligi cheklanmagan matn | `TEXT` |
| `BOOLEAN` | `TRUE` / `FALSE` | `INTEGER` (0/1) |
| `DATE` | Sana | `TEXT` |
| `TIMESTAMP` | Sana va vaqt | `TEXT` |
| `JSONB` | JSON ma'lumot (indekslanadi, qidiriladi) | `TEXT` |
| `UUID` | Noyob identifikator | `TEXT` |

> 💡 Yangi loyihalarda `id` uchun `GENERATED ALWAYS AS IDENTITY` ham tavsiya etiladi (`SERIAL` ning zamonaviy muqobili). O'rganish uchun `SERIAL` oddiyroq.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🖥️ pgAdmin

**pgAdmin** — PostgreSQL'ni oynali interfeysda boshqarish dasturi (Windows installer bilan birga o'rnatiladi).

**Serverga ulanish:**

1. pgAdmin'ni oching, kirishda so'ralgan **master parol** qo'ying (bu pgAdmin'ning o'z paroli).
2. Chapdagi **Servers** ustiga o'ng tugma → **Register → Server**.
3. **General** → `Name`: `Local`.
4. **Connection** → `Host`: `localhost`, `Port`: `5432`, `Username`: `postgres`, `Password`: o'rnatishdagi parol.
5. **Save** bosing.

**Imkoniyatlari:**

| Imkoniyat | Qayerda |
|-----------|---------|
| Baza va jadval ko'rish | Chap daraxt: `Databases → maktab → Schemas → public → Tables` |
| SQL yozish | Bazaga o'ng tugma → **Query Tool** |
| Jadval ma'lumotini ko'rish | Jadvalga o'ng tugma → **View/Edit Data → All Rows** |
| Baza zaxira nusxasi | Bazaga o'ng tugma → **Backup...** |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🐍 Python bilan ulanish

## 1. `psycopg2` — to'g'ridan-to'g'ri ulanish

PostgreSQL uchun Python **drayveri** (virtual muhitni faollashtirib o'rnating, 20-dars):

```bash
pip install psycopg2-binary
```

```python
import psycopg2

conn = psycopg2.connect(
    dbname="maktab",
    user="ali",
    password="mening_parolim",
    host="localhost",
    port=5432,
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM talabalar WHERE kurs = %s", (2,))
for qator in cursor.fetchall():
    print(qator)

conn.commit()
cursor.close()
conn.close()
```

> ⚠️ `sqlite3` da qiymat `?` bilan uzatilgan, `psycopg2` da esa **`%s`** ishlatiladi. Tuzilish (`execute`, `fetchall`, `commit`) deyarli bir xil. Qiymatni f-string bilan qo'shmang (SQL Injection!).

**`with` bilan:**

```python
with psycopg2.connect(dbname="maktab", user="ali", password="mening_parolim", host="localhost") as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO talabalar (ism, yosh) VALUES (%s, %s)",
            ("Aziz", 21)
        )
```

> `with conn:` blokidan muvaffaqiyatli chiqilganda `commit()` avtomatik bajariladi, xato bo'lsa `rollback()`. Ulanishni esa alohida `conn.close()` bilan yopish kerak.

## 2. Sozlamalarni `.env` da saqlash (python-decouple)

Parolni kod ichiga yozmang (20-dars).

**`.env`:**

```
DB_NAME=maktab
DB_USER=ali
DB_PASSWORD=mening_parolim
DB_HOST=localhost
DB_PORT=5432
```

```python
from decouple import config
import psycopg2

conn = psycopg2.connect(
    dbname=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host=config("DB_HOST"),
    port=config("DB_PORT", cast=int),
)
```

> `.env` ni `.gitignore` ga qo'shishni unutmang.

## 3. SQLAlchemy bilan (30-dars)

SQLite'dan PostgreSQL'ga o'tish uchun asosan **ulanish manzili** o'zgaradi:

```python
from sqlalchemy import create_engine

# SQLite (30-dars)
engine = create_engine("sqlite:///maktab.db")

# PostgreSQL
engine = create_engine("postgresql+psycopg2://ali:mening_parolim@localhost:5432/maktab")
```

**Manzil tuzilishi:**

```
postgresql+psycopg2://FOYDALANUVCHI:PAROL@SERVER:PORT/BAZA_NOMI
```

> ⚠️ Parolda `@`, `/`, `:` kabi maxsus belgilar bo'lsa, ular URL kodlashi (`%40`, `%2F`, `%3A`) kerak bo'ladi. Boshida oddiy harf va raqamli parol ishlatish qulay.

`.env` bilan:

```python
from decouple import config
from sqlalchemy import create_engine

engine = create_engine(config("DATABASE_URL"))
```

```
DATABASE_URL=postgresql+psycopg2://ali:mening_parolim@localhost:5432/maktab
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Eng ko'p uchraydigan muammolar

| Xato / holat | Sababi | Yechim |
|--------------|--------|--------|
| `psql` topilmadi | `bin` papkasi PATH da yo'q | PATH ga qo'shing, terminalni qayta oching |
| `password authentication failed` | Parol yoki foydalanuvchi noto'g'ri | Parolni tekshiring, `ALTER USER ... PASSWORD` bilan yangilang |
| `connection refused` | Server ishlamayapti yoki port noto'g'ri | Xizmat holatini tekshiring (`systemctl status postgresql`, Windows'da Services) |
| `database "x" does not exist` | Baza yaratilmagan yoki nomi xato | `\l` bilan ro'yxatni ko'ring, `CREATE DATABASE` qiling |
| `permission denied for schema public` | Foydalanuvchida sxemaga huquq yo'q | Bazani `OWNER` bilan yarating |
| `5432` port band | Boshqa Postgres nusxasi ishlayapti | Boshqa port tanlang yoki eskisini to'xtating |
| `postgres-#` da qotib qoldi | SQL oxirida `;` qo'yilmagan | `;` yozing va Enter bosing |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔐 Xavfsizlik qoidalari

- `postgres` superuser'ni dasturlaringizda ishlatmang, loyiha uchun **alohida foydalanuvchi** yarating.
- **Kuchli parol** ishlating, uni kodga emas, `.env` ga yozing.
- Parol va `.env` ni **GitHub'ga yuklamang**.
- Serverni internetga ochmang: standart `localhost` dan boshqa joydan ulanish yopiq bo'ladi, bu yaxshi.
- Muhim ma'lumotdan **zaxira nusxa** (backup) oling:

```bash
pg_dump -U ali -d maktab -f zaxira.sql          # zaxira olish
psql -U ali -d maktab -f zaxira.sql             # tiklash
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. PostgreSQL'ni o'z tizimingizga o'rnating va `psql --version` ni tekshiring.
2. `psql` ga `postgres` foydalanuvchisi bilan kiring va `SELECT version();` ni bajaring.
3. `\l`, `\du`, `\conninfo` buyruqlarini sinab ko'ring.
4. O'zingiz uchun foydalanuvchi yarating (`CREATE USER`).
5. `dukon` bazasini shu foydalanuvchi `OWNER` bo'lgan holda yarating.
6. `dukon` bazasiga o'tib (`\c dukon`), `mahsulotlar` jadvalini yarating: `id SERIAL`, `nom`, `narx NUMERIC`, `miqdor`.
7. Jadvalga 5 ta mahsulot qo'shing va `SELECT`, `UPDATE`, `DELETE` ni sinab ko'ring.
8. `\dt` va `\d mahsulotlar` bilan jadval tuzilishini ko'ring.
9. pgAdmin'da serverga ulaning va jadval ma'lumotini oynada ko'ring.
10. `psycopg2` o'rnating va Python'dan bazaga ulanib, mahsulotlarni chiqaring.
11. Ulanish ma'lumotlarini `.env` ga ko'chirib, `python-decouple` bilan o'qing.
12. 30-darsdagi SQLAlchemy modelini PostgreSQL'ga ulab ishga tushiring (`create_all`).
13. `pg_dump` bilan bazadan zaxira nusxa oling.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **PostgreSQL** — kuchli, bepul, mijoz-server arxitekturali relyatsion baza, standart porti `5432`.
- SQLite'dan farqi: alohida server, foydalanuvchilar va huquqlar, ko'p foydalanuvchi bilan ishlash, boy ma'lumot turlari.
- O'rnatishda `postgres` superuser **parolini eslab qoling**.
- `psql` meta-buyruqlari: `\l`, `\c`, `\dt`, `\d`, `\du`, `\q`. SQL buyruq oxirida `;` shart.
- Loyiha uchun alohida **foydalanuvchi** va **baza** yarating: `CREATE USER`, `CREATE DATABASE ... OWNER ...`.
- PostgreSQL'da `id` uchun `SERIAL PRIMARY KEY`, `psycopg2` da qiymat o'rnida `%s` ishlatiladi.
- Python bilan ulanish: `psycopg2` yoki SQLAlchemy (`postgresql+psycopg2://...`).
- Parol va sozlamalarni `.env` da saqlang, `.gitignore` ga qo'shing.
- `pg_dump` bilan zaxira nusxa olib turing.

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