'''
Операнды арифметического выражения записаны в системах счисления с основаниями 11 и 19:
x341y₁₁ + 56x1y₁₉

В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 305.

Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 305 и укажите его в ответе в десятичной системе счисления.
Основание систем счисления в ответе указывать не нужно.

The operands of the arithmetic expression are written in number systems with bases 11 and 19:
x341y₁₁ + 56x1y₁₉

In these numbers, the variables x and y represent unknown digits that are valid in their respective bases.
Determine the values of x and y for which the value of the given arithmetic expression is the smallest possible and divisible by 305.

For the found values of x and y, calculate the quotient of the expression's value divided by 305, and write your answer in decimal notation.
Do not include the base of the number system in your answer.
'''

valid_results = []

for digit_x in '0123456789A':
    for digit_y in '0123456789A':

        number_base11_str = digit_x + '341' + digit_y
        number_base11 = int(number_base11_str, 11)

        number_base19_str = '56' + digit_x + '1' + digit_y
        number_base19 = int(number_base19_str, 19)

        total_sum = number_base11 + number_base19

        if total_sum % 305 == 0:
            valid_results.append(total_sum)

if valid_results:
    minimal_divisible_result = min(valid_results)
    print(minimal_divisible_result // 305)