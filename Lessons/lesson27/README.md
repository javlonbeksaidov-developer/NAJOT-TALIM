<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2027%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 SQLite3 yordamida masalalar

Bu darsda oldingi darsda o'rganilgan **CRUD** va SQL buyruqlari **amaliy masalalar** orqali mustahkamlanadi. Har bir masalada shart, yechim va tushuntirish beriladi.

**Eslatma (ish tartibi):**

```python
import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

# ... so'rovlar ...

conn.commit()
conn.close()
```

| Qoida | Tavsif |
|-------|--------|
| Qiymat uzatish | Doim `?` bilan: `execute("... WHERE id = ?", (id,))` |
| O'zgarish | `INSERT`, `UPDATE`, `DELETE` dan keyin `commit()` |
| `UPDATE` / `DELETE` | `WHERE` ni unutmang |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧪 1-masala: Talabalar bazasi (CRUD)

**Shart:** `talabalar` jadvalini yarating (`id`, `ism`, `yosh`, `kurs`, `ball`). 5 ta talaba qo'shing, so'ng barchasini chiqaring.

```python
import sqlite3

conn = sqlite3.connect("maktab.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS talabalar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        yosh INTEGER,
        kurs INTEGER DEFAULT 1,
        ball REAL DEFAULT 0
    )
""")

talabalar = [
    ("Ali", 20, 2, 85.5),
    ("Vali", 22, 3, 92.0),
    ("Sardor", 19, 1, 70.0),
    ("Aziz", 21, 2, 88.5),
    ("Bobur", 23, 4, 60.0),
]

cursor.executemany(
    "INSERT INTO talabalar (ism, yosh, kurs, ball) VALUES (?, ?, ?, ?)",
    talabalar
)
conn.commit()

cursor.execute("SELECT * FROM talabalar")
for qator in cursor.fetchall():
    print(qator)

conn.close()
```

**Natija:**

```
(1, 'Ali', 20, 2, 85.5)
(2, 'Vali', 22, 3, 92.0)
(3, 'Sardor', 19, 1, 70.0)
(4, 'Aziz', 21, 2, 88.5)
(5, 'Bobur', 23, 4, 60.0)
```

> ⚠️ Dasturni ikkinchi marta ishga tushirsangiz, talabalar **yana qo'shiladi** (takrorlanadi), chunki `INSERT` har safar bajariladi. Tozalash uchun `.db` faylni o'chiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔍 2-masala: Shart bo'yicha qidirish

**Shart:** quyidagilarni toping:

- a) 2-kursda o'qiydigan talabalar
- b) Bali 80 dan yuqori talabalar
- c) Ismi `A` harfi bilan boshlanadiganlar
- d) Yoshi 20 va 22 orasidagilar

```python
import sqlite3

conn = sqlite3.connect("maktab.db")
cursor = conn.cursor()

# a) 2-kurs
cursor.execute("SELECT ism FROM talabalar WHERE kurs = ?", (2,))
print("2-kurs:", cursor.fetchall())

# b) ball > 80
cursor.execute("SELECT ism, ball FROM talabalar WHERE ball > ?", (80,))
print("80 dan yuqori:", cursor.fetchall())

# c) A bilan boshlanadigan
cursor.execute("SELECT ism FROM talabalar WHERE ism LIKE ?", ("A%",))
print("A harfi:", cursor.fetchall())

# d) yosh oralig'i
cursor.execute("SELECT ism, yosh FROM talabalar WHERE yosh BETWEEN ? AND ?", (20, 22))
print("20-22 yosh:", cursor.fetchall())

conn.close()
```

**Natija:**

```
2-kurs: [('Ali',), ('Aziz',)]
80 dan yuqori: [('Ali', 85.5), ('Vali', 92.0), ('Aziz', 88.5)]
A harfi: [('Ali',), ('Aziz',)]
20-22 yosh: [('Ali', 20), ('Vali', 22), ('Aziz', 21)]
```

> `LIKE` bilan `%` ni so'rov ichiga emas, **qiymatning ichiga** yozing: `("A%",)`.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📊 3-masala: Tartiblash va cheklash

**Shart:** eng yuqori ball olgan **3 ta** talabani toping.

```python
cursor.execute("""
    SELECT ism, ball
    FROM talabalar
    ORDER BY ball DESC
    LIMIT 3
""")

for o'rin, (ism, ball) in enumerate(cursor.fetchall(), start=1):
    print(f"{o'rin}. {ism} - {ball}")
```

