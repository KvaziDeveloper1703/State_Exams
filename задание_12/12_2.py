'''
Исходная строка: одна цифра 1, за которой следуют 80 подряд идущих цифр 8.
То есть строка имеет вид: "1888888...888" (всего 81 символ: 1 и 80 восьмёрок).

Выполняется следующий алгоритм:

НАЧАЛО

ПОКА в строке встречается "18" ИЛИ "288" ИЛИ "3888":
    ЕСЛИ в строке есть "18":
        заменить первое вхождение "18" на "2"
    ИНАЧЕ ЕСЛИ в строке есть "288":
        заменить первое вхождение "288" на "3"
    ИНАЧЕ:
        заменить первое вхождение "3888" на "1"
КОНЕЦ ПОКА
КОНЕЦ

Заменяется только первое найденное вхождение соответствующей подстроки.
Нужно определить, какой будет финальная строка после завершения всех замен.
В ответ нужно записать только получившуюся строку.

Initial string: one digit 1 followed by 80 consecutive digits 8.
So the string looks like: "1888888...888" (a total of 81 characters: one "1" and eighty "8"s).

The following algorithm is applied:

START

WHILE the string contains "18" OR "288" OR "3888":
    IF the string contains "18":
        replace the first occurrence of "18" with "2"
    ELSE IF the string contains "288":
        replace the first occurrence of "288" with "3"
    ELSE:
        replace the first occurrence of "3888" with "1"
END WHILE
END

Only the first occurrence of a matching pattern is replaced in each step.
You need to determine what the final string looks like after all replacements are done.
Write only the resulting string as your answer.
'''

sequence = '1' + '8' * 80

while '18' in sequence or '288' in sequence or '3888' in sequence:
    if '18' in sequence:
        sequence = sequence.replace('18', '2', 1)
    elif '288' in sequence:
        sequence = sequence.replace('288', '3', 1)
    else:
        sequence = sequence.replace('3888', '1', 1)

print(sequence)