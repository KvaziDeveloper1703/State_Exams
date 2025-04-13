'''
В файле содержится последовательность из 10 000 натуральных чисел. Каждое число не превышает 10 000.
Необходимо определить:
+ Количество пар различных элементов последовательности, в которых:
    + остатки от деления на d = 160 — разные;
    + хотя бы одно число делится на p = 7.
+ Максимальную сумму среди всех таких пар.

The file contains a sequence of 10,000 natural numbers. Each number is no greater than 10,000.
You need to determine:
+ The number of pairs of different elements in which:
    + the remainders when divided by d = 160 are different;
    + at least one number is divisible by p = 7.
+ The maximum sum among all such pairs.
'''

with open('17.txt') as file:
    number_list = [int(line) for line in file]

pair_count = 0
maximum_sum = 0

for first_index in range(len(number_list) - 1):
    for second_index in range(first_index + 1, len(number_list)):
        first_number = number_list[first_index]
        second_number = number_list[second_index]

        if (first_number % 160 != second_number % 160) and \
           ((first_number % 7 == 0) or (second_number % 7 == 0)):
            pair_count += 1
            current_sum = first_number + second_number
            maximum_sum = max(maximum_sum, current_sum)

print(pair_count, maximum_sum)