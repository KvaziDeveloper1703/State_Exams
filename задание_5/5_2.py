'''
Автомат получает на вход четырёхзначное число. По этому числу строится новое число по следующим правилам:
1) Перемножаются первая и вторая, а также третья и четвёртая цифры исходного числа.
2) Полученные два результата записываются друг за другом в порядке убывания (без пробелов и разделителей).

Пример:
Входное число: 2466
Произведения: 2 × 4 = 8, 6 × 6 = 36
Результат: 368 (так как 36 больше 8)

Найдите наименьшее четырёхзначное число, при обработке которого автомат выдаёт число 124.
1) An automatic machine receives a four-digit number as input. Based on this number, it generates a new number according to the following rules:
2) Multiply the first and second digits, and also the third and fourth digits of the original number.

Write down the two resulting products in descending order, without any separators.

Example:
Input number: 2466
Products: 2 × 4 = 8, 6 × 6 = 36
Result: 368 (since 36 is greater than 8)

Find the smallest four-digit number that, when processed by the machine, produces the result 124.
'''

for four_digit_number in range(1000, 10000):
    number_str = str(four_digit_number)
    
    product_first_two_digits = int(number_str[0]) * int(number_str[1])
    product_last_two_digits = int(number_str[2]) * int(number_str[3])
    
    max_product = str(max(product_first_two_digits, product_last_two_digits))
    min_product = str(min(product_first_two_digits, product_last_two_digits))
    
    combined_result = max_product + min_product
    
    if combined_result == '124':
        print(four_digit_number)
        break