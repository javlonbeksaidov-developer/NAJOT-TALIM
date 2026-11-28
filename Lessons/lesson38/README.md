<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2038%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 `ALTER TABLE` va `DROP TABLE`

Jadval yaratilgandan keyin uning tuzilishini **o'zgartirish** yoki jadvalni **o'chirish** kerak bo'ladi. Buning uchun ikki buyruq ishlatiladi:

| Buyruq | Vazifasi | Guruh |
|--------|----------|-------|
| `ALTER TABLE` | Mavjud jadval **tuzilishini o'zgartiradi** | DDL |
| `DROP TABLE` | Jadvalni **butunlay o'chiradi** | DDL |

> 🚨 Bu buyruqlar jadval tuzilishiga ta'sir qiladi. `DROP TABLE` ma'lumotlarni qaytarib bo'lmaydigan tarzda o'chiradi. Muhim bazada ishlashdan oldin `pg_dump` bilan **zaxira nusxa** oling (36-dars).

**Mashq uchun jadval** (oldingi darslardagi `maktab` yoki `dukon` bazasida):

```sql
CREATE TABLE talabalar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    yosh INTEGER,
    kurs INTEGER DEFAULT 1
);

INSERT INTO talabalar (ism, yosh, kurs) VALUES
    ('Ali', 20, 2),
    ('Vali', 22, 3),
    ('Sardor', 19, 1);
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔧 1. `ALTER TABLE`

**Sintaksis:**

```sql
ALTER TABLE jadval_nomi AMAL;
```

**Asosiy amallar:**

| Amal | Vazifasi |
|------|----------|
| `ADD COLUMN` | Yangi ustun qo'shadi |
| `DROP COLUMN` | Ustunni o'chiradi |
| `RENAME COLUMN` | Ustun nomini o'zgartiradi |
| `ALTER COLUMN ... TYPE` | Ustun turini o'zgartiradi |
| `ALTER COLUMN ... SET/DROP DEFAULT` | Standart qiymatni qo'yadi yoki olib tashlaydi |
| `ALTER COLUMN ... SET/DROP NOT NULL` | `NOT NULL` cheklovini qo'yadi yoki olib tashlaydi |
| `ADD CONSTRAINT` | Cheklov qo'shadi |
| `DROP CONSTRAINT` | Cheklovni o'chiradi |
| `RENAME TO` | Jadval nomini o'zgartiradi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## ➕ Ustun qo'shish: `ADD COLUMN`

```sql
ALTER TABLE talabalar ADD COLUMN telefon VARCHAR(20);
```

**Cheklov va standart qiymat bilan:**

```sql
ALTER TABLE talabalar ADD COLUMN faol BOOLEAN DEFAULT TRUE;
ALTER TABLE talabalar ADD COLUMN email VARCHAR(100) UNIQUE;
```

**Bir nechta ustunni birdan:**

```sql
ALTER TABLE talabalar
    ADD COLUMN manzil VARCHAR(100),
    ADD COLUMN ball NUMERIC(5, 2) DEFAULT 0;
```

**Takroriy xatoning oldini olish:**

```sql
ALTER TABLE talabalar ADD COLUMN IF NOT EXISTS telefon VARCHAR(20);
```

> ⚠️ Jadvalda **ma'lumot bor** bo'lsa, yangi ustun mavjud qatorlarda `NULL` bo'ladi (yoki `DEFAULT` qiymatni oladi). Shuning uchun mavjud jadvalga `NOT NULL` ustun qo'shishda `DEFAULT` ham yozish kerak:
>
> ```sql
> ALTER TABLE talabalar ADD COLUMN guruh VARCHAR(20) NOT NULL DEFAULT 'noma''lum';
> ```
>
> `DEFAULT` siz `NOT NULL` ustun qo'shilsa, jadvalda qator bo'lganda xato chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## ➖ Ustunni o'chirish: `DROP COLUMN`

```sql
ALTER TABLE talabalar DROP COLUMN telefon;
ALTER TABLE talabalar DROP COLUMN IF EXISTS telefon;
```

| Parametr | Ma'nosi |
|----------|---------|
| `IF EXISTS` | Ustun bo'lmasa, xato bermaydi |
| `CASCADE` | Ustunga bog'liq obyektlarni (cheklov, `VIEW`) ham o'chiradi |

```sql
ALTER TABLE talabalar DROP COLUMN kurs CASCADE;
```

> 🚨 Ustun o'chirilsa, undagi **barcha ma'lumot yo'qoladi**. `CASCADE` ni ehtiyotkorlik bilan ishlating.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## ✏️ Nomni o'zgartirish: `RENAME`

**Ustun nomi:**

```sql
ALTER TABLE talabalar RENAME COLUMN ism TO ismi;
```

**Jadval nomi:**

```sql
ALTER TABLE talabalar RENAME TO oquvchilar;
```

> ⚠️ Nom o'zgargach, eski nomni ishlatgan barcha so'rov va Python kodi **ishlamay qoladi**. Ularni ham yangilang. SQLAlchemy modelida `__tablename__` va ustun nomlarini moslashtiring (30-dars).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## 🔄 Ustun turini o'zgartirish: `ALTER COLUMN ... TYPE`

```sql
ALTER TABLE talabalar ALTER COLUMN ism TYPE VARCHAR(100);
ALTER TABLE talabalar ALTER COLUMN yosh TYPE SMALLINT;
```

**Avtomatik o'tmaydigan holatda `USING` yoziladi:**

```sql
-- matn ustunini butun songa aylantirish
ALTER TABLE mahsulotlar
    ALTER COLUMN narx TYPE INTEGER USING narx::INTEGER;
