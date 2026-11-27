<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2026%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 Ma'lumotlar bazasi (Database)

**Ma'lumotlar bazasi (DB)** — ma'lumotlar tartibli saqlanadigan, tez qidiriladigan va boshqariladigan joy. Fayllarga (`.txt`, `.json`) qaraganda katta hajmdagi ma'lumot bilan ishlash ancha qulay va tez.

| Tushuncha | Tavsif |
|-----------|--------|
| **DB (Database)** | Ma'lumotlar bazasi |
| **DBMS** | Bazani boshqarish tizimi (SQLite, PostgreSQL, MySQL) |
| **Jadval (table)** | Ma'lumotlar saqlanadigan qator va ustunlar |
| **Qator (row, record)** | Bitta yozuv (masalan, bitta talaba) |
| **Ustun (column, field)** | Yozuvning bitta xususiyati (masalan, `ism`) |
| **Primary Key (PK)** | Har bir qatorni noyob aniqlovchi ustun (`id`) |
| **SQL** | Baza bilan ishlash uchun so'rov tili |

**Jadval ko'rinishi:**

| id | ism | yosh | kurs |
|----|-----|------|------|
| 1 | Ali | 20 | 2 |
| 2 | Vali | 22 | 3 |
| 3 | Sardor | 19 | 1 |

**Ma'lumotlar bazasi turlari:**

| Tur | Misol |
|-----|-------|
| **Relyatsion (SQL)** | SQLite, PostgreSQL, MySQL |
| **NoSQL** | MongoDB, Redis |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🪶 SQLite nima?

**SQLite** — alohida server talab qilmaydigan, butun baza **bitta faylda** (`.db`) saqlanadigan yengil ma'lumotlar bazasi.

| Xususiyat | Tavsif |
|-----------|--------|
| O'rnatish | Shart emas, Python bilan birga keladi |
| Server | Kerak emas |
| Saqlash | Bitta `.db` fayl |
| Qachon ishlatiladi | O'rganish, kichik loyiha, mobil ilova, bot |

```python
import sqlite3
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔌 `sqlite3` bilan ishlash tartibi

```python
import sqlite3

# 1. Bazaga ulanish (fayl bo'lmasa, yaratiladi)
conn = sqlite3.connect("maktab.db")

# 2. Kursor yaratish (so'rovlarni bajaruvchi)
cursor = conn.cursor()

# 3. SQL so'rovni bajarish
cursor.execute("SELECT * FROM talabalar")

# 4. O'zgarishlarni saqlash (INSERT, UPDATE, DELETE uchun)
conn.commit()

# 5. Ulanishni yopish
conn.close()
```

| Obyekt / Metod | Vazifasi |
|----------------|----------|
| `connect("nom.db")` | Bazaga ulanadi (`:memory:` — vaqtinchalik xotirada) |
| `conn.cursor()` | So'rov bajaruvchi kursor yaratadi |
| `cursor.execute(sql)` | Bitta SQL so'rovni bajaradi |
| `cursor.executemany(sql, royxat)` | Bir so'rovni ko'p ma'lumot bilan bajaradi |
| `conn.commit()` | O'zgarishlarni bazaga saqlaydi |
| `conn.rollback()` | O'zgarishlarni bekor qiladi |
| `conn.close()` | Ulanishni yopadi |

> ⚠️ `INSERT`, `UPDATE`, `DELETE` dan keyin `commit()` yozilmasa, o'zgarishlar **saqlanmaydi**.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 CRUD nima?

**CRUD** — ma'lumot bilan ishlashning 4 ta asosiy amali:

| Harf | Amal | SQL buyrug'i | Ma'nosi |
|------|------|--------------|---------|
| **C** | Create | `INSERT` | Yangi ma'lumot qo'shish |
| **R** | Read | `SELECT` | Ma'lumotni o'qish |
| **U** | Update | `UPDATE` | Ma'lumotni o'zgartirish |
| **D** | Delete | `DELETE` | Ma'lumotni o'chirish |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧱 Jadval yaratish: `CREATE TABLE`

```sql
CREATE TABLE IF NOT EXISTS talabalar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT NOT NULL,
    yosh INTEGER,
    kurs INTEGER DEFAULT 1
);
```

**SQLite ma'lumot turlari:**

| Tur | Ma'nosi | Python |
|-----|---------|--------|
| `INTEGER` | Butun son | `int` |
| `REAL` | Kasr son | `float` |
| `TEXT` | Matn | `str` |
| `BLOB` | Ikkilik ma'lumot | `bytes` |
| `NULL` | Qiymat yo'q | `None` |

**Cheklovlar (constraints):**

| Cheklov | Ma'nosi |
|---------|---------|
| `PRIMARY KEY` | Noyob identifikator |
| `AUTOINCREMENT` | Raqam avtomatik oshib boradi |
| `NOT NULL` | Bo'sh bo'lishi mumkin emas |
| `UNIQUE` | Qiymat takrorlanmasligi kerak |
| `DEFAULT x` | Standart qiymat |

**Python'da:**

```python
import sqlite3

