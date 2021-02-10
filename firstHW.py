# 1st_task

# myFirstName = 'Sergey'
#
# mySecondName = 'Bychkov'
#
# myAge = 21
#
# myParams = f'My name is {myFirstName} {mySecondName}, me {myAge}'
# print(myParams)
#
# yourName = input("What's your name?")
# yourAge = int(input("How old are you?"))
#
# if yourAge <= 18:
#     firstWord = 'You are too young!'
# elif yourAge in range(19, 31, 1):
#     firstWord = "That's cool!"
# elif yourAge in range(31, 101, 1):
#     firstWord = "You are too old!"
# else:
#     firstWord = "Don't lie me about your age:)"
#
# print(f"Nice to meet u, {yourName}!\n{firstWord}")

# 2nd_task

# seconds = int(input("Give me seconds, i'll convert it in hh:mm:ss format "))
#
# ss = seconds % 60
#
# mm = seconds // 60
#
# # Обработка случаев, когда в итоговом ответе получается > 60 минут
# # В таком случае просто снижаем количество минут
#
# if mm >= 60:
#     mm = mm % 60
#
# hh = seconds // 3600
#
# # Обработка случаев, чтобы было 05 минут/часов, а не 5 минут/часов
# if mm < 10:
#     mm = f'0{mm}'
# if hh < 10:
#     hh = f'0{hh}'
# if ss < 10:
#     ss = f'0{ss}'
#
# print(f"It's like {hh}:{mm}:{ss}")

# 3d_task

# giveMeN = input("Input random integer, please: ")
# giveMeN_x2 = 2*giveMeN
# giveMeN_x3 = 3*giveMeN
#
# print(int(giveMeN) + int(giveMeN_x2) + int(giveMeN_x3))

# # 4th_task
# # Потом отсюда возьмем максимальное число
# list_of_last_numeric = []
# giveMeNumber = input("Give me random integer > 0 ")
#
# len_of_your_number = len(giveMeNumber)
#
# # Счетчик
# i = 0
# # Каждый раз число будем уменьшать, поэтому используем current_number
# current_number = giveMeNumber
# while i < len_of_your_number:
#     last_Numeric = int(current_number) % 10
#     current_number = int(current_number) // 10
#     list_of_last_numeric.append(last_Numeric)
#     i += 1
#
# print(max(list_of_last_numeric))

# 5th_task

# your_Revenue = input("Tell me about your incomes, friend:)")
# your_Costs = input("Tell me about your costs too:)")
#
# if int(your_Revenue) > int(your_Costs):
#     print('You are real businessman!')
#     # Округляем до десятых
#     profit_rate = (int(your_Revenue) - int(your_Costs)) / int(your_Revenue)
#     print(f'Your profit rate is {profit_rate * 100}%')
#
#     workers = input("How much workers do you have?")
#     profit_rate_by_worker = (int(your_Revenue) - int(your_Costs)) / int(workers)
#     print(f'Your profit by worker is {profit_rate_by_worker}')
#
# elif int(your_Revenue) < int(your_Costs):
#     print("It's not so good:(")
#
# elif int(your_Revenue) == int(your_Costs):
#     print("Okkkey, we got it in next next month")

# # 6th_task
#
# start_Training = int(input("How much km do you run? "))
# stop_Training = int(input("And now how much km do you run?) "))
#
# # Счетчик, чтобы определить номер итерации
# i = 0
#
# while start_Training < stop_Training:
#     start_Training = start_Training * 1.1
#     i += 1
#     if start_Training >= stop_Training:
#         print(f'На {i+1} день спортсмен достиг результата - не менее {stop_Training} км.')

