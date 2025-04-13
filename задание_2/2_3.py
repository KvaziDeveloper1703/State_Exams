'''
Логическая функция F задаётся выражением (x ≡ (w ∨ y)) ∨ ((w → z) ∧ (y → w)).
Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

1	2	3	4	F
1   ?   ?   1   0
?	?	?	1	0
1	?	1	?	0

В ответе напишите буквы w, x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала — буква, соответствующая первому столбцу; затем — буква, соответствующая второму столбцу, и т. д.). Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

The logical function F is defined by the expression: F = (x ≡ (w ∨ y)) ∨ ((w → z) ∧ (y → w)).
A partially filled fragment of the truth table for function F is given below. The rows contain unique combinations of variable values.

1	2	3	4	F
1	?	?	1	0
?	?	?	1	0
1	?	1	?	0

Determine which variable corresponds to each column of the truth table (columns 1 to 4, excluding F). Each variable (w, x, y, z) appears exactly once.
In your answer, write the letters w, x, y, z in the order corresponding to the columns of the truth table — first the letter for the first column, then the second, and so on. Do not use any separators between the letters.
'''

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x == (w or y)) or ((w <= z) and (y <= w))):
                    print(x, y, z, w)