> ⚠️ Python'da `o'rin` kabi apostrofli nom **xato** beradi. O'zgaruvchi nomini `orin` deb yozing:

```python
for orin, (ism, ball) in enumerate(cursor.fetchall(), start=1):
    print(f"{orin}. {ism} - {ball}")
```

**Natija:**

```
1. Vali - 92.0
2. Aziz - 88.5
3. Ali - 85.5
```

| So'z | Vazifasi |
|------|----------|
| `ORDER BY ball DESC` | Kamayish tartibida (katta → kichik) |
| `ORDER BY ball ASC` | O'sish tartibida (kichik → katta), standart |
| `LIMIT 3` | Faqat dastlabki 3 ta qator |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧮 4-masala: Statistika (agregat funksiyalar)

**Shart:** talabalar soni, o'rtacha ball, eng yuqori va eng past ballni toping.

```python
cursor.execute("""
    SELECT COUNT(*), AVG(ball), MAX(ball), MIN(ball)
    FROM talabalar
""")

soni, ortacha, eng_yuqori, eng_past = cursor.fetchone()

print("Talabalar soni:", soni)
print("O'rtacha ball:", round(ortacha, 2))
print("Eng yuqori:", eng_yuqori)
print("Eng past:", eng_past)
```

**Natija:**

```
Talabalar soni: 5
O'rtacha ball: 79.2
Eng yuqori: 92.0
Eng past: 60.0
```

**Guruhlash (`GROUP BY`): har bir kursda nechta talaba va o'rtacha ball:**

```python
cursor.execute("""
    SELECT kurs, COUNT(*), AVG(ball)
    FROM talabalar
    GROUP BY kurs
    ORDER BY kurs
""")

for kurs, soni, ortacha in cursor.fetchall():
    print(f"{kurs}-kurs: {soni} ta talaba, o'rtacha {ortacha:.1f}")
```

**Natija:**

```
1-kurs: 1 ta talaba, o'rtacha 70.0
2-kurs: 2 ta talaba, o'rtacha 87.0
3-kurs: 1 ta talaba, o'rtacha 92.0
4-kurs: 1 ta talaba, o'rtacha 60.0
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✏️ 5-masala: Yangilash va o'chirish

**Shart:**

- a) `Sardor` ning ballini `75` ga o'zgartiring
- b) Barcha talabalarning ballini `5` ga oshiring
- c) Bali 65 dan past talabalarni o'chiring

```python
# a) bitta talaba
cursor.execute("UPDATE talabalar SET ball = ? WHERE ism = ?", (75, "Sardor"))
print("O'zgargan qatorlar:", cursor.rowcount)

# b) hammaga +5
cursor.execute("UPDATE talabalar SET ball = ball + 5")

# c) ball < 65 ni o'chirish
cursor.execute("DELETE FROM talabalar WHERE ball < ?", (65,))
print("O'chirilgan qatorlar:", cursor.rowcount)

conn.commit()
```

| Atribut | Vazifasi |
|---------|----------|
| `cursor.rowcount` | So'rov ta'sir qilgan qatorlar soni |

> 🚨 b) misolda `WHERE` ataylab yozilmadi, chunki hamma qator o'zgarishi kerak. Boshqa hollarda `WHERE` ni unutmang.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛒 6-masala: Do'kon (mahsulotlar va savdo)

**Shart:** `mahsulotlar` jadvali yarating (`id`, `nom`, `narx`, `miqdor`). Mahsulot sotib olish funksiyasini yozing: omborda yetarli bo'lsa, miqdorni kamaytirsin, aks holda xabar bersin.

```python
import sqlite3

conn = sqlite3.connect("dukon.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahsulotlar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL UNIQUE,
        narx INTEGER NOT NULL,
        miqdor INTEGER DEFAULT 0
    )
""")

cursor.executemany(
    "INSERT OR IGNORE INTO mahsulotlar (nom, narx, miqdor) VALUES (?, ?, ?)",
    [
        ("Non", 4000, 50),
        ("Sut", 12000, 20),
        ("Tuxum", 15000, 30),
    ]
)
conn.commit()


def sotib_ol(nom, soni):
    cursor.execute("SELECT narx, miqdor FROM mahsulotlar WHERE nom = ?", (nom,))
    qator = cursor.fetchone()

    if qator is None:
        print(f"'{nom}' topilmadi!")
        return

    narx, miqdor = qator

    if soni > miqdor:
        print(f"Omborda faqat {miqdor} ta {nom} bor!")
        return

    cursor.execute(
        "UPDATE mahsulotlar SET miqdor = miqdor - ? WHERE nom = ?",
        (soni, nom)
    )
    conn.commit()
    print(f"{soni} ta {nom} sotildi. Jami: {narx * soni} so'm")


sotib_ol("Non", 10)        # 10 ta Non sotildi. Jami: 40000 so'm
sotib_ol("Sut", 50)        # Omborda faqat 20 ta Sut bor!
sotib_ol("Olma", 1)        # 'Olma' topilmadi!

conn.close()
```

