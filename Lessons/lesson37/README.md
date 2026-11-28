<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2037%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 PostgreSQL uchun SQL buyruqlari

**SQL (Structured Query Language)** — relyatsion bazalar bilan ishlash tili. Bu darsda PostgreSQL'da eng ko'p ishlatiladigan uchta amal o'rganiladi:

| Buyruq | Vazifasi | Turi |
|--------|----------|------|
| `CREATE DATABASE` | Yangi **baza** yaratadi | DDL |
| `CREATE TABLE` | Bazada yangi **jadval** yaratadi | DDL |
| `SELECT` | Jadvaldan ma'lumot **o'qiydi** | DQL |

**SQL buyruqlari guruhlari:**

| Guruh | Ma'nosi | Buyruqlar |
|-------|---------|-----------|
| **DDL** | Tuzilmani belgilash (Data Definition) | `CREATE`, `ALTER`, `DROP` |
| **DML** | Ma'lumotni o'zgartirish (Data Manipulation) | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Ma'lumotni o'qish (Data Query) | `SELECT` |
| **DCL** | Huquqlarni boshqarish (Data Control) | `GRANT`, `REVOKE` |

> 💡 SQL buyruqlari **katta-kichik harfga sezgir emas** (`select` = `SELECT`), lekin kalit so'zlarni **katta harfda** yozish odat. Oxirida `;` shart (36-dars).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗄️ 1. `CREATE DATABASE`

**Ta'rif:** yangi ma'lumotlar bazasini yaratadi.

```sql
CREATE DATABASE maktab;
```

**Egasi bilan:**

```sql
CREATE DATABASE maktab OWNER ali;
```

**Qo'shimcha parametrlar bilan:**

```sql
CREATE DATABASE maktab
    OWNER ali
    ENCODING 'UTF8';
```

