'''
Логическая функция F задаётся выражением (x ∨ y) → (z ≡ x).
Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.

1   2   3   F
?	0	0	0
?	0	?	0

В ответе напишите буквы x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала — буква, соответствующая первому столбцу; затем — буква, соответствующая второму столбцу, и т. д.). 
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

The logical function F is defined by the expression:
(x ∨ y) → (z ≡ x)

A partially filled fragment containing non-repeating rows from the truth table of the function F is given.
Determine which column of the truth table corresponds to each variable x, y, and z.

1   2   3   F
?   0   0   0
?   0   ?   0

In your answer, write the letters x, y, z in the order corresponding to the columns of the truth table (first — the letter corresponding to the first column; then — the letter for the second column; and so on).
Write the letters together without any separators.
'''

print("x y z")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x or y) <= (z == x)):
                print(x, y, z)