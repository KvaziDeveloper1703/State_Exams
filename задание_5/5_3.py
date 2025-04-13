'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
+ Строится двоичная запись числа N.
+ К этой записи справа дописываются два разряда по следующему правилу:
    + Сначала вычисляется сумма цифр двоичной записи числа. Остаток от деления этой суммы на 2 (т.е. 0 или 1) дописывается справа к двоичной записи;
    + Затем над новой записью снова выполняется то же действие: находится сумма её цифр, берётся остаток от деления на 2 и дописывается ещё один разряд.
+ Полученная таким образом запись (на два бита длиннее исходной) — это двоичное представление числа R.

Найдите минимальное число R, которое превышает 43 и может быть результатом работы этого алгоритма.
В ответе укажите десятичное значение числа R.

A natural number N is given as input to an algorithm. The algorithm constructs a new number R as follows:
+ Build the binary representation of N.
+ Then two additional bits are appended to this binary number, according to the following rules:
    + First, calculate the sum of the digits (bits) in the binary representation. The remainder of dividing this sum by 2 (i.e. 0 or 1) is appended to the right of the binary number.
    + Then, the same operation is repeated on the new binary number: calculate the sum of its bits, take the remainder modulo 2, and append it to the end.

+ The resulting binary number (which is 2 bits longer than the original) is the binary representation of R.

Find the smallest possible R that is greater than 43 and can be obtained as a result of this algorithm.
Give your answer in decimal form.
'''

for decimal_number in range(1, 100):
    binary_representation = bin(decimal_number)[2:]

    number_of_ones = binary_representation.count('1')

    if number_of_ones % 2 == 0:
        modified_binary = binary_representation + '00'
    else:
        modified_binary = binary_representation + '10'

    result_number = int(modified_binary, 2)

    if result_number > 43:
        print(result_number)
        break