| Parametr | Ma'nosi |
|----------|---------|
| `OWNER` | Baza egasi (foydalanuvchi) |
| `ENCODING 'UTF8'` | Belgilar kodlashi (o'zbekcha harflar uchun UTF8) |

**Boshqa buyruqlar:**

| Buyruq | Vazifasi |
|--------|----------|
| `\l` | Bazalar ro'yxati (`psql`) |
| `\c maktab` | Bazaga o'tish (`psql`) |
| `ALTER DATABASE eski RENAME TO yangi;` | Bazaning nomini o'zgartiradi |
| `DROP DATABASE maktab;` | Bazani **o'chiradi** |
| `DROP DATABASE IF EXISTS maktab;` | Bor bo'lsa o'chiradi, yo'q bo'lsa xato bermaydi |

> ⚠️ **`CREATE DATABASE IF NOT EXISTS` PostgreSQL'da yo'q** (MySQL'da bor). Baza bor-yo'qligini `\l` bilan tekshiring.

> ⚠️ `CREATE DATABASE` ni **tranzaksiya ichida** bajarib bo'lmaydi. `psql` da muammo yo'q, lekin ba'zi Python kutubxonalarida `autocommit` yoqish kerak bo'ladi.

> 🚨 Ochiq (ulanilgan) bazani o'chirib bo'lmaydi. Avval boshqa bazaga (`\c postgres`) o'ting. `DROP DATABASE` qaytarib bo'lmaydi.

**Tartib:**

```
postgres=# CREATE DATABASE maktab OWNER ali;
CREATE DATABASE
postgres=# \c maktab
You are now connected to database "maktab" as user "postgres".
maktab=#
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 2. `CREATE TABLE`

**Ta'rif:** joriy bazada yangi jadval yaratadi.

**Sintaksis:**

```sql
CREATE TABLE jadval_nomi (
    ustun1 TUR CHEKLOV,
    ustun2 TUR CHEKLOV,
    ...
);
```

**Misol:**

```sql
CREATE TABLE talabalar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50),
    yosh INTEGER CHECK (yosh > 0),
    kurs INTEGER DEFAULT 1,
    ball NUMERIC(5, 2) DEFAULT 0,
    email VARCHAR(100) UNIQUE,
    faol BOOLEAN DEFAULT TRUE,
    tugilgan_sana DATE,
    yaratilgan TIMESTAMP DEFAULT NOW()
);
```

> `IF NOT EXISTS` jadval bor bo'lsa, xato bermaydi: `CREATE TABLE IF NOT EXISTS talabalar (...);`

## Ma'lumot turlari

| Tur | Ma'nosi | Misol |
|-----|---------|-------|
| `SERIAL` | Avtomatik oshuvchi butun son | `id` |
| `INTEGER` | Butun son | `20` |
| `BIGINT` | Katta butun son | `9000000000` |
| `NUMERIC(p, s)` | Aniq kasr son (`p` jami xona, `s` kasr xona) | `NUMERIC(5,2)` → `123.45` |
| `VARCHAR(n)` | Uzunligi `n` gacha matn | `'Ali'` |
| `TEXT` | Cheklanmagan matn | uzun matn |
| `BOOLEAN` | Mantiqiy | `TRUE`, `FALSE` |
| `DATE` | Sana | `'2026-11-27'` |
| `TIME` | Vaqt | `'14:30:00'` |
| `TIMESTAMP` | Sana va vaqt | `'2026-11-27 14:30:00'` |
| `JSONB` | JSON ma'lumot | `'{"a": 1}'` |

## Cheklovlar (constraints)

| Cheklov | Ma'nosi | Misol |
|---------|---------|-------|
| `PRIMARY KEY` | Noyob va bo'sh bo'lmagan identifikator | `id SERIAL PRIMARY KEY` |
| `NOT NULL` | Bo'sh bo'lishi mumkin emas | `ism VARCHAR(50) NOT NULL` |
| `UNIQUE` | Qiymat takrorlanmaydi | `email VARCHAR(100) UNIQUE` |
| `DEFAULT x` | Standart qiymat | `kurs INTEGER DEFAULT 1` |
| `CHECK (shart)` | Qiymat shartga mos bo'lishi kerak | `CHECK (yosh > 0)` |
| `FOREIGN KEY` | Boshqa jadvalga havola | `REFERENCES guruhlar(id)` |

## Jadvallarni bog'lash (`FOREIGN KEY`)

```sql
CREATE TABLE guruhlar (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE oquvchilar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    guruh_id INTEGER REFERENCES guruhlar(id) ON DELETE CASCADE
);
```

| Qism | Ma'nosi |
|------|---------|
| `REFERENCES guruhlar(id)` | `guruh_id` qiymati `guruhlar.id` da mavjud bo'lishi shart |
| `ON DELETE CASCADE` | Guruh o'chsa, unga tegishli o'quvchilar ham o'chadi |
| `ON DELETE SET NULL` | Guruh o'chsa, `guruh_id` `NULL` bo'ladi |

> ⚠️ Avval **havola qilinadigan** jadval (`guruhlar`), keyin havola qiluvchi (`oquvchilar`) yaratiladi.

## Jadval bilan ishlash buyruqlari

| Buyruq | Vazifasi |
|--------|----------|
| `\dt` | Jadvallar ro'yxati (`psql`) |
| `\d talabalar` | Jadval tuzilishi (`psql`) |
| `ALTER TABLE t ADD COLUMN telefon VARCHAR(20);` | Ustun qo'shadi |
| `ALTER TABLE t DROP COLUMN telefon;` | Ustunni o'chiradi |
| `ALTER TABLE t RENAME COLUMN eski TO yangi;` | Ustun nomini o'zgartiradi |
| `ALTER TABLE t RENAME TO yangi_nom;` | Jadval nomini o'zgartiradi |
| `DROP TABLE t;` | Jadvalni **o'chiradi** |
| `DROP TABLE IF EXISTS t;` | Bor bo'lsa o'chiradi |
| `TRUNCATE TABLE t;` | Jadvaldagi barcha qatorni o'chiradi, jadvalning o'zi qoladi |

> 🚨 `DROP TABLE` jadvalni ma'lumotlari bilan birga o'chiradi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ Ma'lumot qo'shish (`SELECT` uchun tayyorgarlik)

`SELECT` ni sinash uchun avval jadvalga ma'lumot kerak:

```sql
INSERT INTO talabalar (ism, familiya, yosh, kurs, ball, email)
VALUES
    ('Ali', 'Valiyev', 20, 2, 85.50, 'ali@mail.com'),
    ('Vali', 'Aliyev', 22, 3, 92.00, 'vali@mail.com'),
    ('Sardor', 'Karimov', 19, 1, 70.00, 'sardor@mail.com'),
    ('Aziz', 'Toshev', 21, 2, 88.50, 'aziz@mail.com'),
    ('Bobur', 'Nazarov', 23, 4, 60.00, NULL),
    ('Anvar', 'Rustamov', 20, 2, 75.25, 'anvar@mail.com');
