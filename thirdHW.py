# 1st_task

# a = int(input('Type first number: '))
# b = int(input('Type second number: '))
#
#
# def my_function(a: int, b: int):
#     try:
#         print('a / b is: ', a / b)
#     except ZeroDivisionError:
#         print('Division by zero is denied!')
#
#
# my_function(a, b)

# 2nd_task

# name = input('Type your name: ')
# surname = input('Type your surname: ')
# year = int(input('Type your year of birthday: '))
# city = input('Type your city: ')
# e_mail = input('Type your e_mail: ')
# phone = input('Type your phone: ')
#
# def your_params(name, surname, year, city, e_mail, phone):
#     print(f'Oookey, your are {name} {surname}, you {2021 - year}, you are from {city}, '
#           f'your e-mail is {e_mail}, and your numbers is {phone}')
#
#
# your_params(name=name, surname=surname, year=year, city=city, e_mail=e_mail, phone=phone)

# 3d_task

# a = float(input("Please, type any number: "))
# b = float(input("Please, type any number: "))
# c = float(input("Please, type any number: "))
#
# # Из этих цифр потом сделаем список
#
# our_range = a, b, c
#
# #Т.е. сортируем массив, а потом разворачиваем
#
# def my_func(a, b, c):
#     compare_Number = list(our_range)
#     compare_Number.sort()
#     compare_Number.reverse()
#     final = compare_Number[0] + compare_Number[1]
#     print(final)
#
# my_func(a, b, c)

# 4th_task

# x = float(input("Please, type any number: "))
# y = float(input("Please, type any number: "))

# Через **

# def my_func(x, y):
#     print(x ** y)
#
# my_func(x, y)

# Через цикл
# def my_func(x, y):
#     i = 1
#     result = 1
#     while i <= y * -1:
#         result = result * x
#         true = 1 / result
#         i += 1
#     print(true)

# my_func(x, y)

# 5th_task

# Добавляем спец. символы
# from string import punctuation
#
# dinied_Symbols = [_ for _ in punctuation if _ not in ("-", ".")]
# sum_Of_Element = 0
# answer = True
#
# while answer is True:
#     my_Numbers = input("Type any numbers: ").split(" ")
#     for each_Element in my_Numbers:
#         if each_Element in dinied_Symbols:
#             answer = False
#             break
#         sum_Of_Element += float(each_Element)
#     print('Sum of numbers is ', sum_Of_Element)

# 6th_task

# any_Phrase = input("Type any phrase ")

# т.е. сначала заливаем новые элементы в массив, а затем элементы массива джойним в строку


# def int_func(any_Phrase: str):
#     any_Phrase_Array = any_Phrase.split(" ")
#     any_Phrase_Uppercase_array = []
#     for each_word in any_Phrase_Array:
#         each_word = each_word.capitalize()
#         any_Phrase_Uppercase_array.append(each_word)
#     any_Phrase_Uppercase_string = " ".join(any_Phrase_Uppercase_array)
#     return any_Phrase_Uppercase_string
#
#
# print(int_func(any_Phrase))


