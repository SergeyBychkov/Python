# 1st_task
from functools import reduce
from itertools import count, cycle
from math import factorial
from sys import argv

# def salary_func(*args: float) -> float:
#     """Считаем з/п"""
#     salary = float(args[1]) * float(args[2]) + float(args[3])
#     return salary


# Запускаемся из консольки
# print(salary_func(argv[1:]))

# 2nd_task

# first_List = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Берем индекс > 0, т.к. нулевой элемент не с чем сравнивать

# final_List = [ each_element for index, each_element in enumerate(first_List)
#                if each_element > first_List[index-1] and index > 0 ]
# print(final_List)


# 3d_task

# from_20_to_240 = range(20, 241)
#
# final_List = [each_element for each_element in from_20_to_240 if
#               (each_element % 20 == 0) or (each_element % 21 == 0)]
#
# print(final_List)

# 4th_task

# src_List = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#
# final_List = [each_element for each_element in src_List if
#               src_List.count(each_element) == 1]
#
# print(final_List)

# 5th_task

# src_List = range(100, 1001)
#
# final_List = [each_element for each_element in src_List
#               if each_element % 2 == 0]
#
#
# def composition_func(first_param: int, second_param: int) -> int:
#     """Считаем произведение входных параметров"""
#     return first_param * second_param
#
#
# result = reduce(composition_func, final_List)
#
# print(result)

# 6th_task

# any_List = range(11)
#
# # Первый скрипт
# for el in count(3):
#     if el > 10:
#         break
#     else:
#         print(el)
#
# # Второй скрипт
# i = 0
# for el in cycle(any_List):
#     if i > 21:
#         break
#     print(el)
#     i += 1

# 7th_task

# def factorial_func(any_param: int) -> int:
#     """Создаем генератор и вычисляем факториал"""
#     for element in count(1):
#         yield f"Factorial {element}: {factorial(element)}"
#         if element == any_param:
#             break
#
#
# result = factorial_func(int(input("Please, type any integer: ")))
#
# for each_element in result:
#     print(each_element)