```

> `id` ni yozmadik: `SERIAL` uni o'zi beradi. Qiymatlar **bitta tirnoq** `' '` ichida yoziladi (ikkita tirnoq `" "` PostgreSQL'da ustun nomi uchun).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📖 3. `SELECT`

**Ta'rif:** jadvaldan ma'lumot o'qiydi.

**Umumiy tuzilish:**

```sql
SELECT ustunlar
FROM jadval
WHERE shart
GROUP BY guruhlash
HAVING guruh_sharti
ORDER BY tartib
LIMIT n OFFSET m;
```

> Bu tartibda yoziladi. Hamma qism majburiy emas, faqat `SELECT` va (odatda) `FROM`.

## Asosiy ko'rinishlar

```sql
SELECT * FROM talabalar;                       -- hamma ustun
SELECT ism, ball FROM talabalar;               -- tanlangan ustunlar
SELECT ism AS "Ismi", ball AS "Bali" FROM talabalar;     -- ustunga laqab (alias)
SELECT DISTINCT kurs FROM talabalar;           -- takrorlanmas qiymatlar
```

> ⚠️ Katta jadvalda `SELECT *` o'rniga kerakli ustunlarni yozing. Bu tezroq ishlaydi.

**Hisoblash va matn birlashtirish:**

```sql
SELECT ism, ball, ball + 5 AS bonusli FROM talabalar;
SELECT ism || ' ' || familiya AS toliq_ism FROM talabalar;
```

`||` — PostgreSQL'da matnlarni birlashtirish operatori.

## `WHERE` — shart

```sql
SELECT * FROM talabalar WHERE kurs = 2;
SELECT * FROM talabalar WHERE ball > 80;
SELECT * FROM talabalar WHERE kurs = 2 AND ball > 80;
SELECT * FROM talabalar WHERE kurs = 1 OR ball > 90;
```

| Operator | Ma'nosi | Misol |
|----------|---------|-------|
| `=` | Teng | `kurs = 2` |
| `<>` yoki `!=` | Teng emas | `kurs <> 2` |
| `>`, `<`, `>=`, `<=` | Taqqoslash | `ball >= 80` |
| `AND` | Va | `kurs = 2 AND ball > 80` |
| `OR` | Yoki | `kurs = 1 OR kurs = 2` |
| `NOT` | Emas | `NOT kurs = 1` |
| `BETWEEN` | Oraliqda (chegaralar kiradi) | `yosh BETWEEN 20 AND 22` |
| `IN` | Ro'yxatda | `kurs IN (1, 2)` |
| `LIKE` | Andoza (katta-kichik harf **farqlanadi**) | `ism LIKE 'A%'` |
| `ILIKE` | Andoza (katta-kichik harf **farqlanmaydi**, faqat PostgreSQL) | `ism ILIKE 'a%'` |
| `IS NULL` | Bo'sh | `email IS NULL` |
| `IS NOT NULL` | Bo'sh emas | `email IS NOT NULL` |

```sql
SELECT * FROM talabalar WHERE yosh BETWEEN 20 AND 22;
SELECT * FROM talabalar WHERE kurs IN (1, 2);
SELECT * FROM talabalar WHERE ism LIKE 'A%';          -- A bilan boshlanadi
SELECT * FROM talabalar WHERE ism ILIKE '%li';        -- "li" bilan tugaydi
SELECT * FROM talabalar WHERE email IS NULL;
```

> 🚨 `NULL` bilan `= NULL` **ishlamaydi**. Doim `IS NULL` yoki `IS NOT NULL` yoziladi.

**`LIKE` belgilari:**

| Belgi | Ma'nosi | Misol | Mos keladi |
|-------|---------|-------|------------|
| `%` | Istalgan miqdordagi belgi | `'A%'` | `Ali`, `Aziz`, `Anvar` |
| `_` | Aynan bitta belgi | `'A_i'` | `Ali` |

## `ORDER BY`, `LIMIT`, `OFFSET`

```sql
SELECT * FROM talabalar ORDER BY ball DESC;                 -- kamayish
SELECT * FROM talabalar ORDER BY kurs ASC, ball DESC;       -- ikki shart
SELECT * FROM talabalar ORDER BY ball DESC LIMIT 3;         -- eng yaxshi 3 ta
SELECT * FROM talabalar ORDER BY id LIMIT 3 OFFSET 3;       -- 4-6 qatorlar (sahifalash)
```

| So'z | Vazifasi |
|------|----------|
| `ASC` | O'sish tartibi (standart) |
| `DESC` | Kamayish tartibi |
| `LIMIT n` | Faqat `n` ta qator |
| `OFFSET m` | Dastlabki `m` ta qatorni o'tkazib yuboradi |

> ⚠️ `ORDER BY` yozilmasa, PostgreSQL qatorlarni **qaysi tartibda qaytarishi kafolatlanmaydi**. Tartib kerak bo'lsa, doim `ORDER BY` yozing.

## Agregat funksiyalar

| Funksiya | Vazifasi |
|----------|----------|
| `COUNT(*)` | Qatorlar soni |
| `COUNT(ustun)` | `NULL` bo'lmagan qiymatlar soni |
| `SUM(ustun)` | Yig'indi |
| `AVG(ustun)` | O'rtacha |
| `MIN(ustun)` | Eng kichik |
| `MAX(ustun)` | Eng katta |

```sql
SELECT COUNT(*) FROM talabalar;                      -- 6
SELECT COUNT(email) FROM talabalar;                  -- 5 (NULL sanalmaydi)
SELECT AVG(ball), MAX(ball), MIN(ball) FROM talabalar;
SELECT ROUND(AVG(ball), 2) AS ortacha FROM talabalar;
```

## `GROUP BY` va `HAVING`

```sql
-- har bir kursda nechta talaba va o'rtacha ball
SELECT kurs, COUNT(*) AS soni, ROUND(AVG(ball), 1) AS ortacha
FROM talabalar
GROUP BY kurs
ORDER BY kurs;
```

**Natija:**

```
 kurs | soni | ortacha