```

| Qism | Ma'nosi |
|------|---------|
| `TYPE yangi_tur` | Yangi ma'lumot turi |
| `USING ifoda` | Eski qiymatni yangi turga qanday o'tkazish |
| `narx::INTEGER` | PostgreSQL'da tur o'zgartirish (`CAST`) |

> ⚠️ Mavjud ma'lumot yangi turga **mos kelmasa** (masalan, `'abc'` ni songa), buyruq xato beradi. Kichikroq turga o'tishda (`VARCHAR(100)` → `VARCHAR(10)`) uzun qiymatlar sig'masa ham xato chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## ⚙️ `DEFAULT` va `NOT NULL`

```sql
-- standart qiymat qo'yish / olib tashlash
ALTER TABLE talabalar ALTER COLUMN kurs SET DEFAULT 1;
ALTER TABLE talabalar ALTER COLUMN kurs DROP DEFAULT;

-- NOT NULL qo'yish / olib tashlash
ALTER TABLE talabalar ALTER COLUMN yosh SET NOT NULL;
ALTER TABLE talabalar ALTER COLUMN yosh DROP NOT NULL;
```

> ⚠️ `SET NOT NULL` ustunda **`NULL` qiymat bor bo'lsa** xato beradi. Avval ularni to'ldiring:
>
> ```sql
> UPDATE talabalar SET yosh = 18 WHERE yosh IS NULL;
> ALTER TABLE talabalar ALTER COLUMN yosh SET NOT NULL;
> ```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## 🔒 Cheklovlar: `ADD` / `DROP CONSTRAINT`

**Cheklov qo'shish:**

```sql
-- UNIQUE
ALTER TABLE talabalar ADD CONSTRAINT talabalar_email_uniq UNIQUE (email);

-- CHECK
ALTER TABLE talabalar ADD CONSTRAINT talabalar_yosh_chk CHECK (yosh > 0);

-- PRIMARY KEY
ALTER TABLE kitoblar ADD PRIMARY KEY (id);

-- FOREIGN KEY
ALTER TABLE oquvchilar
    ADD CONSTRAINT oquvchilar_guruh_fk
    FOREIGN KEY (guruh_id) REFERENCES guruhlar(id) ON DELETE CASCADE;
