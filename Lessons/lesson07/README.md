<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=009650&height=180&section=header&text=LESSON%2007%20%E2%80%94%20NAJOT%20TA'LIM&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

</div>

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📌 GitHub bilan tanishish

**[GitHub](https://github.com/)** — dasturchilar kodni saqlaydigan, boshqalar bilan birga ishlaydigan va o'zgarishlar tarixini yuritadigan onlayn platforma. U **Git** versiyalarni boshqarish tizimi asosida ishlaydi.

**Asosiy tushunchalar:**

| Tushuncha | Tavsif |
|-----------|--------|
| **Git** | Kod o'zgarishlarini kuzatuvchi dastur (kompyuteringizda ishlaydi) |
| **GitHub** | Git repozitoriylarini onlayn saqlovchi platforma |
| **Repository (repo)** | Loyiha papkasi, barcha fayllar va tarixi bilan |
| **Commit** | O'zgarishlarning saqlangan "surati" |
| **Push** | Lokal o'zgarishlarni GitHub'ga yuborish |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 📥 1. `git clone`

**Ta'rif:** GitHub'dagi repozitoriyni kompyuterga nusxalab oladi.

```bash
git clone <repo_url>
```

**Misol:**

```bash
git clone https://github.com/username/my-project.git
```

> Klon qilingandan so'ng loyiha nomi bilan yangi papka yaratiladi. `cd my-project` buyrug'i bilan unga kiring.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# ➕ 2. `git add`

**Ta'rif:** o'zgargan faylni commit uchun tayyorlaydi (staging area'ga qo'shadi).

```bash
git add fayl_nomi
```

**Misol:**

```bash
git add main.py
git add .
```

| Buyruq | Vazifasi |
|--------|----------|
| `git add main.py` | Faqat bitta faylni qo'shadi |
| `git add .` | Barcha o'zgargan fayllarni qo'shadi |

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 💾 3. `git commit`

**Ta'rif:** staging'dagi o'zgarishlarni xabar bilan birga saqlaydi.

```bash
git commit -m "xabar"
```

**Misol:**

```bash
git commit -m "main.py fayli qo'shildi"
```

> ⚠️ Xabar qisqa va tushunarli bo'lishi kerak: nima o'zgargani aytilsin.

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🚀 4. `git push`

**Ta'rif:** lokal commit'larni GitHub'ga yuboradi.

```bash
git push
```

**Birinchi marta yuborishda:**

```bash
git push -u origin main
```

<hr style="border: 0; height: 3px; background: #009650; border-radius: 10px;">

# 🔄 Ish jarayoni

```bash
git clone https://github.com/username/my-project.git
cd my-project

# fayl yaratish yoki o'zgartirish

git add main.py
git commit -m "main.py qo'shildi"
git push
```

**Tartib:**

| Qadam | Buyruq | Nima qiladi |
|-------|--------|-------------|
| 1 | `git clone` | Loyihani yuklab oladi |
| 2 | `git add` | O'zgarishni tayyorlaydi |
| 3 | `git commit` | O'zgarishni saqlaydi |
| 4 | `git push` | GitHub'ga yuboradi |

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