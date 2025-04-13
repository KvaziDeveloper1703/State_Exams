'''
Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 11:
88x4y₉ + 7x44y₁₁

В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 61.

Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 61 и укажите его в ответе в десятичной системе счисления.
Основание систем счисления в ответе указывать не нужно.

The operands of the arithmetic expression are written in number systems with bases 9 and 11:
88x4y₉ + 7x44y₁₁

In the numbers, the variables x and y represent unknown digits that are valid in the respective bases.
Determine the values of x and y for which the value of the given arithmetic expression is the smallest possible and divisible by 61.

For the found values of x and y, calculate the quotient of the expression's value divided by 61, and write your answer in decimal notation.
Do not include the base of the number system in your answer.
'''

results_divisible_by_61 = []

for digit_x in '012345678':
    for digit_y in '012345678':

        number_base9_str = '88' + digit_x + '4' + digit_y
        number_base9 = int(number_base9_str, 9)

        number_base11_str = '7' + digit_x + '44' + digit_y
        number_base11 = int(number_base11_str, 11)

        total_sum = number_base9 + number_base11

        if total_sum % 61 == 0:
            results_divisible_by_61.append(total_sum)

if results_divisible_by_61:
    smallest_result = min(results_divisible_by_61)
    print(smallest_result // 61)