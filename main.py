# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на нечётной позиции
# spisok = [20, 30, 22, 24, 17]
# randlist = []
# for i in range(len(spisok)):
#     if i % 2 != 0:
#         randlist.append(spisok[i])
# print(sum(randlist))

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д
# my_list = [2, 3, 5, 6]
# res = []
# while len(my_list) > 0:
#             name = my_list.pop(0)
#             name_1 = my_list.pop()
#             sum = name * name_1
#             res.append(sum)
# print(res)

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# num = int(input('Введите число'))
# some = ''
# while num > 0:
#     some = str(num % 2) + some
#     num = num // 2
# print(some)


# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.


spisok = [1.1, 1.2, 3.3, 10.01]
min_num = 1
max_num = 0
for i in spisok:
    if (i - int(i)) <= min_num:
        min_num = i - int(i)
    if (i - int(i)) >= max_num:
        max_num = i - int(i)
print(max_num-min_num)