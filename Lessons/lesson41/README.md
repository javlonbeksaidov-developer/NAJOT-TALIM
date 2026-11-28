<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2041%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 JOIN: jadvallarni birlashtirish

Relyatsion bazada ma'lumot odatda **bir nechta jadvalga** bo'lib saqlanadi (masalan, talabalar alohida, guruhlar alohida). **`JOIN`** ularni umumiy ustun (odatda `FOREIGN KEY`) orqali **bitta natijaga** birlashtiradi.

| JOIN turi | Natija |
|-----------|--------|
| `INNER JOIN` | Ikkala jadvalda **mos kelgan** qatorlar |
| `LEFT JOIN` | **Chap** jadvalning hamma qatori + o'ngdan mosi (yo'q bo'lsa `NULL`) |
| `RIGHT JOIN` | **O'ng** jadvalning hamma qatori + chapdan mosi (yo'q bo'lsa `NULL`) |
| `FULL JOIN` | **Ikkala** jadvalning hamma qatori |
| `SELF JOIN` | Jadvalning **o'zi** bilan birlashtirish |
| `CROSS JOIN` | Har bir qator har bir qator bilan (**dekart ko'paytma**) |
| `NATURAL JOIN` | Nomi bir xil ustunlar bo'yicha **avtomatik** birlashtirish |

**Mashq jadvallari** (`maktab` bazasida):

```sql
DROP TABLE IF EXISTS baholar, talabalar, guruhlar;

CREATE TABLE guruhlar (
    guruh_id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL
);

CREATE TABLE talabalar (
    talaba_id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    guruh_id INTEGER REFERENCES guruhlar(guruh_id) ON DELETE SET NULL
);

CREATE TABLE baholar (
    baho_id SERIAL PRIMARY KEY,
    talaba_id INTEGER REFERENCES talabalar(talaba_id),
    fan VARCHAR(30),
    ball INTEGER
);

INSERT INTO guruhlar (nom) VALUES ('PY-12'), ('JS-05'), ('UI-03');

INSERT INTO talabalar (ism, guruh_id) VALUES
    ('Ali', 1),
    ('Vali', 1),
    ('Sardor', 2),
    ('Aziz', NULL),
    ('Bobur', 2);

INSERT INTO baholar (talaba_id, fan, ball) VALUES
    (1, 'Python', 90),
    (1, 'SQL', 80),
    (2, 'Python', 70),
    (3, 'JS', 85);
```

**Jadvallar mazmuni:**

`guruhlar`:

| guruh_id | nom |
|----------|-----|
| 1 | PY-12 |
| 2 | JS-05 |
| 3 | UI-03 |

`talabalar`:

| talaba_id | ism | guruh_id |
|-----------|-----|----------|
| 1 | Ali | 1 |
| 2 | Vali | 1 |
| 3 | Sardor | 2 |
| 4 | Aziz | `NULL` |
| 5 | Bobur | 2 |

> 💡 Ma'lumot ataylab shunday tanlangan: **Aziz** hech qaysi guruhda emas (`NULL`), **UI-03** guruhida esa talaba yo'q. Turli JOIN lar ularni qanday ko'rsatishini kuzating.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 JOIN sintaksisi

```sql
SELECT ustunlar
FROM jadval1
JOIN_TURI jadval2 ON jadval1.ustun = jadval2.ustun;
```

| Qism | Ma'nosi |
|------|---------|
| `ON` | Qatorlar **qanday moslashishi** sharti |
| `USING (ustun)` | Ikkala jadvalda **nomi bir xil** ustun bo'lsa, `ON` ning qisqa yozuvi |
| Jadval laqabi | `talabalar t`, `guruhlar g`: yozishni qisqartiradi (40-dars) |

> ⚠️ Ikkala jadvalda bir xil nomli ustun bo'lsa, `SELECT guruh_id` xato beradi (`column reference "guruh_id" is ambiguous`). Jadval laqabi bilan yozing: `t.guruh_id`.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 1️⃣ `INNER JOIN`

**Ta'rif:** faqat **ikkala jadvalda mos kelgan** qatorlarni qaytaradi. Mos kelmaganlar natijaga tushmaydi. Eng ko'p ishlatiladigan JOIN.

```sql
SELECT t.talaba_id, t.ism, g.nom AS guruh
FROM talabalar t
INNER JOIN guruhlar g ON t.guruh_id = g.guruh_id
ORDER BY t.talaba_id;
```

**Natija:**

```
 talaba_id |  ism   | guruh
-----------+--------+-------
         1 | Ali    | PY-12
         2 | Vali   | PY-12
         3 | Sardor | JS-05
         5 | Bobur  | JS-05
```

> **Aziz** (guruhi `NULL`) va **UI-03** (talabasi yo'q) natijada **yo'q**, chunki ularning mosi topilmadi.

**Qisqa yozuv:** `JOIN` yozilsa, bu `INNER JOIN` degani.

```sql
SELECT t.ism, g.nom
FROM talabalar t
JOIN guruhlar g ON t.guruh_id = g.guruh_id;

-- USING bilan (ustun nomi ikkala jadvalda bir xil)
SELECT ism, nom
FROM talabalar
JOIN guruhlar USING (guruh_id);
```

## Uch va undan ko'p jadvalni bog'lash

```sql
SELECT t.ism, g.nom AS guruh, b.fan, b.ball
FROM talabalar t
JOIN guruhlar g ON t.guruh_id = g.guruh_id
JOIN baholar b ON b.talaba_id = t.talaba_id
ORDER BY t.talaba_id, b.baho_id;
```

**Natija:**

```
  ism   | guruh |  fan   | ball
--------+-------+--------+------
 Ali    | PY-12 | Python |   90
 Ali    | PY-12 | SQL    |   80
 Vali   | PY-12 | Python |   70
 Sardor | JS-05 | JS     |   85
```

> JOIN lar ketma-ket yoziladi: har biri oldingi natijaga yangi jadval qo'shadi. Ali ikkita bahosi bor, shuning uchun 2 qatorda chiqdi.

## `WHERE`, `GROUP BY`, `ORDER BY` bilan

```sql
-- PY-12 guruhidagi talabalarning o'rtacha bali
SELECT g.nom, ROUND(AVG(b.ball), 1) AS ortacha
FROM guruhlar g
JOIN talabalar t ON t.guruh_id = g.guruh_id
JOIN baholar b ON b.talaba_id = t.talaba_id
WHERE g.nom = 'PY-12'
GROUP BY g.nom;
```

```
  nom  | ortacha
-------+---------
 PY-12 |    80.0
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 2️⃣ `LEFT JOIN`

**Ta'rif:** **chap** (`FROM` dagi) jadvalning **hamma qatorini** qaytaradi. O'ngda mosi bo'lmasa, o'ng jadval ustunlari `NULL` bo'ladi. To'liq nomi `LEFT OUTER JOIN`.

```sql
SELECT t.talaba_id, t.ism, g.nom AS guruh
FROM talabalar t
LEFT JOIN guruhlar g ON t.guruh_id = g.guruh_id
ORDER BY t.talaba_id;
```

**Natija:**

```
 talaba_id |  ism   | guruh
-----------+--------+-------
         1 | Ali    | PY-12
         2 | Vali   | PY-12
         3 | Sardor | JS-05
         4 | Aziz   |
         5 | Bobur  | JS-05
```

> **Aziz** endi natijada bor, guruhi esa `NULL`.

## Mosi yo'q qatorlarni topish (anti-join)

`LEFT JOIN` + `IS NULL` bilan "**biror joyda yo'q**" qatorlarni topiladi:

```sql
-- guruhi yo'q talabalar
SELECT t.ism
FROM talabalar t
LEFT JOIN guruhlar g ON t.guruh_id = g.guruh_id
WHERE g.guruh_id IS NULL;
```

```
  ism
------
 Aziz
```

```sql
-- bahosi yo'q talabalar
SELECT t.ism
FROM talabalar t
LEFT JOIN baholar b ON b.talaba_id = t.talaba_id
WHERE b.baho_id IS NULL;
```

```
  ism
-------
 Aziz
 Bobur
```

## `LEFT JOIN` va agregat funksiyalar

```sql
-- har bir talabaning baholari soni (bahosizlar uchun 0)
SELECT t.ism, COUNT(b.baho_id) AS baholar_soni
FROM talabalar t
LEFT JOIN baholar b ON b.talaba_id = t.talaba_id
GROUP BY t.talaba_id, t.ism
ORDER BY t.talaba_id;
```

```
  ism   | baholar_soni
--------+--------------
 Ali    |            2
 Vali   |            1
 Sardor |            1
 Aziz   |            0
 Bobur  |            0
```

> ⚠️ `COUNT(*)` emas, **`COUNT(b.baho_id)`** yozing. `COUNT(*)` `NULL` qatorni ham sanab, bahosizlarga ham `1` beradi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 3️⃣ `RIGHT JOIN`

**Ta'rif:** **o'ng** (`JOIN` dan keyingi) jadvalning **hamma qatorini** qaytaradi. Chapda mosi bo'lmasa, chap jadval ustunlari `NULL` bo'ladi. To'liq nomi `RIGHT OUTER JOIN`.

```sql
SELECT g.nom AS guruh, t.ism
FROM talabalar t
RIGHT JOIN guruhlar g ON t.guruh_id = g.guruh_id
ORDER BY g.guruh_id, t.talaba_id;
```

**Natija:**

```
 guruh |  ism
-------+--------
 PY-12 | Ali
 PY-12 | Vali
 JS-05 | Sardor
 JS-05 | Bobur
 UI-03 |
```

> **UI-03** guruhida talaba yo'q, lekin guruh natijada bor. **Aziz** esa yo'q, chunki u chap jadvalda, uning mosi esa o'ngda topilmadi.

**Guruhlari bo'sh (talabasi yo'q) guruhlarni topish:**

```sql
SELECT g.nom
FROM talabalar t
RIGHT JOIN guruhlar g ON t.guruh_id = g.guruh_id
WHERE t.talaba_id IS NULL;
```

```
  nom
-------
 UI-03
```

> 💡 `RIGHT JOIN` ni jadvallar o'rnini almashtirib, `LEFT JOIN` bilan har doim yozish mumkin. Shuning uchun amalda **`LEFT JOIN` ko'proq** ishlatiladi (o'qish osonroq):
>
> ```sql
> SELECT g.nom, t.ism
> FROM guruhlar g
> LEFT JOIN talabalar t ON t.guruh_id = g.guruh_id;
> ```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 4️⃣ `FULL JOIN`

**Ta'rif:** **ikkala** jadvalning hamma qatorini qaytaradi. Mos kelgani birlashtiriladi, mosi yo'q tomon `NULL` bo'ladi. To'liq nomi `FULL OUTER JOIN`.

```sql
SELECT t.ism, g.nom AS guruh
FROM talabalar t
FULL JOIN guruhlar g ON t.guruh_id = g.guruh_id
ORDER BY g.guruh_id, t.talaba_id;
```

**Natija:**

```
  ism   | guruh
--------+-------
 Ali    | PY-12
 Vali   | PY-12
 Sardor | JS-05
 Bobur  | JS-05
        | UI-03
 Aziz   |
```

> Ham **Aziz** (guruhsiz), ham **UI-03** (talabasiz) natijada bor. `NULL` lar `ORDER BY` da oxirida turadi.

**Faqat mos kelmaganlarni topish** (har ikki tomondan):

```sql
SELECT t.ism, g.nom
FROM talabalar t
FULL JOIN guruhlar g ON t.guruh_id = g.guruh_id
WHERE t.talaba_id IS NULL OR g.guruh_id IS NULL;
```

```
 ism  |  nom
------+-------
 Aziz |
      | UI-03
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪞 5️⃣ `SELF JOIN`

**Ta'rif:** jadvalning **o'zini o'zi bilan** birlashtirish. Alohida buyruq emas, oddiy JOIN, faqat bitta jadval **ikki xil laqab** bilan ishlatiladi.

Odatda **ierarxiya** (xodim va uning rahbari) yoki **juftliklar** uchun kerak.

```sql
CREATE TABLE xodimlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    rahbar_id INTEGER REFERENCES xodimlar(id)
);

INSERT INTO xodimlar (ism, rahbar_id) VALUES
    ('Karim', NULL),
    ('Dilnoza', 1),
    ('Jasur', 1),
    ('Sevara', 2),
    ('Otabek', 2);
```

| id | ism | rahbar_id |
|----|-----|-----------|
| 1 | Karim | `NULL` |
| 2 | Dilnoza | 1 |
| 3 | Jasur | 1 |
| 4 | Sevara | 2 |
| 5 | Otabek | 2 |

## Xodim va uning rahbari

```sql
SELECT x.ism AS xodim, r.ism AS rahbar
FROM xodimlar x
LEFT JOIN xodimlar r ON x.rahbar_id = r.id
ORDER BY x.id;
```

**Natija:**

```
  xodim  | rahbar
---------+---------
 Karim   |
 Dilnoza | Karim
 Jasur   | Karim
 Sevara  | Dilnoza
 Otabek  | Dilnoza
```

> `x` — "xodim" roli, `r` — "rahbar" roli. Bitta jadval, ikki laqab. `LEFT JOIN` ishlatildi, chunki **Karim** ning rahbari yo'q (`NULL`), `INNER JOIN` da u tushib qolardi.

## Bir guruhdagi talabalar juftligi

```sql
SELECT a.ism AS birinchi, b.ism AS ikkinchi, a.guruh_id
FROM talabalar a
JOIN talabalar b
    ON a.guruh_id = b.guruh_id
   AND a.talaba_id < b.talaba_id
ORDER BY a.guruh_id;
```

**Natija:**

```
 birinchi | ikkinchi | guruh_id
----------+----------+----------
 Ali      | Vali     |        1
 Sardor   | Bobur    |        2
```

> `a.talaba_id < b.talaba_id` sharti ikki narsadan saqlaydi: talabaning o'zi bilan juftlanishi (`Ali–Ali`) va takroriy juftlik (`Ali–Vali` va `Vali–Ali`).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✖️ 6️⃣ `CROSS JOIN`

**Ta'rif:** **dekart ko'paytma**: birinchi jadvalning **har bir qatori** ikkinchi jadvalning **har bir qatori** bilan juftlanadi. `ON` sharti **yo'q**. Natija soni: `n × m`.

```sql
CREATE TABLE ranglar (id SERIAL PRIMARY KEY, nom VARCHAR(20));
CREATE TABLE olchamlar (id SERIAL PRIMARY KEY, nom VARCHAR(5));

INSERT INTO ranglar (nom) VALUES ('Qizil'), ('Ko''k');
INSERT INTO olchamlar (nom) VALUES ('S'), ('M'), ('L');
```

```sql
SELECT r.nom AS rang, o.nom AS olcham
FROM ranglar r
CROSS JOIN olchamlar o
ORDER BY r.id, o.id;
```

**Natija** (2 × 3 = 6 qator):

```
 rang  | olcham
-------+--------
 Qizil | S
 Qizil | M
 Qizil | L
 Ko'k  | S
 Ko'k  | M
 Ko'k  | L
```

**Qayerda ishlatiladi:**

| Holat | Misol |
|-------|-------|
| Barcha kombinatsiyalar | Rang × o'lcham, sana × xona |
| Test ma'lumot yaratish | Ko'p qator tez hosil qilish |
| Jadval va qatorlar ketma-ketligi | `generate_series` bilan birga |

**Eski yozuv** (vergul bilan), natijasi bir xil:

```sql
SELECT r.nom, o.nom FROM ranglar r, olchamlar o;
```

> 🚨 **Ehtiyot bo'ling:** `FROM a, b` yozib `WHERE` da bog'lashni unutsangiz, tasodifan `CROSS JOIN` hosil bo'ladi. 1 000 × 1 000 qatorli jadvalda bu **1 000 000** qator! Doim aniq `JOIN ... ON` yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧬 7️⃣ `NATURAL JOIN`

**Ta'rif:** ikkala jadvaldagi **nomi bir xil bo'lgan barcha ustunlar** bo'yicha avtomatik birlashtiradi. `ON` yozilmaydi.

Bizda ikkala jadvalda faqat `guruh_id` nomi umumiy:

```sql
SELECT *
FROM talabalar
NATURAL JOIN guruhlar
ORDER BY talaba_id;
```

**Natija:**

```
 guruh_id | talaba_id |  ism   |  nom
----------+-----------+--------+-------
        1 |         1 | Ali    | PY-12
        1 |         2 | Vali   | PY-12
        2 |         3 | Sardor | JS-05
        2 |         5 | Bobur  | JS-05
```

> Bu `JOIN guruhlar USING (guruh_id)` bilan bir xil natija beradi. Umumiy ustun (`guruh_id`) natijada **bir marta**, boshida chiqadi.

**Variantlari:**

```sql
SELECT * FROM talabalar NATURAL LEFT JOIN guruhlar;
SELECT * FROM talabalar NATURAL RIGHT JOIN guruhlar;
SELECT * FROM talabalar NATURAL FULL JOIN guruhlar;
```

> 🚨 **`NATURAL JOIN` xavfli**, ishlab chiqarish (production) kodida tavsiya etilmaydi:
>
> - Keyinroq jadvalga **tasodifan bir xil nomli ustun** qo'shilsa (masalan, ikkalasiga ham `nom` yoki `yaratilgan`), JOIN sharti **jimgina o'zgaradi** va natija buziladi.
> - Aytaylik, ikkala jadvalda `id` bor: `NATURAL JOIN` ularni `id = id` deb bog'laydi, bu odatda **mantiqsiz**.
> - Qaysi ustunlar bo'yicha bog'lanishi kodda ko'rinmaydi.
>
> Yaxshisi `JOIN ... ON` yoki `JOIN ... USING (...)` yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧭 `ON`, `USING` va `NATURAL` solishtirish

| | `ON` | `USING (ustun)` | `NATURAL` |
|---|------|-----------------|-----------|
| Shart | Aniq yoziladi | Bir xil nomli ustun | Bir xil nomli **barcha** ustunlar |
| Ustun nomi farq qilsa | ✅ Ishlaydi | ❌ Ishlamaydi | ❌ Ishlamaydi |
| Murakkab shart (`AND`, `<`) | ✅ Mumkin | ❌ | ❌ |
| Umumiy ustun natijada | Ikki marta | Bir marta | Bir marta |
| Xavfsizlik | ✅ Eng aniq | ✅ Yaxshi | ❌ Xavfli |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🎛️ `ON` va `WHERE` farqi (`LEFT JOIN` da)

`INNER JOIN` da shartni `ON` ga ham, `WHERE` ga ham yozsa natija bir xil. Lekin **`LEFT JOIN` da farq bor**.

**1. Shart `ON` da** (JOIN **paytida** filtrlanadi, hamma talaba qoladi):

```sql
SELECT t.ism, g.nom
FROM talabalar t
LEFT JOIN guruhlar g
    ON t.guruh_id = g.guruh_id AND g.nom = 'PY-12'
ORDER BY t.talaba_id;
```

```
  ism   |  nom
--------+-------
 Ali    | PY-12
 Vali   | PY-12
 Sardor |
 Aziz   |
 Bobur  |
```

**2. Shart `WHERE` da** (JOIN **dan keyin** filtrlanadi, `NULL` qatorlar tushib qoladi):

```sql
SELECT t.ism, g.nom
FROM talabalar t
LEFT JOIN guruhlar g ON t.guruh_id = g.guruh_id
WHERE g.nom = 'PY-12'
ORDER BY t.talaba_id;
```

```
 ism  |  nom
------+-------
 Ali  | PY-12
 Vali | PY-12
```

| | `ON` ga yozilsa | `WHERE` ga yozilsa |
|---|-----------------|--------------------|
| Qachon | JOIN paytida | JOIN natijasidan keyin |
| Chap jadval qatorlari | **Hammasi** saqlanadi | Mos kelmaganlari **tushib qoladi** |
| Amalda | `LEFT JOIN` ning ma'nosi saqlanadi | `LEFT JOIN` aslida `INNER JOIN` ga aylanadi |

> ⚠️ `LEFT JOIN` yozib, o'ng jadval ustuni bo'yicha `WHERE` da shart qo'ysangiz (`IS NULL` dan tashqari), `LEFT JOIN` ning foydasi yo'qoladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🖼️ Qaysi JOIN ni tanlash?

| Savol | JOIN |
|-------|------|
| Faqat **mos kelganlar** kerakmi? | `INNER JOIN` |
| Chap jadvalning **hammasi** kerakmi (mosi bo'lmasa ham)? | `LEFT JOIN` |
| Mosi **yo'q** qatorlarni topish kerakmi? | `LEFT JOIN ... WHERE o'ng.id IS NULL` |
| **Ikkala** jadvalning hammasi kerakmi? | `FULL JOIN` |
| Jadval **o'zi bilan** bog'lanadimi (ierarxiya, juftlik)? | `SELF JOIN` |
| **Barcha kombinatsiyalar** kerakmi? | `CROSS JOIN` |

**Qisqa jadval:**

| JOIN | Ali (mos bor) | Aziz (guruhsiz) | UI-03 (talabasiz) |
|------|---------------|-----------------|--------------------|
| `INNER` | ✅ | ❌ | ❌ |
| `LEFT` (talabalar chapda) | ✅ | ✅ | ❌ |
| `RIGHT` (guruhlar o'ngda) | ✅ | ❌ | ✅ |
| `FULL` | ✅ | ✅ | ✅ |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ⚡ Tezlik haqida

| Maslahat | Sababi |
|----------|--------|
| `JOIN` qilinadigan ustunlarga **indeks** qo'ying | Qidirish tezlashadi |
| `FOREIGN KEY` o'zi **indeks yaratmaydi** | PostgreSQL'da FK ustuniga alohida `CREATE INDEX` kerak (PK va `UNIQUE` ga avtomatik) |
| `SELECT *` o'rniga kerakli ustunlarni yozing | Kam ma'lumot ko'chiriladi |
| Avval `WHERE` bilan qatorlarni kamaytiring | JOIN kichikroq ma'lumot bilan ishlaydi |
| Tahlil qilish uchun `EXPLAIN ANALYZE` | So'rov rejasi va vaqtini ko'rsatadi |

```sql
CREATE INDEX idx_talabalar_guruh_id ON talabalar (guruh_id);

EXPLAIN ANALYZE
SELECT t.ism, g.nom
FROM talabalar t
JOIN guruhlar g ON t.guruh_id = g.guruh_id;
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🐍 Python'dan JOIN so'rovi

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
        # INNER JOIN
        cursor.execute("""
            SELECT t.ism, g.nom
            FROM talabalar t
            JOIN guruhlar g ON t.guruh_id = g.guruh_id
            ORDER BY t.talaba_id
        """)
        for ism, guruh in cursor.fetchall():
            print(f"{ism} - {guruh}")

        # LEFT JOIN: guruhsiz talabalar uchun None keladi
        cursor.execute("""
            SELECT t.ism, g.nom
            FROM talabalar t
            LEFT JOIN guruhlar g ON t.guruh_id = g.guruh_id
            ORDER BY t.talaba_id
        """)
        for ism, guruh in cursor.fetchall():
            print(f"{ism} - {guruh or 'guruhsiz'}")

        # Shart bilan: qiymat %s orqali
        cursor.execute("""
            SELECT t.ism, b.fan, b.ball
            FROM talabalar t
            JOIN baholar b ON b.talaba_id = t.talaba_id
            WHERE b.ball >= %s
            ORDER BY b.ball DESC
        """, (80,))
        print(cursor.fetchall())

conn.close()
```

> SQL'dagi `NULL` Python'da **`None`** bo'lib keladi (36-dars). `guruh or 'guruhsiz'` yozuvi `None` o'rniga matn ko'rsatadi.

**SQLAlchemy (30-dars) bilan JOIN:**

```python
from sqlalchemy import select

stmt = (
    select(Talaba.ism, Guruh.nom)
    .join(Guruh, Talaba.guruh_id == Guruh.guruh_id)          # INNER JOIN
)

stmt_left = (
    select(Talaba.ism, Guruh.nom)
    .join(Guruh, Talaba.guruh_id == Guruh.guruh_id, isouter=True)   # LEFT JOIN
)

stmt_full = (
    select(Talaba.ism, Guruh.nom)
    .join(Guruh, Talaba.guruh_id == Guruh.guruh_id, full=True)      # FULL JOIN
)
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Eng ko'p uchraydigan xatolar

| Xato / holat | Sababi | Yechim |
|--------------|--------|--------|
| `column reference "guruh_id" is ambiguous` | Ustun ikkala jadvalda bor | Laqab bilan yozing: `t.guruh_id` |
| Natijada qatorlar kam | `INNER JOIN` mosi yo'q qatorlarni tashlaydi | `LEFT JOIN` ishlating |
| Natijada qatorlar **juda ko'p** | `ON` sharti noto'g'ri yoki yo'q (tasodifiy `CROSS JOIN`), yoki bir-ko'p bog'lanish | `ON` ni tekshiring, `COUNT(*)` bilan solishtiring |
| `LEFT JOIN` `INNER JOIN` kabi ishlayapti | O'ng jadval ustuni bo'yicha `WHERE` sharti | Shartni `ON` ga ko'chiring |
| `COUNT(*)` bahosizlarga `1` beryapti | `LEFT JOIN` da `NULL` qator ham sanaladi | `COUNT(o'ng.ustun)` |
| `missing FROM-clause entry for table "x"` | Laqab noto'g'ri yoki yozilmagan | Laqabni tekshiring |
| `table name "x" specified more than once` | Bir jadval ikki marta, laqabsiz | Har biriga alohida laqab bering (SELF JOIN) |
| `NATURAL JOIN` noto'g'ri natija beryapti | Tasodifan bir xil nomli boshqa ustun | `ON` yoki `USING` ga o'ting |
| `JOIN` sekin ishlayapti | Bog'lovchi ustunda indeks yo'q | `CREATE INDEX` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. Yuqoridagi `guruhlar`, `talabalar`, `baholar` jadvallarini yarating va ma'lumotni qo'shing.
2. `INNER JOIN` bilan talabalar va ularning guruh nomlarini chiqaring.
3. Shu so'rovni `USING (guruh_id)` bilan qayta yozing.
4. `LEFT JOIN` bilan hamma talabani chiqaring (guruhsizlari ham).
5. Guruhi yo'q talabalarni toping (`LEFT JOIN` + `IS NULL`).
6. `RIGHT JOIN` bilan hamma guruhni chiqaring va talabasi yo'q guruhni toping.
7. Xuddi shu so'rovni `LEFT JOIN` bilan, jadvallar o'rnini almashtirib yozing.
8. `FULL JOIN` bilan ikkala jadvalning hamma qatorini chiqaring.
9. Faqat mos kelmagan qatorlarni toping (`FULL JOIN` + `WHERE ... IS NULL OR ... IS NULL`).
10. Uchta jadvalni bog'lang: talaba ismi, guruh nomi, fan va ball.
11. Har bir talabaning o'rtacha bali va baholar sonini chiqaring (`LEFT JOIN`, `GROUP BY`). Bahosizlar ham ko'rinsin.
12. Har bir guruhdagi talabalar sonini chiqaring. Bo'sh guruh uchun `0` chiqsin (`COUNT(t.talaba_id)`).
13. Eng yuqori o'rtacha ball olgan guruhni toping.
14. `xodimlar` jadvalini yarating va `SELF JOIN` bilan xodim va rahbarini chiqaring.
15. Rahbari yo'q xodimlarni toping (`SELF JOIN` + `IS NULL`).
16. Har bir rahbarning qo'l ostida nechta xodim borligini toping.
17. Bir guruhdagi talabalar juftligini chiqaring (`a.talaba_id < b.talaba_id`).
18. `CROSS JOIN` bilan `ranglar` va `olchamlar` kombinatsiyalarini chiqaring, qatorlar soni `n × m` ekanini tekshiring.
19. `NATURAL JOIN` yozib, natijani `USING` bilan solishtiring. So'ng jadvallarga bir xil nomli `nom` ustuni qo'shib, nima o'zgarishini kuzating.
20. `LEFT JOIN` da shartni avval `ON` ga, keyin `WHERE` ga yozib, farqini tushuntiring.
21. `talabalar.guruh_id` ga indeks yarating va `EXPLAIN ANALYZE` ni ishga tushiring.
22. `psycopg2` bilan Python'dan `LEFT JOIN` so'rov yuborib, `None` o'rniga "guruhsiz" so'zini chiqaring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **`JOIN`** bir nechta jadvaldagi bog'liq ma'lumotni umumiy ustun orqali birlashtiradi.
- **`INNER JOIN`** (`JOIN`) faqat mos kelgan qatorlarni beradi.
- **`LEFT JOIN`** chap jadvalning hammasini saqlaydi, mosi yo'q joyda `NULL`. Eng ko'p ishlatiladigan tashqi JOIN.
- **`RIGHT JOIN`** o'ng jadvalning hammasini saqlaydi. Jadvallar o'rnini almashtirib, `LEFT JOIN` bilan yozish mumkin.
- **`FULL JOIN`** ikkala jadvalning hamma qatorini saqlaydi.
- **`SELF JOIN`** jadvalni o'zi bilan **ikki xil laqab** orqali birlashtiradi (ierarxiya, juftliklar).
- **`CROSS JOIN`** `ON` siz, **barcha kombinatsiyalarni** (`n × m`) beradi. `FROM a, b` yozib shartni unutish tasodifiy `CROSS JOIN` ga olib keladi.
- **`NATURAL JOIN`** nomi bir xil ustunlar bo'yicha avtomatik bog'laydi, lekin **xavfli**: `ON` yoki `USING` afzal.
- Mosi **yo'q** qatorni topish: `LEFT JOIN` + `WHERE o'ng.id IS NULL`.
- `LEFT JOIN` da o'ng jadval sharti `ON` ga yoziladi, `WHERE` ga yozilsa `INNER JOIN` ga aylanadi.
- `LEFT JOIN` bilan sanashda `COUNT(*)` emas, `COUNT(o'ng.ustun)` ishlating.
- Ustun nomi ikkala jadvalda bo'lsa, **laqab** bilan yozing (`t.guruh_id`).
- FK ustunlariga `CREATE INDEX` qo'ying, `EXPLAIN ANALYZE` bilan so'rovni tekshiring.

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