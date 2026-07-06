'''1-misol & 2-misol'''
# numbers = [12, 32, 7, 94, 0, 3]
# max_num = numbers[0]
# min_num = numbers[0]

# for number in numbers:
#     if number > max_num:
#         max_num = number
#     if number < min_num:
#         min_num = number

# print(f"Eng katta son: {max_num} ga teng.")
# print(f"Eng kichik son: {min_num} ga teng.")

'''3-misol'''
# numbers = [12, 32, 7, 94, 0, 3, 12, 5, 94]
# set_numbers = []

# for number in numbers:
#     if number not in set_numbers:
#         set_numbers.append(number)

#     # set_numbers.append(number) if number not in set_numbers else None

# print(set_numbers)

'''4-misol'''
# list_1 = [12, 42, 60, 4, 96]
# list_2 = [33, 71, 59, 1, 37]

# # 1-usul
# list_1.extend(list_2) 
# print(list_1)

# # 2-usul
# for i in list_2:
#     list_1.append(i)

# print(list_1)

'''5-misol'''
# numbers = [12, 32, 7, 94, 0, 3, 12, 5, 94]

# # 1-usul
# numbers[::-1]
# print(numbers)

# # 2-usul
# numbers.reverse()
# print(numbers)

'''6-misol'''
# # 1-usul
# numbers = [12, 32, 7, 94, 0, 3, 12, 5, 94]
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

# # 2-usul
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)


'''7-misol'''
# numbers = [12, 32, -7, 94, 0, 3, -12, 5, -94]
# positive = [number for number in numbers if number >= 0]
# print(positive)

'''8-misol'''
# mevalar = ['olma', 'nok', 'shaftoli', 'anjir', 'qulupnay', 'anor', 'uzum']
# for meva in mevalar:
#     if len(meva) >= 5:
#         print(meva)

'''9-misol'''
# mevalar = ['olma', 'nok', 'shaftoli', 'anjir', 'qulupnay', 'anor', 'uzum']
# for meva in mevalar:
#     if meva[0] in 'aouieAOUIE':
#         print(meva)