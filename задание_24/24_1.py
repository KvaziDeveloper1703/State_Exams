'''
Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
Для выполнения этого задания следует написать программу.

A text file contains no more than 10**6 characters, consisting only of X, Y, and Z.
Determine the maximum number of consecutive characters in which every two adjacent characters are different.
To solve this problem, you need to write a program.
'''

text_line = open('24_1.txt').readline()

current_sequence_length = 1
maximum_sequence_length = 0

for index in range(1, len(text_line)):
    current_character = text_line[index]
    previous_character = text_line[index - 1]

    if current_character != previous_character:
        current_sequence_length += 1
    else:
        maximum_sequence_length = max(maximum_sequence_length, current_sequence_length)
        current_sequence_length = 1

maximum_sequence_length = max(maximum_sequence_length, current_sequence_length)
print(maximum_sequence_length)