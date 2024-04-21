set_of_characters = "КБЛА"
counter = 0
for character1 in set_of_characters:
    for character2 in set_of_characters:
        for character3 in set_of_characters:
            for character4 in set_of_characters:
                for character5 in set_of_characters:
                    for character6 in set_of_characters:
                        word = character1 + character2 + character3 + character4 + character5 + character6
                        if word.count("К") == 1 and word.count("Б") == 1 and word.count("Л") == 1 and word.count("А") == 3:
                            if word.count("АА") == 0:
                                counter = counter + 1
print(counter)