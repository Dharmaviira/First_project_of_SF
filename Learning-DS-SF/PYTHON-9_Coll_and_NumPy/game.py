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

# import numpy as np
# np.random.seed(2021)

# simple = np.random.rand()
# randoms = np.random.uniform(-150,2021, size = 120)
# table = np.random.randint(1,101, size = (3,2))
# even = np.arange(2,17,2)
# mix = even.copy()
# np.random.shuffle(mix)
# select = np.random.choice(even, size=3, replace=False)
# triplet = np.random.permutation(select)
# print(select)
# print(triplet)





# def get_chess(a):    
#     b = (a,a)   
#     arr = np.zeros(b)
#     arr[1::2,::2] = 1 
#     arr[::2,1::2] = 1
#     return(arr)
    

# print(get_chess(1))

# Для этого напишите функцию shuffle_seed(<array>),  которая принимает на вход массив из чисел, 
# генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает
# кортеж: перемешанный с данным seed массив (исходный массив должен оставаться без изменений), 
# а также seed, с которым этот массив был получен.


# def shuffle_seed(array):
        
#     seedrand = np.random.randint(2**32-1, dtype=np.uint32)
#     np.random.seed(seedrand)
#     triplet = np.random.permutation(array)

#     return tuple([triplet,seedrand])    

# play_list = (1,2,3,4,5)
# print(shuffle_seed(play_list))



# Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов через запятую. 
# Гарантируется, что все векторы, которые передаются, одинаковой длины.

# Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.


# def min_max_dist (*vector):
     
#     length = vector[1].shape[0]
#     for vec in vector:
#         if length != vec.shape[0]:
#             print("One of your vectors are not of equal lenght!")
#             return
#     distances = []
#     num_vectors = len(vector)
#     for i in range(num_vectors):
#         for j in range(i+1, num_vectors):
#             dist = np.linalg.norm(vector[i] - vector[j])
#             distances.append(dist)
    
    
#         return tuple([np.min(distances), np.max(distances)])

# vec1 = np.array([1,2,3])
# vec2 = np.array([4,5,6])
# vec3 = np.array([7,8,9])

# min_max_dist(vec1, vec2, vec3)


# def any_normal (*vector):
     
#     length = vector[1].shape[0]
#     for vec in vector:
#         if length != vec.shape[0]:
#             print("One of your vectors are not of equal lenght!")
#             return
#     normal = []
#     num_vectors = len(vector)
#     for i in range(num_vectors):
#         for j in range(i+1, num_vectors):
#             dist = np.dot(vector[i], vector[j])
#             normal.append(dist)
#             for a in normal:
#                 if a == 0:
#                     return True
#     return False            
    
# vec1 = np.array([1,2,3])
# vec2 = np.array([4,5,6])

# print(any_normal(vec1, vec2))

# def get_unique_loto(num):
#     arr = []
#     for i in range(num):
#         arr.append(np.random.choice(np.arange(0, 101), size=(5, 5), replace=False))
#     return np.array(arr)

# print(get_unique_loto(5))

# simplelist = [19, 242, 14, 152, 142, 1000]
# A = sum(simplelist)/ len(simplelist)
# print(A)

# a = (6**2 + 8**2)
# b = 24*5
# print(b)