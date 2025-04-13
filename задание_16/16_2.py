'''
Последовательность трибоначчи задаётся следующим рекуррентным соотношением:
+ F(1) = 0;
+ F(2) = 1;
+ F(3) = 1;
+ F(n) = F(n–3) + F(n–2) + F(n–1), при n > 3, где n — натуральное число.

Чему равно девятое число в последовательности трибоначчи?
В ответе запишите только натуральное число.

The Tribonacci sequence is defined by the following recurrence relation:
+ F(1) = 0;
+ F(2) = 1;
+ F(3) = 1;
+ F(n) = F(n–3) + F(n–2) + F(n–1), for n > 3, where n is a natural number.

What is the ninth number in the Tribonacci sequence?
In your answer, write only the natural number.
'''

def calculate_custom_sequence(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    if n == 3:
        return 1

    value_three_steps_back = calculate_custom_sequence(n - 3)
    value_two_steps_back = calculate_custom_sequence(n - 2)
    value_one_step_back = calculate_custom_sequence(n - 1)

    result = value_three_steps_back + value_two_steps_back + value_one_step_back
    return result

print(calculate_custom_sequence(9))