# 1st_task

# first_Array = [1, 'SB', True, 2.0, b'SB']
#
# for i in first_Array:
#     print(type(i))

# 2nd_task
# Не совсем понял, где нужно использовать input

# my_Array = list(input("Give me any array: "))
# reversed_Array = []
#
# print(my_Array)

# Проверяем четнось индекса. Если он четный - прибавляем единицу, если нечетный - отнимаем
# Добавляем исключение в случае нечетного количества элементов
# for i, x in enumerate(my_Array):
#     if i % 2 == 0:
#         i = i + 1
#     elif i % 2 != 0:
#         i = i - 1
#     try:
#         reversed_Array.append(my_Array[i])
#     except IndexError:
#         reversed_Array.append(my_Array[-1])
#
# print(reversed_Array)

# 3d_task

# Решение через list
# month_Number = input("Give me month number: ")

# if month_Number in ['1', '2', '12']:
#     print("It's winter!")
# elif month_Number in ['3', '4', '5']:
#     print("It's spring!")
# elif month_Number in ['6', '7', '8']:
#     print("It's summer!")
# elif month_Number in ['9', '10', '11']:
#     print("It's autumn!")
# else:
#     print("You have to type number from 1 to 12!")

# Решение через dict

# dict_Of_Season_Time = {"winter": "1, 2, 12",
#                        "spring": "3, 4, 5",
#                        "summer": "6, 7, 8",
#                        "autumn": "9, 10, 11"
#                        }

# То есть просто правильно разделяем элементы списка

# for key, value in dict_Of_Season_Time.items():
#     if month_Number in value.split(", "):
#         print(key)

# 4th_task

# any_Words = input("Give me any words: ")
#
# # Дробим строку через пробелы в список
# any_Words_list = any_Words.split()
#
# for i, k in enumerate(any_Words_list):
#     print(i, k[:10])

# 5th_task

# my_Rating = [7, 5, 3, 3, 2]
# my_Rating_Reversed = my_Rating[::-1]
#
# any_Number = int(input("Give me any number: "))

# Разворачиваем список и домножаем индекс на -1, если пользователь ввел число, которое есть в списке

# if any_Number > int(max(my_Rating)):
#     my_Rating.insert(0, any_Number)
#
# elif any_Number < int(min(my_Rating)):
#     my_Rating.append(any_Number)
#
# elif any_Number in my_Rating:
#     my_Rating.insert(-1 * my_Rating_Reversed.index(any_Number), any_Number)
#
# print(my_Rating)

# 6th_task

# Вносим в словарь данные пользователя
# Ситаем, что данные вносятся в формате <что-то>,<что-то-1>,<что-то-2> и т.д.
# компьютер,5000,3,шт
# принтер,3000,1,шт
# final_Structure = []
#
# answer = True
# i = 0

#т.е. итеративно вносим товары в корзину
# while answer is True:
#
#     give_Me_Any_Items = input("Please, type any item and its characteristics: ")
#     give_Me_Any_Items_array = give_Me_Any_Items.split(",")
#     my_Structure = {"Название": give_Me_Any_Items_array[0::4],
#                     "Цена": give_Me_Any_Items_array[1::4],
#                     "Количество": give_Me_Any_Items_array[2::4],
#                     "Ед.": give_Me_Any_Items_array[3::4]
#                     }
#     i += 1
#     element_In_Structure = (i, my_Structure)
#     final_Structure.append(element_In_Structure)
#     do_You_Continue = input("Do you want to continue? \n"
#                             "If you want, type 'yes' or 'no' for not: ")
#     if do_You_Continue.lower() == "yes":
#         continue
#     elif do_You_Continue.lower() == "no":
#         answer = False



# analyze_Structure={"Название": [],"Цена": [],"Количество": [],"Ед.": "шт."}
#
# for i in range(0, len(final_Structure)):
#     analyze_Structure["Название"].append(final_Structure[i][1]["Название"])
#     analyze_Structure["Цена"].append(final_Structure[i][1]["Цена"])
#     analyze_Structure["Количество"].append(final_Structure[i][1]["Количество"])
#
# print(analyze_Structure)









