friends = {
    "Ali": {"Vali", "Hasan", "Akmal"},
    "Vali": {"Ali", "Jasur"},
    "Hasan": {"Ali", "Aziz"},
    "Akmal": {"Ali"},
    "Aziz": {"Hasan"},
}

follow = set()

for friend in friends["Ali"]:
    for new_friend in friends[friend]:
        if new_friend not in friends["Ali"] and new_friend != "Ali":
            follow.add(new_friend)

print(f"Alining do'stlarining do'stlari {follow}")