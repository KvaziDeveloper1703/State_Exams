'''
В файле содержится последовательность целых чисел. Элементы последовательности могут принимать значения от –10 000 до 10 000 включительно.
Необходимо определить и записать в ответе:
+ Количество пар подряд идущих элементов, в которых хотя бы одно число делится на 3;
+ Максимальную сумму среди всех таких пар.

Под парой подразумеваются два идущих подряд элемента последовательности.

The file contains a sequence of integers. The elements of the sequence can take values from –10,000 to 10,000, inclusive.
You need to determine and write in your answer:
+ The number of pairs of consecutive elements in which at least one number is divisible by 3;
+ The maximum sum among all such pairs.

A pair refers to two consecutive elements of the sequence.
'''

pair_count = 0
maximum_pair_sum = -20001

with open('17_1.txt') as file:
    number_list = [int(line) for line in file]

for index in range(len(number_list) - 1):
    first_number = number_list[index]
    second_number = number_list[index + 1]

    if (first_number % 3 == 0) or (second_number % 3 == 0):
        pair_count += 1
        current_sum = first_number + second_number
        maximum_pair_sum = max(maximum_pair_sum, current_sum)

print(pair_count, maximum_pair_sum)