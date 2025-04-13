'''
Исполнитель "Редактор" работает со строкой, состоящей из цифр, и может выполнять две команды (в обеих командах v и w — цепочки цифр):
1)  заменить(v, w) — заменяет первое слева вхождение подстроки v на подстроку w.
    Например, заменить(111, 27) преобразует строку 05111150 в 0527150.
    Если v не встречается в строке, строка остаётся без изменений.

2)  нашлось(v) — проверяет, встречается ли в строке цепочка v.
    Возвращает логическое значение: истина, если v есть в строке, иначе ложь.
    Строка при этом не изменяется.

Также используются конструкции управления:
+ ПОКА условие / КОНЕЦ ПОКА — цикл выполняется, пока условие истинно;
+ ЕСЛИ условие / ТО / ИНАЧЕ / КОНЕЦ ЕСЛИ — условное выполнение команд.

The Editor program processes a string of digits using two types of commands (where v and w are digit sequences):
1)  replace(v, w) — replaces the first occurrence of substring v from the left with substring w.
    Example: replace(111, 27) turns "05111150" into "0527150".
    If the substring v does not exist in the string, no changes are made.

2)  found(v) — checks whether the substring v is present in the string.
    Returns true if found, false otherwise. The string itself remains unchanged.

Control structures used:
+ WHILE condition / END WHILE — repeats the block as long as the condition is true.
+ IF condition / THEN / ELSE / END IF — executes one of two commands based on whether the condition is true or false.
'''

sequence = '8' * 68

while ('222' in sequence) or ('888' in sequence):

    if '222' in sequence:
        sequence = sequence.replace('222', '8', 1)
    else:
        sequence = sequence.replace('888', '2', 1)

print(sequence)