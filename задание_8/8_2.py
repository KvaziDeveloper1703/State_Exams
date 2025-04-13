'''
Игорь составляет таблицу кодовых слов для передачи сообщений. Каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Игорь использует 5-буквенные слова, составленные только из букв П, И, Р, при этом:
+ Буква П должна входить в слово ровно 1 раз.
+ Буквы И и Р могут встречаться любое количество раз, включая 0.

Сколько различных кодовых слов может использовать Игорь?

Igor is creating a table of code words to transmit messages, with each message having its own unique code word.
He uses 5-letter words made only from the letters P, I, and R, under the following conditions:
+ The letter P must appear exactly once in each word.
+ The letters I and R may appear any number of times, including zero.

How many different code words can Igor use?
'''

letters = "ПИР"
count = 0

for letter_1 in letters:
    for letter_2 in letters:
        for letter_3 in letters:
            for letter_4 in letters:
                for letter_5 in letters:
                    word = letter_1 + letter_2 + letter_3 + letter_4 + letter_5
                    if word.count('П') == 1:
                        count += 1
print(count)