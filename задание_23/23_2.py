'''
Исполнитель РазДваТри преобразует число на экране с помощью трёх команд:
+ Прибавить 1 — увеличивает текущее число на 1;
+ Умножить на 2 — умножает текущее число на 2;
+ Умножить на 3 — умножает текущее число на 3.

Программа для исполнителя — это последовательность этих команд.

Сколько существует различных программ, которые:
+ преобразуют исходное число 2 в число 44;
+ при этом траектория вычислений содержит число 13;
+ и не содержит число 29?

The RazDvaTri executor transforms a number on the screen using three commands:
+ Add 1 — increases the current number by 1;
+ Multiply by 2 — multiplies the current number by 2;
+ Multiply by 3 — multiplies the current number by 3.

A program is a sequence of these commands.

How many different programs:
+ transform the initial number 2 into 44;
+ whose trajectory of computation contains the number 13;
+ and does not contain the number 29?
'''

def count_paths(start, target):
    if start > target or start == 29:
        return 0

    if start == target:
        return 1

    paths_add_1 = count_paths(start + 1, target)
    paths_multiply_2 = count_paths(start * 2, target)
    paths_multiply_3 = count_paths(start * 3, target)

    return paths_add_1 + paths_multiply_2 + paths_multiply_3

total_paths = count_paths(2, 13) * count_paths(13, 44)

print(total_paths)