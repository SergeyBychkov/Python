# 1st_task

my_File = open("myFile.txt", "w+", encoding="UTF-8")

answer = True

# Для красоты добавляем перенос строки после каждой фразы пользователя

while answer:
    ask_User = input("Do you want to write smth. in your file? "
                     "Type + for write and - for not: ")
    if ask_User == "+":
        string_For_Write = input("Please, type smth. for your file:\n")
        my_File.write(string_For_Write + "\n")
    else:
        break
my_File.close()

# 2nd_task

my_File = open("myFile.txt", "r", encoding="UTF-8")

content = my_File.read()
each_row = content.split("\n")

# Из-за того, что последний элемент в файле содержит перенос строки на конце,
# создается элемент массива '', который мешает корректному подсчету
each_row = [row for row in each_row if len(row) > 0]
cnt_Row = len(each_row)
print(f"{cnt_Row} rows in our file")
# Считаем, что слова в строке разделены пробелом, тогда

for row in each_row:
    row = row.split(" ")
    print(f"{len(row)} words in row")

my_File.close()


# 3d_task

my_File = open("workers.txt", "r", encoding="UTF-8")

each_row = my_File.read().split("\n")

# Сделаем список из доходов сотрудников, чтобы потом посчитать средней доход
list_Of_Income = []

for row in each_row:
    row_list = row.split(",")
    if int(row_list[1]) < 20000:
        print(f"Less 20000: {row_list[0]}")
    list_Of_Income.append(int(row_list[1]))

print(f"Avg salary is {sum(list_Of_Income) / len(list_Of_Income)}")

my_File.close()

# 4th_task

my_File = open("fourth_task.txt", "r", encoding="UTF-8")
my_File_Final = open("fourth_task_completed.txt", "w", encoding="UTF-8")

my_Dict = {"One": "Один",
           "Two": "Два",
           "Three": "Три",
           "Four": "Четыре"}

for line in my_File:
    line_Array = line.split("\n")
    first_Element = line_Array[0]
    first_Element_array = first_Element.split(" — ")
    # т.е. заменяем первый элемент списка на русский эквивалент из словаря
    first_Element_array[0] = my_Dict[first_Element_array[0]]
    pre_Final_Str = ",".join(first_Element_array)
    final_Str = pre_Final_Str.replace(",", " - ")
    my_File_Final.write(final_Str + "\n")
    print(final_Str)

my_File.close()
my_File_Final.close()

# 5th_task

my_File = open("fifth_task.txt", "w", encoding="UTF-8")

answer = True
sum_Of_Numbers = 0

# т.е. постепенно считаем сумму чисел, введенных пользователем

while answer:
    ask_User = input("Do you want to write number in your file? "
                     "Type + for write and - for not: ")
    if ask_User == "+":
        number_For_Write = input("Please, type number for your file:\n")
        my_File.write(number_For_Write + " ")
    else:
        break
    sum_Of_Numbers += float(number_For_Write)

print(f"Sum of your numbers is {sum_Of_Numbers}")

my_File.close()

# 6th_task

import re

my_File = open("sixth_task.txt", "r", encoding="UTF-8")

content = my_File.read()
content_Array = content.split("\n")
my_Dict = {}


# т.е. нулевое элемент row_Array - название предмета,
# а первый - количество часов
for row in content_Array:
    row_Array = row.split(":")
    find_Numbers = re.findall(r'\d*\.\d+|\d+', row_Array[1])
    # верхний код вернул строку:(
    # нужно конвертировать в числовой тип
    find_Numbers_Num = [float(num) for num in find_Numbers]
    my_Dict[row_Array[0]] = sum(find_Numbers_Num)


my_File.close()


# 7th_task

import json

with open("seventh_task.txt", "r", encoding="UTF-8") as my_File:
    profit_Dict = {}
    list_of_Profit = []
    final_List = []

    for row in my_File:
        row_Array = row.split(".\n")
        first_Element = row_Array[0].replace(".", "")
        first_Element_Array = first_Element.split(" ")
        profit = float(first_Element_Array[2]) - float(first_Element_Array[3])
        profit_Dict[first_Element_Array[0]] = profit
        if profit > 0:
            list_of_Profit.append(profit)

    avg_Profit_Dict = {"avg_Profit": sum(list_of_Profit) / len(list_of_Profit)
                       }
    # т.е. мы сначала закинули значения в словарь для прибыли,
    # а потом закинули созданный словарь в финальный лист
    final_List.append(profit_Dict)
    final_List.append(avg_Profit_Dict)

with open("seventh_task.json", "w", encoding="UTF-8") as final_File:
    json.dump(final_List, final_File)






