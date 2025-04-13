'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам:
1) Складываются первая и вторая, а также вторая и третья цифры исходного числа.
2) Полученные два значения записываются друг за другом в порядке убывания (без пробелов и разделителей).

Пример:
Входное число: 348
Суммы: 3 + 4 = 7, 4 + 8 = 12
Результат: 127 (так как 12 больше 7, сначала записывается 12, затем 7)

Найдите наименьшее трёхзначное число, при обработке которого автомат выдаёт результат 1412.

An automatic machine receives a three-digit number as input. Based on this number, a new number is generated according to the following rules:
1) Add the first and second digits, and then the second and third digits of the original number.
2) Write down the two resulting sums in descending order, without any separators.

Example:
Input number: 348
Sums: 3 + 4 = 7, 4 + 8 = 12
Result: 127 (because 12 is greater than 7, it comes first)

Find the smallest three-digit number that produces the result 1412 when processed by the machine.
'''

for number in range(100, 1000):
    number_str = str(number)
    
    sum_first_and_second_digits = int(number_str[0]) + int(number_str[1])
    sum_second_and_third_digits = int(number_str[1]) + int(number_str[2])
    
    max_sum = str(max(sum_first_and_second_digits, sum_second_and_third_digits))
    min_sum = str(min(sum_first_and_second_digits, sum_second_and_third_digits))
    
    combined_result = max_sum + min_sum
    
    if combined_result == '1412':
        print(number)
        break