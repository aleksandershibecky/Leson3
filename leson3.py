# c = float(input("Температура в цельсіях: "))
# print (f"Температура у Фаренгейтах: {round,((c * 1.8 + 32),2)}")
#
# c = float(input("Температура в цельсіях: "))
# print ("Температура у Фаренгейтах: " + ("{0:.2f}". format (c * 1.8 + 32)))
#
# x = float(input("Модуль числа: "))
# print(abs(x))

# a = int(input())
# b = int(input())
# c = int(input())
# if (a > 0 or b > 0 and c > 0):
#     print(True)
# else:
#     print(False)

# a = int(input())
# b = int(input())
# c = int(input())
# def f(a,b,c):
#     w = (a > 0 or b > 0 and c > 0)
#     if w == 0:
#         print(False)
#     else:
#         print(True)
#     #return w
# f(a,b,c)


# a = int(input())
# b = int(input())
# c = int(input())
# def election(a, b, c):
#     if a + b + c >= 2:
#         return True
#     return False
# print(election(a, b, c))

# from random import choice
#
#
# def get_votes():
#     '''
#     Функция, которая рандомно генерирует результаты голосования 3х людей
#     :return: x, y, z
#     '''
#     return choice([0, 1]), choice([0, 1]), choice([0, 1])
#
#
# # присваиваю переменным a, b, c значения из выполнения функции
# a, b, c = get_votes()
#
# # принчу результат для понятности
# print(a, b, c)
#
#
# def election(x, y, z):
#     '''
#     Функция, которая определяет результат голосования по переданным голосам.
#     :param x: int[1, 0]  --целое число 0 или 1
#     :param y: int[1, 0] --целое число 0 или 1
#     :param z: int[1, 0] --целое число 0 или 1
#     :return: bool --возвращает булевое значение (true/false)
#     '''
#     if x + y + z >= 2:
#         return True
#     return False
#
#
# # передаю в функцию ранее полученные голоса, принчу результат вызова функции
# print(election(a, b, c))








