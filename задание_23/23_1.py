'''
Исполнитель ТР4 преобразует число на экране с помощью двух команд:
+ Прибавить 1 — увеличивает число на экране на 1;
+ Умножить на 2 — умножает число на 2.

Программа для исполнителя ТР4 — это последовательность команд, применяемых к числу.

Сколько существует различных программ, которые:
+ преобразуют исходное число 2 в число 35;
+ при этом траектория вычислений содержит число 15;
+ и не содержит число 31?

The TR4 executor transforms the number on the screen using two commands:
+ Add 1 — increases the current number by 1;
+ Multiply by 2 — multiplies the current number by 2.

A program for the TR4 executor is a sequence of commands applied to a number.

How many different programs:
+ transform the initial number 2 into 35;
+ and the trajectory of calculations contains the number 15;
+ but does not contain the number 31?
'''

def count_paths(start, end):
    if start > end or start == 31:
        return 0

    if start == end:
        return 1

    paths_via_increment = count_paths(start + 1, end)
    paths_via_double = count_paths(start * 2, end)

    return paths_via_increment + paths_via_double

total_paths = count_paths(2, 15) * count_paths(15, 35)

print(total_paths)