| So'z | Vazifasi |
|------|----------|
| `UNIQUE` | Bir xil nomli mahsulot ikki marta qo'shilmaydi |
| `INSERT OR IGNORE` | Takrorlanish bo'lsa, xato bermasdan o'tkazib yuboradi |
| `fetchone()` → `None` | Mahsulot topilmadi degani |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📒 7-masala: Telefon kontaktlar (menyu dastur)

**Shart:** konsolda ishlaydigan, CRUD amallari bor kontaktlar dasturi yozing.

```python
import sqlite3

conn = sqlite3.connect("kontaktlar.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS kontaktlar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        telefon TEXT NOT NULL UNIQUE
    )
""")
conn.commit()


def qosh():
    ism = input("Ism: ")
    telefon = input("Telefon: ")
    try:
        cursor.execute(
            "INSERT INTO kontaktlar (ism, telefon) VALUES (?, ?)",
            (ism, telefon)
        )
        conn.commit()
        print("Qo'shildi!")
    except sqlite3.IntegrityError:
        print("Bu raqam allaqachon mavjud!")


def korsat():
    cursor.execute("SELECT * FROM kontaktlar ORDER BY ism")
    qatorlar = cursor.fetchall()
    if not qatorlar:
        print("Kontaktlar yo'q.")
    for id, ism, telefon in qatorlar:
        print(f"{id}. {ism} - {telefon}")


def qidir():
    soz = input("Ism bo'yicha qidirish: ")
    cursor.execute("SELECT * FROM kontaktlar WHERE ism LIKE ?", (f"%{soz}%",))
    qatorlar = cursor.fetchall()
    if not qatorlar:
        print("Topilmadi.")
    for id, ism, telefon in qatorlar:
        print(f"{id}. {ism} - {telefon}")


def yangila():
    id = int(input("Qaysi ID: "))
    telefon = input("Yangi telefon: ")
    cursor.execute("UPDATE kontaktlar SET telefon = ? WHERE id = ?", (telefon, id))
    conn.commit()
    print("Yangilandi!" if cursor.rowcount else "ID topilmadi!")


def ochir():
    id = int(input("Qaysi ID: "))
    cursor.execute("DELETE FROM kontaktlar WHERE id = ?", (id,))
    conn.commit()
    print("O'chirildi!" if cursor.rowcount else "ID topilmadi!")


while True:
    print("\n1. Qo'shish\n2. Ko'rsatish\n3. Qidirish\n4. Yangilash\n5. O'chirish\n0. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        qosh()
    elif tanlov == "2":
        korsat()
    elif tanlov == "3":
        qidir()
    elif tanlov == "4":
        yangila()
    elif tanlov == "5":
        ochir()
    elif tanlov == "0":
        break
    else:
        print("Noto'g'ri tanlov!")

conn.close()
```

> `LIKE` da qidirish uchun qiymatni `f"%{soz}%"` shaklida tayyorlab, `?` orqali uzatamiz. Bu xavfsiz, chunki f-string faqat qiymatni tayyorlaydi, SQL so'rovning o'zini emas.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏦 8-masala: Bank hisobi (tranzaksiya)

**Shart:** bir hisobdan boshqasiga pul o'tkazing. Ikkala amal **birga** bajarilishi yoki **birortasi ham** bajarilmasligi kerak.

