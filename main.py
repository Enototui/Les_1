# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день
#выходным.
# day = int(input('Введите день: '))
# if day >= 1 and day < 6:
#     print('Рабочий')
# elif day == 6 or day == 7:
#     print('Выходной')
# else:
#     print('Неверное число')

# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result
#
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# x = int(input('Введите координат точки Х:  '))
# y = int(input('Введите координат точки Y:  '))
# if x > 0 and y > 0:
#     print('1 координатная четверть')
# if x < 0 and y > 0:
#     print('2 координатная четверть')
# if x < 0 and y < 0:
#     print('3 координатная четверть')
# if x > 0 and y < 0:
#     print('4 координатная четверть')

# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).
# num = int(input('Введите номер четверти от 1 до 4: '))
# if num == 1:
#     print('от X до Y')
# elif num == 2:
#     print('от -X до Y')
# elif num == 3:
#     print('от -X до -Y')
# elif num == 4:
#     print('от X до -Y')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
# пространстве.
import math
import os
x_coordinate_A = int(input('Введите X(a): '))
y_coordinate_A = int(input('Введите Y(a): '))
x_coordinate_B = int(input('Введите X(b): '))
y_coordinate_B = int(input('Введите Y(b): '))
distance = round(math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2), 2)
print(distance)