```

**Cheklovni o'chirish:**

```sql
ALTER TABLE talabalar DROP CONSTRAINT talabalar_yosh_chk;
ALTER TABLE talabalar DROP CONSTRAINT IF EXISTS talabalar_yosh_chk;
```

**Cheklov nomlarini ko'rish:**

```
maktab=> \d talabalar
```

| Cheklov | Qo'shish |
|---------|----------|
| `UNIQUE` | `ADD CONSTRAINT nom UNIQUE (ustun)` |
| `CHECK` | `ADD CONSTRAINT nom CHECK (shart)` |
| `PRIMARY KEY` | `ADD PRIMARY KEY (ustun)` |
| `FOREIGN KEY` | `ADD CONSTRAINT nom FOREIGN KEY (ustun) REFERENCES jadval(ustun)` |

> 💡 Cheklovga **o'zingiz nom bering**. Shunda keyin uni o'chirish oson. Nom bermasangiz, PostgreSQL o'zi nom beradi (`talabalar_yosh_check`).

> ⚠️ Cheklov qo'shilganda **mavjud ma'lumot** unga mos bo'lishi shart, aks holda xato chiqadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## 🧩 Ko'p amalni birdan bajarish

Bir `ALTER TABLE` ichida vergul bilan bir nechta amal yozish mumkin. Ular **birgalikda** bajariladi:

```sql
ALTER TABLE talabalar
    ADD COLUMN telefon VARCHAR(20),
    ALTER COLUMN ism TYPE VARCHAR(100),
    ALTER COLUMN kurs SET DEFAULT 1,
    DROP COLUMN IF EXISTS eski_ustun;
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

## 🧪 Tranzaksiya ichida xavfsiz sinash

PostgreSQL'da `ALTER TABLE` **tranzaksiya ichida** bajarilishi mumkin. Natijadan qoniqmasangiz, `ROLLBACK` bilan hammasini bekor qilasiz (bu SQLite'da bunday emas):

```sql
BEGIN;

ALTER TABLE talabalar DROP COLUMN yosh;
SELECT * FROM talabalar;

ROLLBACK;        -- bekor qilish (yoki COMMIT; bilan tasdiqlash)
```

| Buyruq | Vazifasi |
|--------|----------|
| `BEGIN;` | Tranzaksiyani boshlaydi |
| `COMMIT;` | O'zgarishlarni tasdiqlaydi |
| `ROLLBACK;` | O'zgarishlarni bekor qiladi |

> 💡 Xavfli o'zgarishni avval `BEGIN` ichida sinab ko'rish yaxshi odat.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗑️ 2. `DROP TABLE`

**Ta'rif:** jadvalni **tuzilishi va barcha ma'lumoti bilan** butunlay o'chiradi.

```sql
DROP TABLE talabalar;
```

**Xavfsizroq variantlar:**

```sql
DROP TABLE IF EXISTS talabalar;                 -- yo'q bo'lsa, xato bermaydi
DROP TABLE IF EXISTS talabalar, kitoblar;       -- bir nechta jadval
DROP TABLE talabalar CASCADE;                   -- bog'liq obyektlar bilan
```

| Parametr | Ma'nosi |
|----------|---------|
| `IF EXISTS` | Jadval bo'lmasa, xato o'rniga ogohlantirish beradi |
| `CASCADE` | Jadvalga bog'liq obyektlarni (`FOREIGN KEY` cheklovi, `VIEW`) ham o'chiradi |
| `RESTRICT` | Bog'liq obyekt bo'lsa, o'chirmaydi (**standart xatti-harakat**) |

## Bog'langan jadvalni o'chirish

Boshqa jadval unga `FOREIGN KEY` orqali bog'langan bo'lsa:

```sql
DROP TABLE guruhlar;
```

```
ERROR:  cannot drop table guruhlar because other objects depend on it
DETAIL:  constraint oquvchilar_guruh_id_fkey on table oquvchilar depends on table guruhlar
HINT:  Use DROP ... CASCADE to drop the dependent objects too.
```

**Yechimlar:**

```sql
-- 1-usul: avval bog'langan (bola) jadvalni o'chirish
DROP TABLE oquvchilar;
DROP TABLE guruhlar;

-- 2-usul: CASCADE (faqat cheklovni o'chiradi, oquvchilar jadvali qoladi)
DROP TABLE guruhlar CASCADE;
```

> ⚠️ `CASCADE` bog'liq **jadvalni** emas, faqat unga bog'langan **cheklov va obyektlarni** (masalan, `FOREIGN KEY`, `VIEW`) o'chiradi. `oquvchilar` jadvali o'zi qoladi, lekin `guruhlar` bilan aloqasi uziladi.

> 💡 Qoida: jadvallarni **yaratishda** avval asosiy (`guruhlar`), keyin bog'langan (`oquvchilar`); **o'chirishda** teskari tartibda.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚖️ `DROP TABLE`, `TRUNCATE` va `DELETE` farqi