conn = sqlite3.connect("maktab.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS talabalar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        yosh INTEGER,
        kurs INTEGER DEFAULT 1
    )
""")

conn.commit()
conn.close()
```

> `IF NOT EXISTS` jadval allaqachon bor bo'lsa, xato bermaydi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ C: Create (`INSERT`)

**SQL:**

```sql
INSERT INTO talabalar (ism, yosh, kurs) VALUES ('Ali', 20, 2);
```

**Python'da (to'g'ri usul, `?` bilan):**

```python
cursor.execute(
    "INSERT INTO talabalar (ism, yosh, kurs) VALUES (?, ?, ?)",
    ("Ali", 20, 2)
)
conn.commit()
```

**Bir nechta qator (`executemany`):**

```python
talabalar = [
    ("Vali", 22, 3),
    ("Sardor", 19, 1),
    ("Aziz", 21, 2),
]

cursor.executemany(
    "INSERT INTO talabalar (ism, yosh, kurs) VALUES (?, ?, ?)",
    talabalar
)
conn.commit()
```

**Qo'shilgan qator `id` sini olish:**

```python
print(cursor.lastrowid)    # oxirgi qo'shilgan qatorning id si
```

> 🚨 **Xavfsizlik:** SQL so'rovga qiymatni **f-string yoki `+` bilan qo'shmang**. Bu **SQL Injection** hujumiga yo'l ochadi. Doim `?` (placeholder) ishlating.

```python
# ❌ XAVFLI
cursor.execute(f"INSERT INTO talabalar (ism) VALUES ('{ism}')")

# ✅ XAVFSIZ
cursor.execute("INSERT INTO talabalar (ism) VALUES (?)", (ism,))
```

> Bitta qiymat bo'lsa ham kortej yoziladi: `(ism,)` (vergul shart).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📖 R: Read (`SELECT`)

**SQL:**

```sql
SELECT * FROM talabalar;                       -- hamma ustun, hamma qator
SELECT ism, yosh FROM talabalar;               -- faqat tanlangan ustunlar
SELECT * FROM talabalar WHERE kurs = 2;        -- shart bilan
```

**Natijani olish usullari:**

| Metod | Qaytaradi |
|-------|-----------|
| `fetchall()` | Barcha qatorlar (kortejlar ro'yxati) |
| `fetchone()` | Bitta qator (yoki `None`) |
| `fetchmany(n)` | `n` ta qator |

```python
cursor.execute("SELECT * FROM talabalar")
natija = cursor.fetchall()

print(natija)
# [(1, 'Ali', 20, 2), (2, 'Vali', 22, 3), (3, 'Sardor', 19, 1)]

for qator in natija:
    print(qator[1], qator[2])       # ism va yosh
```

**Bitta qator:**

```python
cursor.execute("SELECT * FROM talabalar WHERE id = ?", (1,))
t = cursor.fetchone()
print(t)       # (1, 'Ali', 20, 2)
```

**Tuple ochish (unpacking):**

```python
cursor.execute("SELECT id, ism, yosh FROM talabalar")

for id, ism, yosh in cursor.fetchall():
    print(f"{id}. {ism} - {yosh} yosh")
```

**Natijani lug'at kabi olish (`Row`):**

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM talabalar")
for qator in cursor.fetchall():
    print(qator["ism"], qator["yosh"])
```

## `WHERE` sharti

| Operator | Ma'nosi | Misol |
|----------|---------|-------|
| `=` | Teng | `WHERE kurs = 2` |
| `!=` yoki `<>` | Teng emas | `WHERE kurs != 2` |
| `>`, `<`, `>=`, `<=` | Taqqoslash | `WHERE yosh >= 20` |
| `AND` | Va | `WHERE yosh > 18 AND kurs = 2` |
| `OR` | Yoki | `WHERE kurs = 1 OR kurs = 2` |
| `NOT` | Emas | `WHERE NOT kurs = 1` |
| `BETWEEN` | Oraliqda | `WHERE yosh BETWEEN 18 AND 22` |
| `IN` | Ro'yxatda | `WHERE kurs IN (1, 2)` |
| `LIKE` | Andoza bo'yicha | `WHERE ism LIKE 'A%'` |
| `IS NULL` | Bo'sh | `WHERE yosh IS NULL` |

**`LIKE` belgilari:**

| Belgi | Ma'nosi | Misol | Mos keladi |
|-------|---------|-------|------------|
| `%` | Istalgan belgilar | `'A%'` | `Ali`, `Aziz` |
| `_` | Bitta belgi | `'A_i'` | `Ali`, `Ani` |

## Qo'shimcha so'zlar

| So'z | Vazifasi | Misol |
|------|----------|-------|
| `ORDER BY` | Tartiblash | `ORDER BY yosh DESC` |
| `LIMIT` | Qatorlar sonini cheklash | `LIMIT 5` |
| `DISTINCT` | Takrorlanmas qiymatlar | `SELECT DISTINCT kurs` |
| `COUNT()` | Qatorlar soni | `SELECT COUNT(*)` |
| `AVG()`, `SUM()`, `MIN()`, `MAX()` | Agregat funksiyalar | `SELECT AVG(yosh)` |
| `GROUP BY` | Guruhlash | `GROUP BY kurs` |

```sql
SELECT * FROM talabalar ORDER BY yosh DESC LIMIT 3;
SELECT COUNT(*) FROM talabalar;
SELECT kurs, COUNT(*) FROM talabalar GROUP BY kurs;
SELECT AVG(yosh) FROM talabalar;
```

```python
cursor.execute("SELECT COUNT(*) FROM talabalar")
print(cursor.fetchone()[0])      # 4
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✏️ U: Update (`UPDATE`)

**SQL:**

```sql
UPDATE talabalar SET yosh = 21 WHERE id = 1;
UPDATE talabalar SET yosh = 23, kurs = 4 WHERE ism = 'Vali';
```

**Python'da:**

```python
cursor.execute(
    "UPDATE talabalar SET yosh = ? WHERE id = ?",
    (21, 1)
)
conn.commit()

print(cursor.rowcount)     # nechta qator o'zgargani
```

> 🚨 **`WHERE` yozishni unutmang!** `WHERE` bo'lmasa, **barcha qatorlar** o'zgaradi:
> `UPDATE talabalar SET kurs = 1;` → hamma talabaning kursi `1` bo'lib ketadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🗑️ D: Delete (`DELETE`)

**SQL:**

```sql
DELETE FROM talabalar WHERE id = 3;
DELETE FROM talabalar WHERE yosh < 18;
```

**Python'da:**

```python
cursor.execute("DELETE FROM talabalar WHERE id = ?", (3,))
conn.commit()

print(cursor.rowcount)     # nechta qator o'chirilgani
```

> 🚨 **`WHERE` bo'lmasa, jadvaldagi hamma ma'lumot o'chadi!**
> `DELETE FROM talabalar;`

| Buyruq | Vazifasi |
|--------|----------|
| `DELETE FROM jadval WHERE ...` | Shartga mos qatorlarni o'chiradi |
| `DROP TABLE jadval` | Jadvalning o'zini butunlay o'chiradi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔒 `with` bilan ishlash

`with` blokida `commit()` avtomatik bajariladi (xato bo'lsa, `rollback`). Lekin ulanishni **yopmaydi**.

```python
import sqlite3

conn = sqlite3.connect("maktab.db")

with conn:
    conn.execute(
        "INSERT INTO talabalar (ism, yosh) VALUES (?, ?)",
        ("Bobur", 20)
    )

conn.close()
```

**`contextlib.closing` bilan to'liq yopish:**

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect("maktab.db")) as conn:
    with conn:
        conn.execute("DELETE FROM talabalar WHERE id = ?", (5,))
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ Xatolarni ushlash

```python
import sqlite3

try:
    conn = sqlite3.connect("maktab.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO talabalar (ism) VALUES (?)", (None,))
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Cheklov buzildi:", e)
except sqlite3.OperationalError as e:
    print("So'rov xatosi:", e)
except sqlite3.Error as e:
    print("Baza xatosi:", e)
finally:
    conn.close()
```

| Xato | Sababi |
|------|--------|
| `sqlite3.IntegrityError` | `NOT NULL`, `UNIQUE`, `PRIMARY KEY` cheklovi buzildi |
| `sqlite3.OperationalError` | Jadval yo'q, SQL sintaksis xatosi |
| `sqlite3.Error` | Barcha sqlite3 xatolarining umumiy klassi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 Amaliy misol: to'liq CRUD dastur

```python
import sqlite3


def ulanish():
    return sqlite3.connect("maktab.db")


def jadval_yaratish():
    with ulanish() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS talabalar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ism TEXT NOT NULL,
                yosh INTEGER,
                kurs INTEGER DEFAULT 1
            )
        """)


