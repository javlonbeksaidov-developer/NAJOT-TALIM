from random import randint

name = input("Ismingizni kiriting: ")
surname = input("Familiyangizni kiriting: ")

option01 = name + "." + surname
option02 = name + "_" + surname
option03 = name[0] + "." + surname + str(randint(100, 999))
option04 = surname[0] + "." + name

print("Sizning email manzilingiz quyidagicha bo'lishi mumkin:")
print(option01 + "@gmail.com")
print(option02 + "@gmail.com")
print(option03 + "@gmail.com")
print(option04 + "@gmail.com")
