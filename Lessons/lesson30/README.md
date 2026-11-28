<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2030%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 ORM va SQLAlchemy

**ORM (Object-Relational Mapping)** — ma'lumotlar bazasidagi **jadvallarni Python klasslari**, **qatorlarni obyektlar** sifatida ishlatish usuli. SQL yozish o'rniga oddiy Python kodi yoziladi.

**SQLAlchemy** — Python'dagi eng mashhur ORM kutubxonasi. U SQLite, PostgreSQL, MySQL va boshqa bazalar bilan ishlaydi.

| Baza tushunchasi | ORM da |
|------------------|--------|
| Jadval (table) | Klass (`class Talaba`) |
| Qator (row) | Obyekt (`Talaba(ism="Ali")`) |
| Ustun (column) | Atribut (`talaba.ism`) |
| SQL so'rov | Python ifodasi (`select(Talaba)`) |

**database.py uchun**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**ORM afzalliklari:**

| Afzallik | Tavsif |
|----------|--------|
| Kam SQL | Jadvallar bilan klass va obyektlar orqali ishlanadi |
| Xavfsizlik | Qiymatlar avtomatik uzatiladi (SQL Injection'dan himoya) |
| Bazani almashtirish | SQLite dan PostgreSQL ga o'tish uchun asosan ulanish manzili o'zgaradi |
| OOP | 22-25 darslardagi klasslar bilan mos keladi |
| Bog'lanishlar | Jadvallar orasidagi aloqa (`relationship`) qulay |

> 💡 Bu dars **SQLAlchemy 2.0** uslubida yozilgan (`DeclarativeBase`, `Mapped`, `select`). Internetda eski uslubdagi (`declarative_base()`, `session.query()`) misollar ham ko'p uchraydi, ular ishlaydi, lekin yangi loyihada 2.0 uslubi tavsiya etiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛠️ O'rnatish

Virtual muhitni faollashtiring (20-dars) va o'rnating:

```bash
pip install sqlalchemy
pip show sqlalchemy
```

```python
import sqlalchemy
print(sqlalchemy.__version__)    # 2.x.x
```

| Qism | Vazifasi |
|------|----------|
| **Engine** | Bazaga ulanish (markaziy obyekt) |
| **Model** | Jadvalni tavsiflovchi klass |
| **Session** | Baza bilan "suhbat": so'rov, qo'shish, saqlash |
| **`select()`** | Ma'lumot olish so'rovini tuzadi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔌 1. Engine (ulanish)

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///maktab.db", echo=True)
```

| Qism | Ma'nosi |
|------|---------|
| `sqlite:///maktab.db` | SQLite, joriy papkadagi `maktab.db` fayli |
| `sqlite:///:memory:` | Vaqtincha xotirada baza (sinov uchun) |
| `echo=True` | Bajarilayotgan SQL'ni terminalda ko'rsatadi (o'rganish uchun qulay) |

**Ulanish manzili tuzilishi:**

```
dialekt:///fayl_yoki_manzil
postgresql://user:parol@localhost/baza_nomi
```

> 🔐 Bazaga ulanish manzilini `.env` da saqlab, `python-decouple` bilan o'qish tavsiya etiladi (20-dars):
> `DB_URL=sqlite:///maktab.db` → `create_engine(config("DB_URL"))`

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🏗️ 2. Model (jadval klassi)

```python
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Talaba(Base):
    __tablename__ = "talabalar"

    id: Mapped[int] = mapped_column(primary_key=True)
    ism: Mapped[str] = mapped_column(String(50))
    yosh: Mapped[int | None]
    kurs: Mapped[int] = mapped_column(default=1)
    ball: Mapped[float] = mapped_column(default=0.0)

    def __repr__(self):
        return f"Talaba(id={self.id}, ism={self.ism!r}, kurs={self.kurs})"
```

**Qismlari:**

| Qism | Tavsif |
|------|--------|
| `Base(DeclarativeBase)` | Barcha modellar uchun ota klass (meros olish, 25-dars) |
| `__tablename__` | Bazadagi jadval nomi |
| `Mapped[int]` | Ustun Python turi (`int` → `INTEGER`) |
| `mapped_column(...)` | Ustun sozlamalari |
| `Mapped[int \| None]` | `None` bo'lishi mumkin (`NULL` ruxsat etilgan) |
| `__repr__` | Obyektni chiroyli chiqarish (24-dars) |

> `Mapped[str]` (`None` siz) ustunni avtomatik `NOT NULL` qiladi, `Mapped[str | None]` esa `NULL` ga ruxsat beradi.

**Turlar mosligi:**

| Python | SQLAlchemy | SQL |
|--------|------------|-----|
| `int` | `Integer` | `INTEGER` |
| `str` | `String(n)` | `VARCHAR(n)` |
| `float` | `Float` | `FLOAT` |
| `bool` | `Boolean` | `BOOLEAN` |
| `datetime` | `DateTime` | `DATETIME` |
| matn (uzun) | `Text` | `TEXT` |

**`mapped_column` parametrlari:**

| Parametr | Ma'nosi | Misol |
|----------|---------|-------|
| `primary_key=True` | Birlamchi kalit | `id` |
| `unique=True` | Qiymat takrorlanmaydi | `email` |
| `nullable=False` | Bo'sh bo'lishi mumkin emas | `ism` |
| `default=...` | Standart qiymat | `default=1` |
| `index=True` | Qidirishni tezlashtiradi | `ism` |

## Jadvallarni yaratish

```python
engine = create_engine("sqlite:///maktab.db", echo=True)
Base.metadata.create_all(engine)
```

> `create_all()` faqat **mavjud bo'lmagan** jadvallarni yaratadi. Mavjud jadval tuzilishini **o'zgartirmaydi**. Buning uchun migratsiya vositasi (**Alembic**) ishlatiladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💬 3. Session

**Session** — baza bilan ishlaydigan "ish oynasi". Obyektlar shu orqali qo'shiladi, o'qiladi va saqlanadi.

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    # ... ish ...
    session.commit()
```

| Metod | Vazifasi |
|-------|----------|
| `session.add(obj)` | Bitta obyektni qo'shadi |
| `session.add_all([...])` | Bir nechta obyektni qo'shadi |
| `session.commit()` | O'zgarishlarni bazaga saqlaydi |
| `session.rollback()` | O'zgarishlarni bekor qiladi |
| `session.delete(obj)` | Obyektni o'chirishga belgilaydi |
| `session.get(Model, id)` | `id` bo'yicha bitta obyekt |
| `session.scalars(stmt)` | So'rov natijasini obyektlar sifatida beradi |
| `session.refresh(obj)` | Obyektni bazadan qayta yuklaydi |

> `with Session(engine) as session:` blokdan chiqqanda sessiya **avtomatik yopiladi**. `commit()` ni esa o'zingiz yozasiz (yoki `with session.begin():` ishlating).

**Avtomatik `commit` bilan:**

```python
with Session(engine) as session:
    with session.begin():
        session.add(Talaba(ism="Ali", yosh=20))
    # begin() blokidan muvaffaqiyatli chiqsa, commit avtomatik bajariladi
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 4. CRUD amallari

## ➕ C: Create (qo'shish)

```python
with Session(engine) as session:
    t1 = Talaba(ism="Ali", yosh=20, kurs=2, ball=85.5)
    session.add(t1)

    session.add_all([
        Talaba(ism="Vali", yosh=22, kurs=3, ball=92.0),
        Talaba(ism="Sardor", yosh=19, kurs=1, ball=70.0),
        Talaba(ism="Aziz", yosh=21, kurs=2, ball=88.5),
        Talaba(ism="Bobur", yosh=23, kurs=4, ball=60.0),
    ])

    session.commit()
    print(t1.id)        # 1  (commit dan keyin id paydo bo'ladi)
```

> `id` ni o'zimiz bermadik: baza uni avtomatik beradi.

## 📖 R: Read (o'qish)

O'qish uchun `select()` ishlatiladi:

```python
from sqlalchemy import select

with Session(engine) as session:
    # Hammasi
    stmt = select(Talaba)
    for t in session.scalars(stmt):
        print(t)
```

**Natijani olish usullari:**

| Usul | Qaytaradi |
|------|-----------|
| `session.scalars(stmt).all()` | Barcha obyektlar (ro'yxat) |
| `session.scalars(stmt).first()` | Birinchi obyekt yoki `None` |
| `session.scalars(stmt).one()` | Aynan bitta obyekt (yo'q yoki ko'p bo'lsa xato) |
| `session.scalars(stmt).one_or_none()` | Bitta obyekt yoki `None` (ko'p bo'lsa xato) |
| `session.get(Talaba, 1)` | `id` bo'yicha (eng tez usul), topilmasa `None` |

```python
with Session(engine) as session:
    hamma = session.scalars(select(Talaba)).all()
    birinchi = session.scalars(select(Talaba)).first()
    ali = session.get(Talaba, 1)

    print(len(hamma))        # 5
    print(ali.ism)           # Ali
```

### Shart: `where()`

```python
with Session(engine) as session:
    # 2-kurs
    stmt = select(Talaba).where(Talaba.kurs == 2)

    # Bali 80 dan yuqori
    stmt = select(Talaba).where(Talaba.ball > 80)

    # Bir nechta shart (AND)
    stmt = select(Talaba).where(Talaba.kurs == 2, Talaba.ball > 85)

    for t in session.scalars(stmt):
        print(t.ism, t.ball)
```

**Shart operatorlari:**

| SQL | SQLAlchemy |
|-----|------------|
| `=` | `Talaba.kurs == 2` |
| `!=` | `Talaba.kurs != 2` |
| `>`, `<`, `>=`, `<=` | `Talaba.ball > 80` |
| `LIKE` | `Talaba.ism.like("A%")` |
| `IN` | `Talaba.kurs.in_([1, 2])` |
| `BETWEEN` | `Talaba.yosh.between(20, 22)` |
| `IS NULL` | `Talaba.yosh.is_(None)` |
| `AND` | `and_(a, b)` yoki `where(a, b)` |
| `OR` | `or_(a, b)` |
| `NOT` | `not_(a)` |

```python
from sqlalchemy import or_

stmt = select(Talaba).where(or_(Talaba.kurs == 1, Talaba.ball > 90))
```

> ⚠️ Python'dagi `and`, `or` bu yerda **ishlamaydi**. `and_()`, `or_()` yoki `where()` ichida vergul ishlating. `None` bilan solishtirishda `== None` emas, `.is_(None)` yoziladi.

### Tartiblash va cheklash

```python
stmt = (
    select(Talaba)
    .order_by(Talaba.ball.desc())
    .limit(3)
)

for t in session.scalars(stmt):
    print(t.ism, t.ball)
```

| Metod | SQL |
|-------|-----|
| `.order_by(Talaba.ball)` | `ORDER BY ball` (o'sish) |
| `.order_by(Talaba.ball.desc())` | `ORDER BY ball DESC` (kamayish) |
| `.limit(n)` | `LIMIT n` |
| `.offset(n)` | `OFFSET n` (sahifalash uchun) |
| `.distinct()` | `DISTINCT` |

### Agregat funksiyalar

```python
from sqlalchemy import func

with Session(engine) as session:
    soni = session.scalar(select(func.count()).select_from(Talaba))
    ortacha = session.scalar(select(func.avg(Talaba.ball)))
    eng_yuqori = session.scalar(select(func.max(Talaba.ball)))

    print(soni, round(ortacha, 1), eng_yuqori)
```

`session.scalar()` — natijaning birinchi qiymatini (bitta son) qaytaradi.

**Guruhlash:**

```python
stmt = (
    select(Talaba.kurs, func.count(), func.avg(Talaba.ball))
    .group_by(Talaba.kurs)
    .order_by(Talaba.kurs)
)

for kurs, soni, ortacha in session.execute(stmt):
    print(f"{kurs}-kurs: {soni} ta, o'rtacha {ortacha:.1f}")
```

> Bir nechta ustun tanlanganda `session.execute()` ishlatiladi, u kortej-qatorlar qaytaradi.

## ✏️ U: Update (yangilash)

**1-usul: obyektni topib, atributni o'zgartirish** (eng ko'p ishlatiladi):

```python
with Session(engine) as session:
    t = session.get(Talaba, 1)
    t.ball = 95
    t.kurs = 3
    session.commit()
```

> Obyekt atributini o'zgartirish kifoya, SQLAlchemy o'zgarishni o'zi payqaydi. `commit()` shart.

**2-usul: ko'p qatorni birdan yangilash:**

```python
from sqlalchemy import update

with Session(engine) as session:
    session.execute(
        update(Talaba)
        .where(Talaba.kurs == 1)
        .values(ball=Talaba.ball + 5)
    )
    session.commit()
```

## 🗑️ D: Delete (o'chirish)

**1-usul: obyekt orqali:**

```python
with Session(engine) as session:
    t = session.get(Talaba, 5)
    if t:
        session.delete(t)
        session.commit()
```

**2-usul: ko'p qatorni birdan o'chirish:**

```python
from sqlalchemy import delete

with Session(engine) as session:
    natija = session.execute(delete(Talaba).where(Talaba.ball < 65))
    session.commit()
    print("O'chirilgan:", natija.rowcount)
```

> 🚨 `update()` va `delete()` da `.where()` ni unutmang, aks holda **hamma qator** o'zgaradi yoki o'chadi.

**CRUD jadvali:**

| Amal | SQL | SQLAlchemy |
|------|-----|------------|
| **C** | `INSERT` | `session.add(obj)` |
| **R** | `SELECT` | `session.scalars(select(Model))` |
| **U** | `UPDATE` | `obj.atribut = qiymat` yoki `update()` |
| **D** | `DELETE` | `session.delete(obj)` yoki `delete()` |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔗 5. Jadvallar orasidagi bog'lanish

Ko'p holatda jadvallar bir-biriga bog'langan. Masalan, **bitta guruhda ko'p talaba** bor (**One-to-Many**).

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Guruh(Base):
    __tablename__ = "guruhlar"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(30), unique=True)

    talabalar: Mapped[list["Talaba"]] = relationship(
        back_populates="guruh",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"Guruh({self.nom!r})"


class Talaba(Base):
    __tablename__ = "talabalar"

    id: Mapped[int] = mapped_column(primary_key=True)
    ism: Mapped[str] = mapped_column(String(50))
    ball: Mapped[float] = mapped_column(default=0.0)

    guruh_id: Mapped[int] = mapped_column(ForeignKey("guruhlar.id"))
    guruh: Mapped["Guruh"] = relationship(back_populates="talabalar")

    def __repr__(self):
        return f"Talaba({self.ism!r}, ball={self.ball})"
```

| Qism | Tavsif |
|------|--------|
| `ForeignKey("guruhlar.id")` | Boshqa jadvalga havola (baza darajasida) |
| `relationship()` | Python darajasida bog'lanish: obyektlar orasida yurish imkoni |
| `back_populates` | Ikki tomonni bir-biriga ulaydi |
| `cascade="all, delete-orphan"` | Guruh o'chsa, uning talabalari ham o'chadi |

**Ishlatish:**

```python
engine = create_engine("sqlite:///maktab.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    py = Guruh(nom="PY-12")
    py.talabalar = [
        Talaba(ism="Ali", ball=85),
        Talaba(ism="Vali", ball=92),
    ]

    session.add(py)             # talabalar ham avtomatik qo'shiladi
    session.commit()

    guruh = session.scalars(select(Guruh).where(Guruh.nom == "PY-12")).one()
    print(guruh.talabalar)             # [Talaba('Ali', ...), Talaba('Vali', ...)]

    ali = session.scalars(select(Talaba).where(Talaba.ism == "Ali")).one()
    print(ali.guruh.nom)               # PY-12
```

> `guruh.talabalar` va `ali.guruh` orqali SQL yozmasdan bog'langan obyektlarga o'tish mumkin.

## JOIN

```python
with Session(engine) as session:
    stmt = (
        select(Talaba.ism, Guruh.nom)
        .join(Guruh, Talaba.guruh_id == Guruh.id)
        .order_by(Talaba.ism)
    )

    for ism, guruh_nomi in session.execute(stmt):
        print(ism, "-", guruh_nomi)
```

**Bog'lanish turlari:**

| Tur | Misol | Qanday |
|-----|-------|--------|
| **One-to-Many** | Guruh → Talabalar | `ForeignKey` "ko'p" tomonda |
| **Many-to-One** | Talaba → Guruh | Teskari tomon |
| **One-to-One** | Foydalanuvchi → Profil | `relationship(uselist=False)` |
| **Many-to-Many** | Talabalar ↔ Kurslar | Oraliq (association) jadval orqali |

> ⚠️ SQLite'da `ForeignKey` cheklovi standart holatda **majburiy tekshirilmaydi**. Majburiy qilish uchun har ulanishda `PRAGMA foreign_keys=ON` yoqiladi. PostgreSQL/MySQL da bu kerak emas.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🛡️ 6. Xatolarni ushlash

```python
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

with Session(engine) as session:
    try:
        session.add(Guruh(nom="PY-12"))      # unique, takrorlanadi
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Bu guruh allaqachon mavjud!")
    except SQLAlchemyError as e:
        session.rollback()
        print("Baza xatosi:", e)
```

| Xato | Sababi |
|------|--------|
| `IntegrityError` | `UNIQUE`, `NOT NULL`, `FOREIGN KEY` cheklovi buzildi |
| `NoResultFound` | `.one()` hech narsa topmadi |
| `MultipleResultsFound` | `.one()` bittadan ko'p topdi |
| `SQLAlchemyError` | Barcha SQLAlchemy xatolarining umumiy klassi |

> ⚠️ Xato bo'lsa `session.rollback()` chaqirish shart, aks holda sessiya "buzilgan" holatda qoladi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💡 7. Amaliy misol: Repository klassi

Baza bilan ishlashni bitta klassga yig'ish (27-dars 9-masalaning ORM varianti):

```python
from sqlalchemy import create_engine, select, func, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Talaba(Base):
    __tablename__ = "talabalar"

    id: Mapped[int] = mapped_column(primary_key=True)
    ism: Mapped[str] = mapped_column(String(50))
    yosh: Mapped[int]
    ball: Mapped[float] = mapped_column(default=0.0)

    def __repr__(self):
        return f"Talaba({self.id}, {self.ism!r}, ball={self.ball})"


class TalabaDB:
    def __init__(self, url="sqlite:///maktab.db"):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)

    def qosh(self, ism, yosh, ball=0.0):
        with Session(self.engine) as session:
            t = Talaba(ism=ism, yosh=yosh, ball=ball)
            session.add(t)
            session.commit()
            return t.id

    def hammasi(self):
        with Session(self.engine) as session:
            return session.scalars(select(Talaba).order_by(Talaba.id)).all()

    def topish(self, id):
        with Session(self.engine) as session:
            return session.get(Talaba, id)

    def yangila(self, id, **maydonlar):
        with Session(self.engine) as session:
            t = session.get(Talaba, id)
            if t is None:
                return False
            for kalit, qiymat in maydonlar.items():
                setattr(t, kalit, qiymat)
            session.commit()
            return True

    def ochir(self, id):
        with Session(self.engine) as session:
            t = session.get(Talaba, id)
            if t is None:
                return False
            session.delete(t)
            session.commit()
            return True

    def ortacha_ball(self):
        with Session(self.engine) as session:
            return session.scalar(select(func.avg(Talaba.ball)))


db = TalabaDB()

id = db.qosh("Ali", 20, 85)
db.qosh("Vali", 22, 92)

print(db.hammasi())
db.yangila(id, ball=95, yosh=21)
print(db.topish(id))
print("O'rtacha:", db.ortacha_ball())
db.ochir(id)
```

> `Session` dan chiqqandan keyin ham obyekt atributlarini o'qish mumkin bo'lishi uchun `Session(engine, expire_on_commit=False)` ishlatiladi. Aks holda `commit()` dan keyin obyekt atributlari "eskirgan" bo'ladi va yopilgan sessiyada ularni o'qishga urinish xato beradi. Yuqoridagi `qosh()` da `t.id` ni `with` ichida qaytarganimiz uchun muammo bo'lmadi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🚀 8. FastAPI bilan ulash (28-dars)

SQLAlchemy odatda FastAPI bilan birga ishlatiladi. Har so'rovga alohida sessiya `Depends` orqali beriladi:

```python
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker

engine = create_engine("sqlite:///maktab.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class TalabaModel(Base):                       # jadval (SQLAlchemy)
    __tablename__ = "talabalar"

    id: Mapped[int] = mapped_column(primary_key=True)
    ism: Mapped[str] = mapped_column(String(50))
    yosh: Mapped[int]


class TalabaIn(BaseModel):                     # kiruvchi ma'lumot (Pydantic)
    ism: str
    yosh: int


class TalabaOut(TalabaIn):                     # chiquvchi ma'lumot (Pydantic)
    id: int
    model_config = {"from_attributes": True}   # ORM obyektidan o'qishga ruxsat


Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    with SessionLocal() as db:
        yield db


@app.get("/talabalar", response_model=list[TalabaOut])
def hammasi(db: Session = Depends(get_db)):
    return db.scalars(select(TalabaModel)).all()


@app.get("/talabalar/{talaba_id}", response_model=TalabaOut)
def bittasi(talaba_id: int, db: Session = Depends(get_db)):
    t = db.get(TalabaModel, talaba_id)
    if t is None:
        raise HTTPException(status_code=404, detail="Talaba topilmadi")
    return t


@app.post("/talabalar", response_model=TalabaOut, status_code=201)
def qosh(talaba: TalabaIn, db: Session = Depends(get_db)):
    t = TalabaModel(**talaba.model_dump())
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


@app.delete("/talabalar/{talaba_id}", status_code=204)
def ochir(talaba_id: int, db: Session = Depends(get_db)):
    t = db.get(TalabaModel, talaba_id)
    if t is None:
        raise HTTPException(status_code=404, detail="Talaba topilmadi")
    db.delete(t)
    db.commit()
```

| Qism | Vazifasi |
|------|----------|
| `sessionmaker` | Sessiya yaratuvchi "fabrika" |
| `get_db()` + `Depends` | Har so'rovga sessiya beradi va oxirida yopadi |
| `check_same_thread=False` | SQLite'ni FastAPI ko'p oqimli muhitida ishlatish uchun |
| `from_attributes` | Pydantic ORM obyektidan ma'lumot o'qiy olishi uchun |
| `db.refresh(t)` | `commit()` dan keyin yangi `id` ni yuklaydi |

> Ikki xil model bor: **SQLAlchemy modeli** (bazadagi jadval) va **Pydantic modeli** (API orqali kiruvchi/chiquvchi ma'lumot). Ular turli vazifa bajaradi.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🧰 Foydali buyruqlar

| Kod | Vazifasi |
|-----|----------|
| `Base.metadata.create_all(engine)` | Jadvallarni yaratadi |
| `Base.metadata.drop_all(engine)` | Barcha jadvallarni o'chiradi |
| `create_engine(url, echo=True)` | SQL so'rovlarni konsolga chiqaradi |
| `session.flush()` | O'zgarishni bazaga yuboradi (commit qilmasdan), `id` olish uchun |
| `session.expunge(obj)` | Obyektni sessiyadan ajratadi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ✍️ Mustaqil ishlash uchun topshiriqlar

1. `sqlalchemy` ni o'rnating va `echo=True` bilan `sqlite:///dukon.db` ga ulaning.
2. `Mahsulot` modelini yarating: `id`, `nom`, `narx`, `miqdor`.
3. `create_all()` bilan jadvalni yarating va `.db` fayl paydo bo'lganini tekshiring.
4. `add_all()` bilan 5 ta mahsulot qo'shing.
5. Narxi 10000 dan katta mahsulotlarni `where()` bilan toping.
6. Mahsulotlarni narx bo'yicha kamayish tartibida chiqaring (`order_by`, `desc`).
7. Bitta mahsulot narxini obyekt orqali o'zgartiring (`session.get` → `commit`).
8. `update()` bilan barcha mahsulot narxini 10% oshiring.
9. `delete()` bilan miqdori 0 bo'lgan mahsulotlarni o'chiring.
10. `func.count()`, `func.avg()`, `func.max()` yordamida statistika chiqaring.
11. `Kategoriya` va `Mahsulot` jadvallarini `ForeignKey` va `relationship` bilan bog'lang, `JOIN` qiling.
12. `MahsulotDB` repository klassini yozing (qo'shish, topish, yangilash, o'chirish).
13. 28-darsdagi FastAPI CRUD'ni lug'at o'rniga SQLAlchemy bilan qayta yozing.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📝 Xulosa

- **ORM** jadvalni klass, qatorni obyekt sifatida ishlatish imkonini beradi, **SQLAlchemy** esa Python'dagi asosiy ORM.
- Asosiy qismlar: **Engine** (ulanish), **Model** (jadval klassi), **Session** (baza bilan ishlash).
- Model `DeclarativeBase` dan meros olinadi, ustunlar `Mapped[...]` va `mapped_column()` bilan yoziladi.
- `Base.metadata.create_all(engine)` jadvallarni yaratadi.
- **CRUD:** `session.add()`, `select()`, atributni o'zgartirish yoki `update()`, `session.delete()` yoki `delete()`.
- O'zgarishlar `session.commit()` bilan saqlanadi, xatoda `session.rollback()`.
- `where()`, `order_by()`, `limit()`, `func.count()`, `group_by()` SQL'ning `WHERE`, `ORDER BY`, `LIMIT`, `COUNT`, `GROUP BY` ga mos.
- Jadvallarni bog'lash: `ForeignKey` + `relationship()`.
- FastAPI bilan: `sessionmaker` va `Depends(get_db)` orqali har so'rovga alohida sessiya beriladi.

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