------+------+---------
    1 |    1 |    70.0
    2 |    3 |    83.1
    3 |    1 |    92.0
    4 |    1 |    60.0
```

**`HAVING`** guruhlangan natijani filtrlaydi:

```sql
SELECT kurs, COUNT(*) AS soni
FROM talabalar
GROUP BY kurs
HAVING COUNT(*) > 1;
```

| | `WHERE` | `HAVING` |
|---|---------|----------|
| Qachon ishlaydi | Guruhlashdan **oldin** | Guruhlashdan **keyin** |
| Nimani filtrlaydi | Alohida qatorlarni | Guruhlarni |
| Agregat funksiya | Ishlatib bo'lmaydi | Ishlatish mumkin |

> ⚠️ `GROUP BY` bilan `SELECT` da faqat **guruhlangan ustun** yoki **agregat funksiya** bo'lishi mumkin.

**Bajarilish tartibi (mantiqiy):**

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

## `JOIN` (jadvallarni birlashtirish)

```sql
-- guruhlar va oquvchilar jadvallari (yuqorida yaratilgan)
SELECT o.ism, g.nom AS guruh
FROM oquvchilar o
JOIN guruhlar g ON o.guruh_id = g.id
ORDER BY o.ism;
```

| JOIN turi | Natija |
|-----------|--------|
| `INNER JOIN` (yoki `JOIN`) | Ikkala jadvalda mos kelganlar |
| `LEFT JOIN` | Chap jadvalning hammasi, o'ngda mos kelmasa `NULL` |
| `RIGHT JOIN` | O'ng jadvalning hammasi |

> `o` va `g` — jadval laqablari (alias), yozishni qisqartiradi.

## `CASE` (shartli qiymat)

```sql
SELECT ism, ball,
    CASE
        WHEN ball >= 90 THEN 'A''lo'
        WHEN ball >= 70 THEN 'Yaxshi'
        ELSE 'Qoniqarli'
    END AS baho
