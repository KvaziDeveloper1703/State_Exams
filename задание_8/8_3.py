'''
Рассматриваются символьные последовательности длины 5 в алфавите из 6 букв: У, Ч, Е, Н, И, К.
Сколько существует таких последовательностей, которые:
+ начинаются с буквы У,
+ и заканчиваются буквой К?

We consider character sequences of length 5 using a 6-letter alphabet: {U, H, E, N, I, K} (Note: in transliteration, H = Ч, E = Е, etc.)
How many such sequences exist that:
+ start with the letter U,
+ and end with the letter K?
'''

letters = ['У', 'Ч', 'Е', 'Н', 'И', 'К']
count = 0

for letter_2 in letters:
    for letter_3 in letters:
        for letter_4 in letters:
            word = 'У' + letter_2 + letter_3 + letter_4 + 'К'
            count += 1
print(count)