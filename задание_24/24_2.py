'''
Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
Определите максимальную длину цепочки вида XYZXYZXYZ...
Для выполнения этого задания необходимо написать программу.

The text file contains no more than 10**6 characters, consisting of X, Y, and Z.
Determine the maximum length of a sequence of the form XYZXYZXYZ...
To solve this problem, you need to write a program.
'''

text_line = open('24_2.txt').readline()

current_length = 0
maximum_length = 0

for index in range(len(text_line)):
    current_char = text_line[index]

    if (current_char == 'X' and current_length % 3 == 0) or \
       (current_char == 'Y' and current_length % 3 == 1) or \
       (current_char == 'Z' and current_length % 3 == 2):
        
        current_length += 1
        maximum_length = max(maximum_length, current_length)

    elif current_char == 'X':
        current_length = 1

    else:
        current_length = 0

print(maximum_length)