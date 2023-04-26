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


def brackets(brack):
    norm = 0
    
    for br in brack:
        rend = []
        if br == "(":
            rend.append(br)
            norm =+ 1
        elif br == ")":
            rend.pop(br)
            norm =- 1
    if norm == 0:
        print("Your brackets is right!")
    else:
        print("Your brackets in notright.")
        
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False 


                            
