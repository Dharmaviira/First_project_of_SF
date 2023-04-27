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
# print(np.finfo(np.float128))

# print(np.sctypeDict)
# arr = np.array([1,5,2,9,10], dtype=np.int8)
# print(arr.dtype)


# mystery = np.array(
#     [[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
#      [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
#      [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
#      [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
#      [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
#      [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
#       dtype=np.int16)

# # elem_5_3 = mystery[4,2]
# # last = mystery[5,6]
# # line_4 = mystery[3] 
# # col_2 = mystery[:,5]
# part = mystery[1:4, 2:5]
# rev = mystery[:, -1][::-1]
# # trans = mystery.transpose()

# mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
#         -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
#         29810.], dtype=np.float32)

# nans_index = np.isnan(mystery)
# n_nan = 0
# for a in nans_index: 
#     if a == True: 
#         n_nan += 1      
# mystery_new = mystery.copy()
# mystery_new[np.isnan(mystery_new)] = 0
# mystery_int = np.int32(mystery)
# array = np.sort(mystery)
# table = array.reshape((5,3) , order='F')
# col = table[:,1]

# print(col)

# print(np.random.rand(2, 3, 4, 10, 12, 23))

import numpy as np
np.random.seed(2021)

simple = np.random.rand()
randoms = np.random.uniform(-150,2021, size = 120)
table = np.random.randint(1, 100 , size = (3,2)) 

print(table)