<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2040%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 SELECT va uning imkoniyatlari

Bu darsda `SELECT` buyrug'i va u bilan birga ishlatiladigan asosiy so'zlar o'rganiladi:

| So'z | Vazifasi |
|------|----------|
| `SELECT` | Ma'lumotni o'qish |
| `AS` (alias) | Ustun yoki jadvalga laqab berish |
| `WHERE` | Qatorlarni shart bo'yicha tanlash |
| `ORDER BY` | Natijani tartiblash |
| `LIMIT`, `OFFSET` | Qatorlar sonini cheklash |
| `FETCH` | `LIMIT` ning SQL standartidagi varianti |
| `IN` | Qiymat ro'yxatda bormi |
| `BETWEEN` | Qiymat oraliqda bormi |
| `LIKE`, `ILIKE` | Matnni andoza bo'yicha qidirish |
| `IS NULL` | Bo'sh qiymatni tekshirish |
| `GROUP BY` | Qatorlarni guruhlash |

**Mashq uchun jadval** (`maktab` bazasida):

```sql
CREATE TABLE talabalar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50),
    yosh INTEGER,
    kurs INTEGER,
    ball NUMERIC(5, 2),
    shahar VARCHAR(30),
    email VARCHAR(100)
);

INSERT INTO talabalar (ism, familiya, yosh, kurs, ball, shahar, email) VALUES
    ('Ali', 'Valiyev', 20, 2, 85.50, 'Toshkent', 'ali@mail.com'),
    ('Vali', 'Aliyev', 22, 3, 92.00, 'Samarqand', 'vali@mail.com'),
    ('Sardor', 'Karimov', 19, 1, 70.00, 'Toshkent', 'sardor@mail.com'),
    ('Aziz', 'Toshev', 21, 2, 88.50, 'Buxoro', 'aziz@mail.com'),
    ('Bobur', 'Nazarov', 23, 4, 60.00, 'Samarqand', NULL),
    ('Anvar', 'Rustamov', 20, 2, 75.25, 'Toshkent', 'anvar@mail.com'),
    ('Madina', 'Karimova', 19, 1, 95.00, 'Buxoro', NULL),
    ('Zilola', 'Yusupova', 21, 3, NULL, 'Toshkent', 'zilola@mail.com');
```

> Jadvalda ataylab `NULL` qiymatlar bor (`Bobur` va `Madina` emaili, `Zilola` bali). Ular `IS NULL`, `ORDER BY` va agregat funksiyalarda qanday ishlashini ko'ramiz.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📖 1. `SELECT`

**Ta'rif:** jadvaldan ma'lumot o'qiydi. Jadvalni o'zgartirmaydi.

**Sintaksis:**

```sql
SELECT ustunlar FROM jadval;
```

```sql
SELECT * FROM talabalar;                    -- hamma ustun
SELECT ism, ball FROM talabalar;            -- tanlangan ustunlar
SELECT DISTINCT shahar FROM talabalar;      -- takrorlanmas qiymatlar
SELECT DISTINCT kurs, shahar FROM talabalar;-- takrorlanmas juftliklar
```

**Natija (`SELECT DISTINCT shahar`):**

```
   shahar
-----------
 Toshkent
 Samarqand
 Buxoro
```

> ⚠️ `SELECT *` o'rganish uchun qulay, lekin haqiqiy loyihada kerakli ustunlarni yozing. Bu tezroq ishlaydi va jadval o'zgarsa kod buzilmaydi.

**Jadvalsiz `SELECT`** (hisoblash va funksiyalar uchun):

```sql
SELECT 5 + 3;
SELECT NOW();
SELECT CURRENT_DATE;
SELECT UPPER('salom');
```

**Ustunlar ustida amallar:**

```sql
SELECT ism, ball, ball + 5 FROM talabalar;
SELECT ism, yosh * 12 FROM talabalar;
SELECT ism || ' ' || familiya FROM talabalar;      -- matn birlashtirish
```

**Foydali funksiyalar:**

