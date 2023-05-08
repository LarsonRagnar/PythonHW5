# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# import random
#
# number, power = random.randint(1, 10), random.randint(1, 10)
# print(number, power)
#
#
# def power_number(number, power):
#     if power == 0:
#         return 1
#     else:
#         return number * power_number(number, power - 1)
#
#
# print(power_number(number, power))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

# import random
#
# one_number, two_number = random.randint(1, 4), random.randint(2, 5)
# print(one_number,two_number)
# def addition (one_number,two_number):
#     if two_number ==0:
#         return one_number
#     elif one_number==0:
#         return two_number
#     else:
#         return addition(one_number-1,two_number)+1
# print(addition(one_number,two_number))
