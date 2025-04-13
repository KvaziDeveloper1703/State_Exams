'''
Сколько различных слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э?
Каждую букву можно использовать неограниченное количество раз (буквы могут повторяться в слове).
Слова не обязательно должны быть осмысленными словами русского языка.

How many different 5-letter words, starting with a vowel, can be formed using the letters E, G, A?
Each letter can be used multiple times (repetition is allowed).
The words do not need to be meaningful in the Russian language.
'''

letters = "ЕГЭ"
vowels = "ЕЭ"
count = 0

for letter_1 in vowels:
    for letter_2 in letters:
        for letter_3 in letters:
            for letter_4 in letters:
                for letter_5 in letters:
                    word = letter_1 + letter_2 + letter_3 + letter_4 + letter_5
                    count += 1
print(count)