FROM talabalar;
```

> Matn ichidagi apostrofni ikkilantirib yoziladi: `'A''lo'` → `A'lo`.

## Sana bilan ishlash

```sql
SELECT NOW();                          -- hozirgi sana va vaqt
SELECT CURRENT_DATE;                   -- bugungi sana
SELECT ism FROM talabalar WHERE yaratilgan > NOW() - INTERVAL '7 days';
SELECT EXTRACT(YEAR FROM tugilgan_sana) AS yil FROM talabalar;
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🐍 Python'dan so'rov yuborish

`psycopg2` bilan (36-dars):

```python
import psycopg2
from decouple import config

conn = psycopg2.connect(
    dbname=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host=config("DB_HOST"),
    port=config("DB_PORT", cast=int),
)

with conn:
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mahsulotlar (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(50) NOT NULL,
                narx NUMERIC(10, 2) NOT NULL
            )
        """)

        cursor.execute(
            "SELECT * FROM talabalar WHERE kurs = %s AND ball > %s",
            (2, 80)
        )

        for qator in cursor.fetchall():
            print(qator)

conn.close()
```

> Qiymatlar `%s` orqali uzatiladi (SQLite'dagi `?` o'rniga). **f-string ishlatmang**, bu SQL Injection xavfini tug'diradi (26-dars).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔁 SQLite va PostgreSQL farqi (qisqacha)

| | SQLite | PostgreSQL |
|---|--------|------------|
| Avto `id` | `INTEGER PRIMARY KEY AUTOINCREMENT` | `SERIAL PRIMARY KEY` |
| Qiymat o'rni (Python) | `?` | `%s` |
| Bazani yaratish | Fayl o'zi yaratiladi | `CREATE DATABASE` |
| Matn birlashtirish | `\|\|` | `\|\|` |
| Katta-kichik harfsiz qidirish | `LIKE` (lotin harflarda) | `ILIKE` |
| Turlar | Erkin | Qat'iy |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol: do'kon bazasi

```sql
-- 1. Baza yaratish (postgres bazasida turib)
CREATE DATABASE dukon OWNER ali;

-- 2. Bazaga o'tish
\c dukon

-- 3. Jadvallar
CREATE TABLE kategoriyalar (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE mahsulotlar (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    narx NUMERIC(12, 2) NOT NULL CHECK (narx >= 0),
    miqdor INTEGER NOT NULL DEFAULT 0,
    kategoriya_id INTEGER REFERENCES kategoriyalar(id)
);

-- 4. Ma'lumot
INSERT INTO kategoriyalar (nom) VALUES ('Oziq-ovqat'), ('Ichimlik');

INSERT INTO mahsulotlar (nom, narx, miqdor, kategoriya_id) VALUES
    ('Non', 4000, 50, 1),
    ('Sut', 12000, 20, 1),
    ('Tuxum', 15000, 30, 1),
    ('Cola', 9000, 40, 2),
    ('Suv', 3000, 100, 2);

-- 5. So'rovlar
SELECT * FROM mahsulotlar ORDER BY narx DESC;

SELECT nom, narx FROM mahsulotlar WHERE narx BETWEEN 5000 AND 12000;

SELECT k.nom AS kategoriya, COUNT(*) AS soni, SUM(m.narx * m.miqdor) AS jami_qiymat
FROM mahsulotlar m
JOIN kategoriyalar k ON m.kategoriya_id = k.id
GROUP BY k.nom
ORDER BY jami_qiymat DESC;
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `psql` da `kutubxona` nomli baza yarating (`CREATE DATABASE`).
2. `\l` bilan bazangiz ro'yxatda borligini tekshiring va `\c kutubxona` bilan unga o'ting.
3. `kitoblar` jadvalini yarating: `id SERIAL`, `nom`, `muallif`, `yil`, `narx NUMERIC(10,2)`, `mavjud BOOLEAN DEFAULT TRUE`.
4. `\d kitoblar` bilan jadval tuzilishini ko'ring.
5. Jadvalga 8 ta kitob qo'shing (`INSERT`).
6. Barcha kitoblarni chiqaring (`SELECT *`).
7. Faqat `nom` va `narx` ustunlarini chiqaring.
8. 2020-yildan keyin chiqqan kitoblarni toping (`WHERE`).
9. Nomida "Python" so'zi bor kitoblarni qidiring (`ILIKE`).
10. Kitoblarni narx bo'yicha kamayish tartibida chiqaring, faqat dastlabki 3 tasini oling.
11. Kitoblar soni va o'rtacha narxini toping (`COUNT`, `AVG`).
12. Muallif bo'yicha kitoblar sonini chiqaring (`GROUP BY`), faqat 2 tadan ko'p kitobi borlarni qoldiring (`HAVING`).
13. `mualliflar` jadvalini yarating, `kitoblar` ni unga `FOREIGN KEY` bilan bog'lang va `JOIN` qiling.
14. `CASE` yordamida kitoblarni "Arzon", "O'rtacha", "Qimmat" toifalarga ajrating.
15. `psycopg2` bilan Python'dan shu jadvalga so'rov yuboring.
16. `ALTER TABLE` bilan jadvalga `sahifalar` ustunini qo'shing, so'ng `DROP COLUMN` bilan o'chiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **`CREATE DATABASE nom OWNER user;`** yangi baza yaratadi. PostgreSQL'da `IF NOT EXISTS` yo'q, ochiq bazani o'chirib bo'lmaydi.
- **`CREATE TABLE`** jadval yaratadi: ustun nomi, **turi** va **cheklovlari** (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY`) yoziladi.
- `id` uchun `SERIAL PRIMARY KEY` ishlatiladi.
- **`SELECT`** ma'lumot o'qiydi: `WHERE` (shart), `ORDER BY` (tartib), `LIMIT/OFFSET` (cheklash), `GROUP BY/HAVING` (guruhlash).
- `NULL` ni `IS NULL` bilan tekshiring, `= NULL` ishlamaydi.
- `ILIKE` katta-kichik harfni farqlamasdan qidiradi (faqat PostgreSQL).
- `ORDER BY` bo'lmasa, qatorlar tartibi kafolatlanmaydi.
- Python'da qiymatlar `%s` orqali uzatiladi, f-string ishlatilmaydi.
- `DROP` va `TRUNCATE` qaytarib bo'lmaydigan buyruqlar, ehtiyot bo'ling.

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