| | `DELETE FROM t` | `TRUNCATE TABLE t` | `DROP TABLE t` |
|---|-----------------|--------------------|----------------|
| Nimani o'chiradi | Shartga mos qatorlarni (`WHERE`) yoki hammasini | **Barcha qatorlarni** | **Jadvalning o'zini** va ma'lumotini |
| Jadval tuzilishi | Qoladi | Qoladi | **Yo'qoladi** |
| `WHERE` | Ishlaydi | Ishlamaydi | Ishlamaydi |
| Tezlik (katta jadval) | Sekin | Tez | Tez |
| `SERIAL` hisoblagich | Davom etadi | O'z holida (`RESTART IDENTITY` bilan nolga qaytadi) | – |
| Qaytarish (`ROLLBACK`) | Mumkin | Mumkin (tranzaksiya ichida) | Mumkin (tranzaksiya ichida) |

```sql
DELETE FROM talabalar WHERE kurs = 1;          -- faqat 1-kurs
DELETE FROM talabalar;                         -- hamma qator, jadval qoladi

TRUNCATE TABLE talabalar;                      -- hamma qator, tez
TRUNCATE TABLE talabalar RESTART IDENTITY;     -- id ni 1 dan boshlaydi

DROP TABLE talabalar;                          -- jadvalning o'zi ham yo'q
```

> 🚨 Jadval o'chirilgandan keyin `SELECT * FROM talabalar;` xato beradi: `relation "talabalar" does not exist`.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 Amaliy misol: jadvalni bosqichma-bosqich o'zgartirish

```sql
-- 1. Asosiy jadval
CREATE TABLE xodimlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    maosh INTEGER
);

INSERT INTO xodimlar (ism, maosh) VALUES
    ('Ali', 5000000),
    ('Vali', 7000000);

-- 2. Yangi ustunlar qo'shish
ALTER TABLE xodimlar
    ADD COLUMN lavozim VARCHAR(50) DEFAULT 'xodim',
    ADD COLUMN ishga_kirgan DATE DEFAULT CURRENT_DATE;

-- 3. Ustun nomini o'zgartirish
ALTER TABLE xodimlar RENAME COLUMN maosh TO oylik;

-- 4. Turini kengaytirish
ALTER TABLE xodimlar ALTER COLUMN oylik TYPE NUMERIC(12, 2);

-- 5. Cheklov qo'shish
ALTER TABLE xodimlar
    ADD CONSTRAINT xodimlar_oylik_chk CHECK (oylik >= 0);

-- 6. Ortiqcha ustunni o'chirish
ALTER TABLE xodimlar DROP COLUMN ishga_kirgan;

-- 7. Jadval nomini o'zgartirish
ALTER TABLE xodimlar RENAME TO ishchilar;

-- 8. Tekshirish
SELECT * FROM ishchilar;

-- 9. Tozalash
DROP TABLE IF EXISTS ishchilar;
```

> `psql` da har qadamdan keyin `\d ishchilar` bilan jadval tuzilishini ko'rib boring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🐍 Python'dan bajarish

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
        cursor.execute("ALTER TABLE talabalar ADD COLUMN IF NOT EXISTS telefon VARCHAR(20)")
        cursor.execute("DROP TABLE IF EXISTS vaqtincha")

conn.close()
```

> ⚠️ Jadval va ustun **nomlarini** `%s` bilan uzatib bo'lmaydi (`%s` faqat **qiymatlar** uchun). Nom foydalanuvchi kiritgan ma'lumotdan olinadigan bo'lsa, `psycopg2.sql` moduli ishlatiladi, aks holda SQL Injection xavfi bor:

```python
from psycopg2 import sql

jadval = "talabalar"
with conn.cursor() as cursor:
    cursor.execute(
        sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(jadval))
    )
