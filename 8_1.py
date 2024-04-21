set_of_characters = "АБВГ"
counter = 0

for character1 in set_of_characters:
    for character2 in set_of_characters:
        for character3 in set_of_characters:
            for character4 in set_of_characters:
                for character5 in set_of_characters:
                    word = character1 + character2 + character3 + character4 + character5
                    if word.count("А") == 1:
                        counter = counter + 1

print(counter)