def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(summa(1, 2, 3))
print(summa())     