```

> Haqiqiy loyihalarda jadval tuzilishini kod bilan emas, **migratsiya vositasi** (Alembic) orqali o'zgartiriladi. Bu keyingi darslarda ko'riladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Eng ko'p uchraydigan xatolar

| Xato | Sababi | Yechim |
|------|--------|--------|
| `column "x" of relation "t" already exists` | Ustun allaqachon bor | `ADD COLUMN IF NOT EXISTS` |
| `column "x" does not exist` | Ustun nomi xato yoki yo'q | `\d jadval` bilan tekshiring |
| `relation "t" does not exist` | Jadval yo'q (yoki boshqa bazada turibsiz) | `\dt`, `\c baza` |
| `column "x" contains null values` | `SET NOT NULL` da `NULL` bor | Avval `UPDATE` bilan to'ldiring |
| `column "x" contains null values` (`ADD COLUMN ... NOT NULL`) | Mavjud qatorlarga qiymat yo'q | `DEFAULT` qo'shing |
| `cannot drop table ... other objects depend on it` | Boshqa jadval havola qilmoqda | Bola jadvalni oldin o'chiring yoki `CASCADE` |
| `column "x" cannot be cast automatically to type ...` | Tur avtomatik o'tmaydi | `USING ustun::tur` yozing |
| `value too long for type character varying(n)` | Mavjud qiymat yangi uzunlikka sig'maydi | Uzunlikni oshiring |
| `permission denied` / `must be owner of table` | Jadval egasi emassiz | Egasi yoki `postgres` bilan bajaring |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `maktab` bazasida `talabalar` jadvalini yarating va 3 ta qator qo'shing.
2. `ALTER TABLE` bilan `telefon VARCHAR(20)` ustunini qo'shing.
3. Bitta buyruq bilan `manzil` va `email` ustunlarini birdan qo'shing.
4. `faol BOOLEAN DEFAULT TRUE` ustunini qo'shing va mavjud qatorlarda qiymati `TRUE` bo'lganini `SELECT` bilan tekshiring.
5. `ism` ustunining nomini `ismi` ga o'zgartiring, keyin qaytaring.
6. `ism` ustunining turini `VARCHAR(100)` ga o'zgartiring.
7. `yosh` ustuniga `CHECK (yosh > 0)` cheklovini nom berib qo'shing (`ADD CONSTRAINT`).
8. Noto'g'ri qiymat (`yosh = -5`) kiritib ko'ring va xatoni kuzating.
9. Qo'shgan cheklovingizni `DROP CONSTRAINT` bilan o'chiring.
10. `telefon` ustunini `DROP COLUMN IF EXISTS` bilan o'chiring.
11. `BEGIN` ichida ustunni o'chirib, `ROLLBACK` bilan qaytaring, ustun joyida qolganini `\d` bilan tekshiring.
12. Jadval nomini `oquvchilar` ga o'zgartiring.
13. `guruhlar` va `oquvchilar` jadvallarini `FOREIGN KEY` bilan bog'lang. `DROP TABLE guruhlar;` ni bajarib xatoni kuzating, keyin to'g'ri tartibda o'chiring.
14. `DELETE`, `TRUNCATE` va `DROP TABLE` farqini o'zingiz sinab, natijalarni solishtiring.
15. `TRUNCATE ... RESTART IDENTITY` dan keyin yangi qator `id` si 1 dan boshlanishini tekshiring.
16. `psycopg2` bilan Python'dan `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` ni bajaring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **`ALTER TABLE`** mavjud jadval tuzilishini o'zgartiradi: ustun qo'shish (`ADD COLUMN`), o'chirish (`DROP COLUMN`), nom (`RENAME`), tur (`ALTER COLUMN ... TYPE`), cheklovlar (`ADD/DROP CONSTRAINT`).
- Bir `ALTER TABLE` ichida vergul bilan bir nechta amal yozish mumkin.
- Ma'lumot bor jadvalga `NOT NULL` ustun qo'shganda `DEFAULT` kerak, `SET NOT NULL` dan oldin `NULL` larni to'ldiring.
- Tur avtomatik o'tmasa, `USING ustun::tur` yoziladi.
- Cheklovga **o'zingiz nom bering**, shunda uni o'chirish oson bo'ladi.
- **`DROP TABLE`** jadvalni tuzilishi va ma'lumoti bilan o'chiradi. `IF EXISTS` xatoni oldini oladi, `CASCADE` bog'liq cheklov va obyektlarni ham o'chiradi.
- Bog'langan jadvallarni **teskari tartibda** o'chiring: avval bola, keyin ota jadval.
- `DELETE` qatorlarni, `TRUNCATE` hamma qatorni (jadval qoladi), `DROP` jadvalning o'zini o'chiradi.
- PostgreSQL'da DDL buyruqlari **tranzaksiya ichida** bajariladi: `BEGIN` → `ROLLBACK` bilan sinash mumkin.
- Python'da jadval/ustun **nomlari** uchun `%s` ishlamaydi, `psycopg2.sql.Identifier` ishlatiladi.
- Ishlab turgan loyihada o'zgartirishdan oldin **zaxira nusxa** oling.

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