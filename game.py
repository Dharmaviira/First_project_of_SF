# """Игра угадай число"""

# import numpy as np

# number = np.random.randint(1, 101) # загадываем число

# # количество попыток
# count = 0

# while True:
#     count+=1
#     predict_number = int(input("Угадай число от 1 до 100: "))
    
#     if predict_number > number:
#         print("Число должно быть меньше!")

#     elif predict_number < number:
#         print("Число должно быть больше!")
    
#     else:
#         print(f"Вы угадали число! Это число = {number}, за {count} попыток")
#         break #конец игры выход из цикла
# users = [
#         [15634602, 15647311, 15619304, 15701354], # id
#         ['Hargrave', 'Hill', 'Onio', 'Boni'], # фамилия
#         [619, 608, 502, 699], # кредитный рейтинг
#         ['Female', 'Female', 'Female', 'Female'], # пол
#         [42, 41, 42, 39], # возраст
#         [1, 0, 1, 0] # статус (1 - клиент активен, 0 - ушел)
#          ]

# print(sum(users[2][::2]) / len(users[2][::2]))

# print(f"{users[1][0]} ({users[0][0]}), {users[1][2]} ({users[0][2]})") 

# from collections import OrderedDict

# data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
# # Сортируем по второму значению из кортежа, то есть по возрасту
# ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[0]))
# print(ordered_client_ages)

# from collections import OrderedDict

# ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
#            ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
#            ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

# cafes = OrderedDict(sorted(ratings, key=lambda x: ( -x[1], x[0])))

# print(cafes)

import numpy as np


# print(np.iinfo(np.uint64))
print(np.finfo(np.float128))