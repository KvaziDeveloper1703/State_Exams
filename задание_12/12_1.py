'''
Дана строка, состоящая из 68 подряд идущих цифр 8 (то есть "8888...88", 68 символов).
Выполняется следующий алгоритм:

НАЧАЛО

ПОКА в строке встречается "222" ИЛИ "888":
    ЕСЛИ в строке есть "222":
        заменить первое вхождение "222" на "8"
    ИНАЧЕ:
        заменить первое вхождение "888" на "2"
КОНЕЦ ПОКА
КОНЕЦ

Заменяются первые вхождения подстрок. Нужно определить, какая строка получится после завершения всех замен.
В ответе нужно просто записать финальную строку.

A string is given, consisting of 68 consecutive digits 8 (i.e., "8888...88", 68 characters long).
The following algorithm is applied:

START

WHILE the string contains "222" OR "888":
    IF the string contains "222":
        replace the first occurrence of "222" with "8"
    ELSE:
        replace the first occurrence of "888" with "2"
END WHILE
END

Each time, only the first occurrence of the target substring is replaced.
You need to determine what the final string looks like after all replacements are completed.
Write only the resulting string as your answer.
'''

sequence = '8' * 68

while ('222' in sequence) or ('888' in sequence):

    if '222' in sequence:
        sequence = sequence.replace('222', '8', 1)
    else:
        sequence = sequence.replace('888', '2', 1)

print(sequence)