# CREATE
def qosh(ism, yosh, kurs=1):
    with ulanish() as conn:
        conn.execute(
            "INSERT INTO talabalar (ism, yosh, kurs) VALUES (?, ?, ?)",
            (ism, yosh, kurs)
        )


# READ
def hammasi():
    with ulanish() as conn:
        return conn.execute("SELECT * FROM talabalar").fetchall()


def topish(id):
    with ulanish() as conn:
        return conn.execute(
            "SELECT * FROM talabalar WHERE id = ?", (id,)
        ).fetchone()


# UPDATE
def yangila(id, yosh, kurs):
    with ulanish() as conn:
        conn.execute(
            "UPDATE talabalar SET yosh = ?, kurs = ? WHERE id = ?",
            (yosh, kurs, id)
        )


# DELETE
def ochir(id):
    with ulanish() as conn:
        conn.execute("DELETE FROM talabalar WHERE id = ?", (id,))


jadval_yaratish()

qosh("Ali", 20, 2)
qosh("Vali", 22, 3)
qosh("Sardor", 19)

for t in hammasi():
    print(t)

yangila(1, 21, 3)
ochir(2)

print(topish(1))       # (1, 'Ali', 21, 3)
```

**Natija:**

```
(1, 'Ali', 20, 2)
(2, 'Vali', 22, 3)
(3, 'Sardor', 19, 1)
(1, 'Ali', 21, 3)
```

> Bu misolda har bir funksiya `ulanish()` orqali yangi ulanish ochadi. `with conn` ichida `commit()` avtomatik bajariladi, shuning uchun alohida yozilmagan.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `sqlite3` bilan `dukon.db` bazasini yarating.
2. `mahsulotlar` jadvalini yarating: `id`, `nom`, `narx`, `miqdor`.
3. Jadvalga 5 ta mahsulot qo'shing (`executemany` bilan).
4. Barcha mahsulotlarni chiqaring.
5. Narxi 10000 dan katta mahsulotlarni toping (`WHERE`).
6. Mahsulotlarni narx bo'yicha kamayish tartibida chiqaring (`ORDER BY`).
7. Bitta mahsulot narxini o'zgartiring (`UPDATE`).
8. Bitta mahsulotni `id` bo'yicha o'chiring (`DELETE`).
9. Mahsulotlar sonini va o'rtacha narxini toping (`COUNT`, `AVG`).
10. Foydalanuvchidan ma'lumot qabul qilib, bazaga qo'shadigan menyu dastur yozing (CRUD).

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **Ma'lumotlar bazasi** ma'lumotni jadval ko'rinishida tartibli saqlaydi, **SQLite** esa bitta `.db` faylda ishlaydi va Python bilan birga keladi.
- Ish tartibi: `connect()` → `cursor()` → `execute()` → `commit()` → `close()`.
- **CRUD:** `INSERT` (qo'shish), `SELECT` (o'qish), `UPDATE` (o'zgartirish), `DELETE` (o'chirish).
- Qiymatlarni so'rovga **doim `?` bilan** uzating, f-string ishlatmang (SQL Injection).
- `UPDATE` va `DELETE` da **`WHERE` ni unutmang**.
- `fetchall()` hamma, `fetchone()` bitta qatorni qaytaradi.
- `INSERT`, `UPDATE`, `DELETE` dan keyin `commit()` shart (yoki `with conn:` ishlating).

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