'''
Дана строка из 55 цифр, где последняя цифра — 7, а все остальные — 5.
То есть исходная строка выглядит так: "555...557" (54 пятёрки и одна семёрка в конце).

Выполняется следующий алгоритм:

НАЧАЛО

ПОКА в строке встречается "722" ИЛИ "557":
    ЕСЛИ в строке есть "722":
        заменить первое вхождение "722" на "57"
    ИНАЧЕ:
        заменить первое вхождение "557" на "72"
КОНЕЦ ПОКА
КОНЕЦ

На каждом шаге заменяется только первое найденное вхождение.
Нужно определить, какая строка получится после завершения всех замен.
В ответе нужно записать только итоговую строку.

A string of 55 digits is given, where the last digit is 7, and all the other digits are 5.
That is, the initial string looks like: "555...557" (54 fives and one seven at the end).

The following algorithm is executed:

START

WHILE the string contains "722" OR "557":
    IF the string contains "722":
        replace the first occurrence of "722" with "57"
    ELSE:
        replace the first occurrence of "557" with "72"
END WHILE
END

Each step replaces only the first occurrence of a matching pattern.
You need to determine what the final string will be after all replacements are complete.
The answer should be just the resulting string.
'''

sequence = '5' * 54 + '7'

while '722' in sequence or '557' in sequence:
    if '722' in sequence:
        sequence = sequence.replace('722', '57', 1)
    else:
        sequence = sequence.replace('557', '72', 1)

print(sequence)