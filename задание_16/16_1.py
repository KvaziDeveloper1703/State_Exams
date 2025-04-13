'''
Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
+ F(1) = 1;
+ F(2) = 3;
+ F(n) = F(n−1) × n + F(n−2) × (n − 1), при n > 2.

Чему равно значение функции F(5)?
В ответе запишите только натуральное число.

The algorithm for calculating the value of the function F(n), where n is a natural number, is defined as follows:
+ F(1) = 1;
+ F(2) = 3;
+ F(n) = F(n−1) × n + F(n−2) × (n − 1), for n > 2.

What is the value of the function F(5)?
In your answer, write only the natural number.
'''

def calculate_recursive_value(n):
    if n == 1:
        return 1

    if n == 2:
        return 3

    previous_value = calculate_recursive_value(n - 1)
    value_before_previous = calculate_recursive_value(n - 2)
    
    result = previous_value * n + value_before_previous * (n - 1)
    return result

print(calculate_recursive_value(5))