```python
import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS hisoblar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        egasi TEXT NOT NULL UNIQUE,
        balans INTEGER NOT NULL CHECK (balans >= 0)
    )
""")

cursor.executemany(
    "INSERT OR IGNORE INTO hisoblar (egasi, balans) VALUES (?, ?)",
    [("Ali", 100000), ("Vali", 50000)]
)
conn.commit()


def otkazma(kimdan, kimga, summa):
    try:
        cursor.execute(
            "UPDATE hisoblar SET balans = balans - ? WHERE egasi = ?",
            (summa, kimdan)
        )
        cursor.execute(
            "UPDATE hisoblar SET balans = balans + ? WHERE egasi = ?",
            (summa, kimga)
        )
        conn.commit()
        print(f"{kimdan} -> {kimga}: {summa} so'm o'tkazildi")
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Xato: mablag' yetarli emas, amal bekor qilindi")


otkazma("Ali", "Vali", 30000)      # muvaffaqiyatli
otkazma("Vali", "Ali", 500000)     # xato, bekor qilinadi

cursor.execute("SELECT * FROM hisoblar")
print(cursor.fetchall())

conn.close()
```

| Tushuncha | Tavsif |
|-----------|--------|
| **Tranzaksiya** | Bir butun sifatida bajariladigan amallar guruhi |
| `commit()` | Hamma amalni tasdiqlaydi |
| `rollback()` | Xato bo'lsa, hamma amalni bekor qiladi |
| `CHECK (balans >= 0)` | Balans manfiy bo'lishini taqiqlaydi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧩 9-masala: OOP bilan birgalikda

**Shart:** baza bilan ishlashni klass ichiga joylang.

```python
import sqlite3


class TalabaDB:
    def __init__(self, fayl="maktab.db"):
        self.conn = sqlite3.connect(fayl)
        self.cursor = self.conn.cursor()
        self.jadval_yarat()

    def jadval_yarat(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS talabalar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ism TEXT NOT NULL,
                yosh INTEGER,
                ball REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def qosh(self, ism, yosh, ball=0):
        self.cursor.execute(
            "INSERT INTO talabalar (ism, yosh, ball) VALUES (?, ?, ?)",
            (ism, yosh, ball)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def hammasi(self):
        self.cursor.execute("SELECT * FROM talabalar")
        return self.cursor.fetchall()

    def topish(self, id):
        self.cursor.execute("SELECT * FROM talabalar WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def yangila(self, id, ball):
        self.cursor.execute("UPDATE talabalar SET ball = ? WHERE id = ?", (ball, id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def ochir(self, id):
        self.cursor.execute("DELETE FROM talabalar WHERE id = ?", (id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def yopish(self):
        self.conn.close()


db = TalabaDB()
id = db.qosh("Ali", 20, 85)
print(db.topish(id))
db.yangila(id, 90)
print(db.hammasi())
db.ochir(id)
db.yopish()
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun masalalar

1. `kitoblar` jadvalini yarating (`id`, `nom`, `muallif`, `yil`, `narx`) va 6 ta kitob qo'shing.
2. 2020-yildan keyin chiqqan kitoblarni toping.
3. Muallifi bo'yicha kitoblar sonini chiqaring (`GROUP BY`).
4. Eng qimmat va eng arzon kitobni toping.
5. Nomida "Python" so'zi bor kitoblarni qidiring (`LIKE`).
6. Kitob narxini 10% ga oshiring (`UPDATE`).
7. Foydalanuvchidan `id` so'rab, kitobni o'chiring.
8. `xodimlar` jadvalini yarating (`ism`, `lavozim`, `maosh`). Lavozim bo'yicha o'rtacha maoshni chiqaring.
9. Maoshi o'rtachadan yuqori xodimlarni toping: `WHERE maosh > (SELECT AVG(maosh) FROM xodimlar)`.
10. Natijalarni `.json` faylga saqlang (`json.dump`).
11. "Vazifalar ro'yxati" (To-Do) dasturini yozing: qo'shish, bajarildi deb belgilash, o'chirish.
12. OOP yordamida `KitobDB` klassini yarating.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- Masala yechishda avval **jadval tuzilishini** o'ylang, so'ng kerakli SQL so'rovni tanlang.
- Qidirish: `WHERE`, `LIKE`, `BETWEEN`, `IN`. Tartiblash: `ORDER BY`, `LIMIT`.
- Statistika: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`, `GROUP BY`.
- `cursor.rowcount` o'zgargan yoki o'chirilgan qatorlar sonini beradi.
- `UNIQUE`, `NOT NULL`, `CHECK` cheklovlari noto'g'ri ma'lumotdan himoya qiladi.
- Bir nechta bog'liq amal bo'lsa, **`commit()`** va xato holatida **`rollback()`** ishlating.
- Baza bilan ishlashni funksiya yoki **klass** ichiga joylash kodni tartibli qiladi.
- Qiymatlarni doim **`?`** bilan uzating (SQL Injection'dan himoya).

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