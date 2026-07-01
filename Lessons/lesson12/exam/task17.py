
'''
🔹 17. Baholash tizimi
🧮 Vazifa: 0–100 oralig‘idagi ballga qarab baho chiqaring.

✳️ Chegaralar:

[90, 100]: "A (A'lo)"
[80, 89]: "B (Yaxshi)"
[70, 79]: "C (Qoniqarli)"
[60, 69]: "D (Qoniqarsiz)"
[0, 59]: "F (Yomon)"
Aks xolatda: "Ball 0-100 oralig'ida bo'lishi kerak!"
📥 Kirish: 85
📤 Chiqish: "B (Yaxshi)"
'''

ball = int(input("Ball: "))

if 0 <= ball <= 100:
    if 90 <= ball <= 100:
        print("A (A'lo)")
    elif 80 <= ball <= 89:
        print("B (Yaxshi)")
    elif 70 <= ball <= 79:
        print("C (Qoniqarli)")
    elif 60 <= ball <= 69:
        print("D (Qoniqarsiz)")
    elif 0 <= ball <= 59:
        print("F (Yomon)")
else:
    print("0-100 oralig'idagi ballni kiriting: ")