| Funksiya | Vazifasi | Misol |
|----------|----------|-------|
| `UPPER(s)` / `LOWER(s)` | Katta / kichik harfga | `UPPER(ism)` |
| `LENGTH(s)` | Matn uzunligi | `LENGTH(ism)` |
| `ROUND(x, n)` | Yaxlitlash | `ROUND(ball, 1)` |
| `COALESCE(a, b)` | `a` `NULL` bo'lsa, `b` ni qaytaradi | `COALESCE(ball, 0)` |
| `CONCAT(a, b)` | Matnlarni birlashtirish (`NULL` ni e'tiborsiz qoldiradi) | `CONCAT(ism, ' ', familiya)` |

> 💡 `||` operatorida bitta qiymat `NULL` bo'lsa, butun natija `NULL` bo'ladi. `CONCAT()` esa `NULL` ni bo'sh matn deb hisoblaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏷️ 2. `ALIASES` (laqablar)

**Ta'rif:** ustun yoki jadvalga vaqtinchalik **nom (laqab)** berish. Faqat shu so'rov uchun amal qiladi, jadvalni o'zgartirmaydi.

## Ustun laqabi

```sql
SELECT ism AS talaba_ismi, ball AS baho FROM talabalar;
```

```sql
SELECT ism || ' ' || familiya AS toliq_ism FROM talabalar;
SELECT ism, ball + 5 AS bonusli_ball FROM talabalar;
```

**Natija:**

```
 toliq_ism
-----------------
 Ali Valiyev
 Vali Aliyev
 ...
```

| Yozilishi | Natija |
|-----------|--------|
| `ism AS nom` | Standart usul |
| `ism nom` | `AS` siz ham ishlaydi (tavsiya etilmaydi, o'qish qiyin) |
| `ism AS "Talaba Ismi"` | Probel yoki katta harf kerak bo'lsa, **ikkita tirnoq** |
| `ism AS 'nom'` | ❌ Xato: bitta tirnoq matn uchun |

> ⚠️ PostgreSQL'da laqab **kichik harfga** o'tkaziladi (`AS Nom` → `nom`). Katta harf yoki probel kerak bo'lsa, ikkita tirnoq ishlating: `AS "Nom"`.

## Jadval laqabi

Jadval nomini qisqartirish. `JOIN` da ayniqsa qulay:

```sql
SELECT t.ism, t.ball
FROM talabalar AS t
WHERE t.kurs = 2;

SELECT t.ism FROM talabalar t;       -- AS siz ham mumkin
```

## Laqab qayerda ishlaydi?

| Qism | Laqabni ishlatish mumkinmi? |
|------|------------------------------|
| `ORDER BY` | ✅ Ha |
| `GROUP BY` | ✅ Ha (PostgreSQL'da) |
| `WHERE` | ❌ **Yo'q** |
| `HAVING` | ❌ Yo'q |

```sql
SELECT ism, ball + 5 AS bonusli
FROM talabalar
ORDER BY bonusli DESC;           -- ishlaydi

SELECT ism, ball + 5 AS bonusli
FROM talabalar
WHERE bonusli > 90;              -- ❌ ERROR: column "bonusli" does not exist
```

**To'g'ri yozilishi:**

```sql
-- ifodani qaytadan yozish
SELECT ism, ball + 5 AS bonusli
FROM talabalar
WHERE ball + 5 > 90;

-- yoki subquery orqali
SELECT * FROM (
    SELECT ism, ball + 5 AS bonusli FROM talabalar
) AS t
WHERE bonusli > 90;
```

> Sababi: `WHERE` `SELECT` dan **oldin** bajariladi, shuning uchun laqab hali mavjud emas (bajarilish tartibi pastda).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 3. `WHERE`

**Ta'rif:** faqat **shartga mos** qatorlarni tanlaydi.

```sql
SELECT * FROM talabalar WHERE kurs = 2;
SELECT ism, ball FROM talabalar WHERE ball > 80;
SELECT * FROM talabalar WHERE kurs = 2 AND ball > 80;
SELECT * FROM talabalar WHERE kurs = 1 OR ball > 90;
SELECT * FROM talabalar WHERE NOT kurs = 1;
```

**Natija (`WHERE ball > 80`):**

```
   ism   |  ball
---------+-------
 Ali     | 85.50
 Vali    | 92.00
 Aziz    | 88.50
 Madina  | 95.00
```

> `Zilola` ning bali `NULL`, shuning uchun `ball > 80` shartiga **tushmaydi**. `NULL` bilan har qanday taqqoslash noma'lum natija beradi va qator tanlanmaydi.

**Taqqoslash operatorlari:**

| Operator | Ma'nosi |
|----------|---------|
| `=` | Teng |
| `<>` yoki `!=` | Teng emas |
| `>`, `<`, `>=`, `<=` | Katta, kichik, katta yoki teng, kichik yoki teng |
| `AND` | Ikkala shart ham rost |
| `OR` | Kamida bittasi rost |
| `NOT` | Shartni teskari qiladi |

> ⚠️ Matn qiymati **bitta tirnoqda** yoziladi: `WHERE shahar = 'Toshkent'`. Ikkita tirnoq (`"Toshkent"`) PostgreSQL'da **ustun nomi** hisoblanadi va xato beradi.

> ⚠️ `AND` `OR` dan **oldin** hisoblanadi. Aniq tartib uchun qavs ishlating:
>
> ```sql
> SELECT * FROM talabalar
> WHERE (kurs = 1 OR kurs = 2) AND ball > 80;
> ```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔢 4. `IN`

**Ta'rif:** qiymat **ro'yxatdagi** qiymatlardan biriga teng bo'lsa, `TRUE`. Ko'p `OR` ni almashtiradi.

```sql
SELECT * FROM talabalar WHERE kurs IN (1, 2);
-- bu quyidagiga teng:
SELECT * FROM talabalar WHERE kurs = 1 OR kurs = 2;

SELECT ism, shahar FROM talabalar WHERE shahar IN ('Toshkent', 'Buxoro');
SELECT ism FROM talabalar WHERE kurs NOT IN (1, 2);
```

**Natija (`kurs IN (1, 2)`):**

```
  ism   | kurs
--------+------
 Ali    |    2
 Sardor |    1
 Aziz   |    2
 Anvar  |    2
 Madina |    1
```

**Subquery bilan:**

```sql
SELECT ism FROM talabalar
WHERE kurs IN (SELECT kurs FROM talabalar WHERE ball > 90);
```

> 🚨 **`NOT IN` va `NULL` tuzog'i:** ro'yxatda `NULL` bo'lsa, `NOT IN` **hech qanday qator qaytarmaydi**:
>
> ```sql
> SELECT * FROM talabalar WHERE kurs NOT IN (1, NULL);    -- bo'sh natija!
> ```
>
> Subquery ichida `NULL` bo'lishi mumkin bo'lsa, `NOT EXISTS` ishlating yoki `WHERE ... IS NOT NULL` qo'shing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📏 5. `BETWEEN`

**Ta'rif:** qiymat berilgan **oraliqda** bo'lsa, `TRUE`. **Chegaralar ham kiradi.**

```sql
SELECT ism, yosh FROM talabalar WHERE yosh BETWEEN 20 AND 22;
-- bu quyidagiga teng:
SELECT ism, yosh FROM talabalar WHERE yosh >= 20 AND yosh <= 22;

SELECT ism, yosh FROM talabalar WHERE yosh NOT BETWEEN 20 AND 22;
```

**Natija (`yosh BETWEEN 20 AND 22`):**

```
   ism   | yosh
---------+------
 Ali     |   20
 Vali    |   22
 Aziz    |   21
 Anvar   |   20
 Zilola  |   21
```

| Qoida | Tavsif |
|-------|--------|
| Chegaralar | `20` va `22` ham **kiradi** |
| Tartib | Avval **kichik**, keyin katta qiymat: `BETWEEN 20 AND 22` |
| `BETWEEN 22 AND 20` | Hech narsa qaytarmaydi |
| Turlar | Son, matn, **sana** bilan ishlaydi |

```sql
SELECT * FROM talabalar WHERE ball BETWEEN 70 AND 90;
SELECT * FROM buyurtmalar WHERE sana BETWEEN '2026-01-01' AND '2026-12-31';
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔤 6. `LIKE` va `ILIKE`

**Ta'rif:** matnni **andoza (pattern)** bo'yicha qidiradi.

| Belgi | Ma'nosi |
|-------|---------|
| `%` | Istalgan miqdordagi belgi (hatto hech biri) |
| `_` | Aynan **bitta** belgi |

```sql
SELECT ism FROM talabalar WHERE ism LIKE 'A%';       -- A bilan boshlanadi
SELECT ism FROM talabalar WHERE ism LIKE '%i';       -- i bilan tugaydi
SELECT ism FROM talabalar WHERE ism LIKE '%a%';      -- ichida a bor
SELECT ism FROM talabalar WHERE ism LIKE 'A_i';      -- A, bitta belgi, i
SELECT ism FROM talabalar WHERE ism NOT LIKE 'A%';
```

**Natija (`ism LIKE 'A%'`):**

```
  ism
-------
 Ali
 Aziz
 Anvar
```

| Andoza | Mos keladi |
|--------|------------|
| `'A%'` | `Ali`, `Aziz`, `Anvar` |
| `'%i'` | `Ali`, `Vali` |
| `'A_i'` | `Ali` |
| `'_a%'` | ikkinchi harfi `a`: `Madina`, `Sardor`, `Vali`... |
| `'%'` | hamma matn (`NULL` dan tashqari) |

## `LIKE` va `ILIKE` farqi

| | `LIKE` | `ILIKE` |
|---|--------|---------|
| Katta-kichik harf | **Farqlanadi** | **Farqlanmaydi** |
| Standart SQL | Ha | Yo'q, **faqat PostgreSQL** |

```sql
SELECT ism FROM talabalar WHERE ism LIKE 'a%';       -- hech narsa topilmaydi
SELECT ism FROM talabalar WHERE ism ILIKE 'a%';      -- Ali, Aziz, Anvar
```

> 💡 Foydalanuvchi qidiruvida odatda `ILIKE '%so''z%'` ishlatiladi.

**`%` yoki `_` belgisining o'zini qidirish:**

```sql
SELECT * FROM mahsulotlar WHERE nom LIKE '%100\%%';     -- "100%" matnini qidiradi
```

**Boshqa usullar:**

| Operator | Vazifasi |
|----------|----------|
| `~` | Regulyar ifoda (katta-kichik harf farqlanadi) |
| `~*` | Regulyar ifoda (farqlanmaydi) |
| `SIMILAR TO` | SQL regulyar ifodasi |

> ⚠️ `LIKE '%so''z%'` (boshida `%`) katta jadvalda **sekin** ishlaydi, chunki indeksdan foydalana olmaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⭕ 7. `IS NULL`

**Ta'rif:** `NULL` — "qiymat yo'q / noma'lum" degani. `0` ham, bo'sh matn (`''`) ham emas. `NULL` ni faqat **`IS NULL`** va **`IS NOT NULL`** bilan tekshiriladi.

```sql
SELECT ism, email FROM talabalar WHERE email IS NULL;
SELECT ism, email FROM talabalar WHERE email IS NOT NULL;
```

**Natija (`email IS NULL`):**

```
  ism   | email
--------+-------
 Bobur  |
 Madina |
```

> 🚨 `= NULL` **ishlamaydi**:
>
> ```sql
> SELECT * FROM talabalar WHERE email = NULL;       -- ❌ hech narsa qaytarmaydi
> SELECT * FROM talabalar WHERE email IS NULL;      -- ✅
> ```
>
> Sababi: `NULL` bilan har qanday taqqoslash (`=`, `<>`, `>`) natijasi `NULL` (noma'lum) bo'ladi, `TRUE` emas.

## `NULL` bilan ishlash qoidalari

| Ifoda | Natija |
|-------|--------|
| `NULL = NULL` | `NULL` (rost emas!) |
| `5 + NULL` | `NULL` |
| `'a' \|\| NULL` | `NULL` |
| `NULL AND FALSE` | `FALSE` |
| `NULL OR TRUE` | `TRUE` |

## `COALESCE` — `NULL` o'rniga qiymat

```sql
SELECT ism, COALESCE(ball, 0) AS ball FROM talabalar;
SELECT ism, COALESCE(email, 'email yo''q') AS email FROM talabalar;
```

## `IS DISTINCT FROM` — `NULL` ni hisobga oluvchi taqqoslash

```sql
SELECT * FROM talabalar WHERE email IS DISTINCT FROM 'ali@mail.com';
-- NULL emaillilarni ham qaytaradi (oddiy <> qaytarmasdi)
```

## Agregat funksiyalar va `NULL`

```sql
SELECT COUNT(*), COUNT(ball), COUNT(email) FROM talabalar;
```

```
 count | count | count
-------+-------+-------
     8 |     7 |     6
```

> `COUNT(*)` hamma qatorni, `COUNT(ustun)` esa faqat `NULL` bo'lmagan qiymatlarni sanaydi. `AVG`, `SUM`, `MIN`, `MAX` ham `NULL` larni **o'tkazib yuboradi**.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📶 8. `ORDER BY`

**Ta'rif:** natijani **tartiblaydi**.

```sql
SELECT ism, ball FROM talabalar ORDER BY ball;              -- o'sish (ASC, standart)
SELECT ism, ball FROM talabalar ORDER BY ball DESC;         -- kamayish
SELECT ism, kurs, ball FROM talabalar ORDER BY kurs ASC, ball DESC;   -- ikki shart
```

| So'z | Ma'nosi |
|------|---------|
| `ASC` | Kichikdan kattaga (standart) |
| `DESC` | Kattadan kichikka |

**Qatorlar tartibi:** birinchi ustun bo'yicha, bir xil bo'lsa ikkinchisi bo'yicha.

**Natija (`ORDER BY kurs ASC, ball DESC`):**

```
   ism   | kurs | ball
---------+------+-------
 Madina  |    1 | 95.00
 Sardor  |    1 | 70.00
 Aziz    |    2 | 88.50
 Ali     |    2 | 85.50
 Anvar   |    2 | 75.25
 Vali    |    3 | 92.00
 Zilola  |    3 |
 Bobur   |    4 | 60.00
```

## `NULL` tartibi: `NULLS FIRST` / `NULLS LAST`

PostgreSQL'da `NULL` **eng katta qiymat** hisoblanadi:

| Tartib | `NULL` qayerda |
|--------|----------------|
| `ASC` | Oxirida |
| `DESC` | **Boshida** |

```sql
SELECT ism, ball FROM talabalar ORDER BY ball DESC;                  -- Zilola (NULL) birinchi!
SELECT ism, ball FROM talabalar ORDER BY ball DESC NULLS LAST;       -- NULL oxirida
SELECT ism, ball FROM talabalar ORDER BY ball ASC NULLS FIRST;       -- NULL boshida
```

**Boshqa usullar:**

```sql
SELECT ism, ball FROM talabalar ORDER BY 2 DESC;              -- 2-ustun bo'yicha (tavsiya etilmaydi)
SELECT ism, ball + 5 AS bonusli FROM talabalar ORDER BY bonusli DESC;   -- laqab bo'yicha
SELECT ism FROM talabalar ORDER BY LENGTH(ism), ism;          -- ifoda bo'yicha
```

> ⚠️ `ORDER BY` yozilmasa, qatorlar tartibi **kafolatlanmaydi** (yangilash yoki qo'shishdan keyin o'zgarib ketishi mumkin). Tartib kerak bo'lsa, doim `ORDER BY` yozing. `LIMIT` bilan birga esa **majburiy**.

> 💡 Matnlar tartibi bazaning **locale** sozlamasiga bog'liq. Kirill va o'zbekcha harflar bilan tartiblashda natijani tekshirib ko'ring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✂️ 9. `LIMIT` va `OFFSET`

**Ta'rif:**

| So'z | Vazifasi |
|------|----------|
| `LIMIT n` | Faqat dastlabki `n` ta qatorni qaytaradi |
| `OFFSET m` | Dastlabki `m` ta qatorni **o'tkazib yuboradi** |

```sql
-- eng yuqori ball olgan 3 ta talaba
SELECT ism, ball FROM talabalar
ORDER BY ball DESC NULLS LAST
LIMIT 3;
```

**Natija:**

```
  ism   | ball
--------+-------
 Madina | 95.00
 Vali   | 92.00
 Aziz   | 88.50
```

## Sahifalash (pagination)

```sql
-- 1-sahifa (3 tadan)
SELECT * FROM talabalar ORDER BY id LIMIT 3 OFFSET 0;

-- 2-sahifa
SELECT * FROM talabalar ORDER BY id LIMIT 3 OFFSET 3;

-- 3-sahifa
SELECT * FROM talabalar ORDER BY id LIMIT 3 OFFSET 6;
```

| Formula | |
|---------|--|
| `OFFSET` | `(sahifa - 1) * sahifa_hajmi` |
| `LIMIT` | `sahifa_hajmi` |

```sql
SELECT * FROM talabalar ORDER BY id LIMIT 1;            -- birinchi qator
SELECT * FROM talabalar ORDER BY id DESC LIMIT 1;       -- oxirgi qo'shilgan
```

> ⚠️ `LIMIT` ni `ORDER BY` siz ishlatsangiz, qaysi qatorlar qaytishi **noaniq**.

> 💡 Juda katta `OFFSET` (masalan, 1 000 000) sekin ishlaydi, chunki baza o'tkazib yuboriladigan qatorlarni ham o'qiydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎯 10. `FETCH`

**Ta'rif:** `LIMIT` bilan bir xil ishlaydigan, **SQL standartidagi** variant. PostgreSQL ikkalasini ham qo'llab-quvvatlaydi.

**Sintaksis:**

```sql
OFFSET m ROWS
FETCH FIRST n ROWS ONLY;
```

```sql
SELECT ism, ball FROM talabalar
ORDER BY ball DESC NULLS LAST
FETCH FIRST 3 ROWS ONLY;
```

**Sahifalash:**

```sql
SELECT * FROM talabalar
ORDER BY id
OFFSET 3 ROWS
FETCH NEXT 3 ROWS ONLY;
```

| Qism | Ma'nosi |
|------|---------|
| `FIRST` va `NEXT` | Bir xil ma'noda (o'qilishi uchun farq) |
| `ROW` va `ROWS` | Bir xil ma'noda (`FETCH FIRST 1 ROW ONLY`) |
| `ONLY` | Aynan `n` ta qator |
| `WITH TIES` | `n` - qatordagi qiymat bilan **teng** qatorlarni ham qo'shadi |

## `WITH TIES`

`ORDER BY` bilan birga ishlatiladi. Oxirgi qatorga teng qiymatli qatorlar ham qaytariladi:

```sql
SELECT ism, kurs FROM talabalar
ORDER BY kurs
FETCH FIRST 1 ROWS WITH TIES;
```

**Natija** (1 ta so'raldi, lekin 1-kursda 2 ta talaba bor):

```
  ism   | kurs
--------+------
 Sardor |    1
 Madina |    1
```

## `LIMIT` va `FETCH` solishtirish

| | `LIMIT / OFFSET` | `FETCH` |
|---|------------------|---------|
| Standart | PostgreSQL, MySQL, SQLite | **SQL standarti** (Oracle, SQL Server, PostgreSQL) |
| Yozilishi | `LIMIT 3 OFFSET 3` | `OFFSET 3 ROWS FETCH NEXT 3 ROWS ONLY` |
| `WITH TIES` | Yo'q | **Bor** |
| Ko'proq ishlatiladi | **Ha** | Kamroq |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗂️ 11. `GROUP BY`

**Ta'rif:** bir xil qiymatli qatorlarni **guruhlarga** ajratadi. Odatda **agregat funksiyalar** bilan ishlatiladi.

**Agregat funksiyalar:**

| Funksiya | Vazifasi |
|----------|----------|
| `COUNT(*)` | Qatorlar soni |
| `SUM(x)` | Yig'indi |
| `AVG(x)` | O'rtacha |
| `MIN(x)` | Eng kichik |
| `MAX(x)` | Eng katta |
| `STRING_AGG(x, ', ')` | Qiymatlarni bitta matnga birlashtiradi |

```sql
SELECT COUNT(*), ROUND(AVG(ball), 2), MAX(ball), MIN(ball) FROM talabalar;
```

**`GROUP BY` bilan:**

```sql
-- har bir shaharda nechta talaba
SELECT shahar, COUNT(*) AS soni
FROM talabalar
GROUP BY shahar
ORDER BY shahar;
```

**Natija:**

```
  shahar   | soni
-----------+------
 Buxoro    |    2
 Samarqand |    2
 Toshkent  |    4
```

**Bir nechta agregat bilan:**

```sql
SELECT shahar,
       COUNT(*) AS soni,
       ROUND(AVG(ball), 2) AS ortacha,
       MAX(ball) AS eng_yuqori
FROM talabalar
GROUP BY shahar
ORDER BY ortacha DESC;
```

**Natija:**

```
  shahar   | soni | ortacha | eng_yuqori
-----------+------+---------+------------
 Buxoro    |    2 |   91.75 |      95.00
 Toshkent  |    4 |   76.92 |      85.50
 Samarqand |    2 |   76.00 |      92.00
```

> `Toshkent` da 4 talaba bor, lekin `Zilola` ning bali `NULL`, shuning uchun o'rtacha **3 ta** qiymat bo'yicha hisoblandi.

**Ismlarni birlashtirish (`STRING_AGG`):**

```sql
SELECT shahar, STRING_AGG(ism, ', ' ORDER BY ism) AS talabalar
FROM talabalar
GROUP BY shahar
ORDER BY shahar;
```

```
  shahar   |        talabalar
-----------+--------------------------
 Buxoro    | Aziz, Madina
 Samarqand | Bobur, Vali
 Toshkent  | Ali, Anvar, Sardor, Zilola
```

## Bir nechta ustun bo'yicha guruhlash

```sql
SELECT shahar, kurs, COUNT(*) AS soni
FROM talabalar
GROUP BY shahar, kurs
ORDER BY shahar, kurs;
```

## `HAVING` — guruhlarni filtrlash

```sql
SELECT kurs, COUNT(*) AS soni
FROM talabalar
GROUP BY kurs
HAVING COUNT(*) > 1
ORDER BY kurs;
```

**Natija:**

```
 kurs | soni
------+------
    1 |    2
    2 |    3
    3 |    2
```

| | `WHERE` | `HAVING` |
|---|---------|----------|
| Qachon ishlaydi | Guruhlashdan **oldin** | Guruhlashdan **keyin** |
| Nimani filtrlaydi | Alohida qatorlarni | Guruhlarni |
| Agregat funksiya | ❌ Ishlatib bo'lmaydi | ✅ Ishlatiladi |

```sql
-- 80 dan yuqori ball olganlar orasida shahar bo'yicha sanash (WHERE avval)
SELECT shahar, COUNT(*) AS soni
FROM talabalar
WHERE ball > 80
GROUP BY shahar
HAVING COUNT(*) >= 2;
```

## Eng ko'p uchraydigan xato

```sql
SELECT shahar, ism, COUNT(*) FROM talabalar GROUP BY shahar;
```

```
ERROR:  column "talabalar.ism" must appear in the GROUP BY clause or be used in an aggregate function
```

> 🚨 `GROUP BY` bilan `SELECT` da faqat **guruhlangan ustun** yoki **agregat funksiya** bo'lishi mumkin. `ism` ga har bir guruhda bir nechta qiymat bor, baza qaysi birini ko'rsatishni bilmaydi.

**Yechim:** `ism` ni `GROUP BY` ga qo'shing yoki `STRING_AGG(ism, ', ')` kabi agregat ishlating.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 SQL bajarilish tartibi

Yozilish tartibi va **bajarilish tartibi** boshqa-boshqa. Shu sababli laqab `WHERE` da ishlamaydi, lekin `ORDER BY` da ishlaydi.

| Yozilish tartibi | Bajarilish tartibi |
|------------------|--------------------|
| 1. `SELECT` | 5. `SELECT` (laqablar shu yerda paydo bo'ladi) |
| 2. `FROM` | 1. `FROM` |
| 3. `WHERE` | 2. `WHERE` |
| 4. `GROUP BY` | 3. `GROUP BY` |
| 5. `HAVING` | 4. `HAVING` |
| 6. `ORDER BY` | 6. `ORDER BY` |
| 7. `LIMIT / FETCH` | 7. `LIMIT / FETCH` |

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**Hammasi birga:**

```sql
SELECT shahar,
       COUNT(*) AS soni,
       ROUND(AVG(ball), 1) AS ortacha
FROM talabalar
WHERE yosh BETWEEN 19 AND 23
  AND ism ILIKE '%a%'
  AND email IS NOT NULL
GROUP BY shahar
HAVING COUNT(*) >= 1
ORDER BY ortacha DESC NULLS LAST
LIMIT 2;
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🐍 Python'dan so'rov yuborish

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
        # WHERE + BETWEEN
        cursor.execute(
            "SELECT ism, yosh FROM talabalar WHERE yosh BETWEEN %s AND %s ORDER BY yosh",
            (20, 22)
        )
        print(cursor.fetchall())

        # LIKE: % belgisi qiymatning ichida
        soz = "a"
        cursor.execute(
            "SELECT ism FROM talabalar WHERE ism ILIKE %s",
            (f"%{soz}%",)
        )
        print(cursor.fetchall())

        # IN: ro'yxatni ANY(%s) bilan uzatish
        kurslar = [1, 2]
        cursor.execute(
            "SELECT ism, kurs FROM talabalar WHERE kurs = ANY(%s)",
            (kurslar,)
        )
        print(cursor.fetchall())

        # GROUP BY
        cursor.execute("""
            SELECT shahar, COUNT(*), ROUND(AVG(ball), 2)
            FROM talabalar
            GROUP BY shahar
            ORDER BY shahar
        """)
        for shahar, soni, ortacha in cursor.fetchall():
            print(f"{shahar}: {soni} ta, o'rtacha {ortacha}")

        # Sahifalash
        sahifa, hajm = 2, 3
        cursor.execute(
            "SELECT id, ism FROM talabalar ORDER BY id LIMIT %s OFFSET %s",
            (hajm, (sahifa - 1) * hajm)
        )
        print(cursor.fetchall())

conn.close()
```

| Holat | Qanday |
|-------|--------|
| Qiymat uzatish | `%s` (f-string emas, SQL Injection!) |
| `LIKE` andozasi | `%` ni **qiymat ichiga** yozing: `(f"%{soz}%",)` |
| `IN` ro'yxati | `= ANY(%s)` va Python ro'yxati |
| Bitta qiymat | Kortej: `(qiymat,)` (vergul shart) |
| `NULL` | `IS NULL` so'rov ichida yoziladi |

> Pastdagi `fetchall()` natijada kortejlar ro'yxati qaytaradi. Qiymat turlari: `NUMERIC` ustuni Python'da `Decimal` bo'lib keladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Eng ko'p uchraydigan xatolar

| Xato / holat | Sababi | Yechim |
|--------------|--------|--------|
| `column "Toshkent" does not exist` | Matn ikkita tirnoqda yozilgan | Bitta tirnoq: `'Toshkent'` |
| `column "bonusli" does not exist` (`WHERE` da) | Laqab `WHERE` da ishlamaydi | Ifodani qaytadan yozing yoki subquery |
| `= NULL` hech narsa qaytarmaydi | `NULL` taqqoslanmaydi | `IS NULL` |
| `NOT IN` bo'sh natija beradi | Ro'yxatda `NULL` bor | `NOT EXISTS` yoki `IS NOT NULL` filtri |
| `must appear in the GROUP BY clause` | `SELECT` da guruhlanmagan ustun | `GROUP BY` ga qo'shing yoki agregat ishlating |
| `aggregate functions are not allowed in WHERE` | `WHERE` da `COUNT()` | `HAVING` ishlating |
| `LIKE 'a%'` topmayapti | `LIKE` katta-kichik harfni farqlaydi | `ILIKE` |
| `LIMIT` da natija har xil | `ORDER BY` yo'q | `ORDER BY` qo'shing |
| `DESC` da `NULL` birinchi chiqdi | PostgreSQL'da `NULL` eng katta | `NULLS LAST` |
| `BETWEEN 30 AND 20` bo'sh | Chegaralar teskari | Avval kichigi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Yuqoridagi `talabalar` jadvalini yarating va ma'lumotni qo'shing.
2. Faqat `ism` va `familiya` ustunlarini chiqaring.
3. `ism` va `familiya` ni birlashtirib, `toliq_ism` laqabi bilan chiqaring.
4. Har bir talabaning `ball` iga 10% qo'shib, `yangi_ball` laqabi bilan chiqaring (`ball * 1.1`).
5. Takrorlanmas shaharlar ro'yxatini chiqaring (`DISTINCT`).
6. Bali 80 dan yuqori talabalarni toping (`WHERE`).
7. Toshkentlik va 2-kursdan yuqori talabalarni toping (`AND`).
8. 1-kurs yoki 4-kurs talabalarini `IN` bilan toping.
9. Yoshi 20 va 22 oralig'idagilarni `BETWEEN` bilan toping, keyin `NOT BETWEEN` bilan teskarisini.
10. Ismi `A` bilan boshlanadiganlarni toping (`LIKE`).
11. Familiyasi `ova` bilan tugaydiganlarni toping.
12. Ismida `a` harfi bor talabalarni `ILIKE` bilan toping, `LIKE` bilan natijani solishtiring.
13. Emaili yo'q talabalarni toping (`IS NULL`), keyin emaili borlarini (`IS NOT NULL`).
14. `COALESCE` yordamida bali `NULL` bo'lganlarga `0` ko'rsating.
15. Talabalarni ball bo'yicha kamayish tartibida chiqaring. `NULL` oxirida bo'lsin (`NULLS LAST`).
16. Avval kurs bo'yicha o'sish, keyin ball bo'yicha kamayish tartibida chiqaring.
17. Eng yuqori ball olgan 3 talabani `LIMIT` bilan chiqaring.
18. Xuddi shu so'rovni `FETCH FIRST 3 ROWS ONLY` bilan yozing.
19. 2-sahifani chiqaring (sahifa hajmi 3) `LIMIT` va `OFFSET` bilan.
20. `FETCH ... WITH TIES` ni sinab, oddiy `ONLY` bilan farqini ko'ring.
21. Har bir kursda nechta talaba borligini toping (`GROUP BY`).
22. Har bir shahar uchun talabalar soni, o'rtacha, eng yuqori va eng past ballni chiqaring.
23. Faqat 2 tadan ko'p talabasi bor shaharlarni qoldiring (`HAVING`).
24. `GROUP BY` da `SELECT` ga guruhlanmagan ustun yozib, xatoni kuzating.
25. `WHERE` da laqabdan foydalanib, xatoni kuzating va to'g'rilang.
26. `COUNT(*)`, `COUNT(ball)`, `COUNT(email)` natijalarini solishtiring va farqini tushuntiring.
27. `psycopg2` bilan Python'dan 3 ta so'rov yuboring: `BETWEEN`, `ILIKE` va `= ANY(%s)`.
28. Foydalanuvchidan sahifa raqamini so'rab, shu sahifadagi talabalarni chiqaruvchi dastur yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **`SELECT`** ma'lumot o'qiydi: `*`, tanlangan ustunlar, hisoblashlar, `DISTINCT`.
- **Alias** (`AS`) ustun yoki jadvalga laqab beradi. Matn ichida probel yoki katta harf kerak bo'lsa, **ikkita tirnoq** ishlating. Laqab `ORDER BY` va `GROUP BY` da ishlaydi, `WHERE` da **ishlamaydi**.
- **`WHERE`** qatorlarni shart bo'yicha tanlaydi. Matn qiymati **bitta tirnoqda**, `AND` `OR` dan oldin hisoblanadi.
- **`IN`** ro'yxatdagi qiymatlarni tekshiradi, `NOT IN` da `NULL` bo'lsa natija bo'sh chiqadi.
- **`BETWEEN a AND b`** chegaralarni **kiritgan** holda oraliqni tekshiradi, avval kichik qiymat yoziladi.
- **`LIKE`** andoza bo'yicha qidiradi (`%` va `_`), **`ILIKE`** katta-kichik harfni farqlamaydi (faqat PostgreSQL).
- **`NULL`** ni faqat `IS NULL` / `IS NOT NULL` bilan tekshiring, `= NULL` ishlamaydi. `COALESCE` `NULL` o'rniga qiymat beradi.
- **`ORDER BY`** tartiblaydi (`ASC`, `DESC`). PostgreSQL'da `NULL` eng katta qiymat, `NULLS FIRST/LAST` bilan boshqariladi.
- **`LIMIT / OFFSET`** va **`FETCH FIRST n ROWS ONLY`** qatorlarni cheklaydi. Doim `ORDER BY` bilan ishlating.
- **`GROUP BY`** guruhlaydi, `SELECT` da faqat guruhlangan ustun yoki agregat funksiya bo'ladi. **`HAVING`** guruhlarni filtrlaydi.
- Bajarilish tartibi: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.
- Python'da qiymatlar `%s` orqali uzatiladi, `IN` o'rniga `= ANY(%s)` ishlatiladi.

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