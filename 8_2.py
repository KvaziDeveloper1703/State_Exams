set_of_characters = "ЕСАУЛ"
counter = 0

for character1 in set_of_characters:
    for character2 in set_of_characters:
        for character3 in set_of_characters:
            for character4 in set_of_characters:
                for character5 in set_of_characters:
                    word = character1 + character2 + character3 + character4 + character5
                    if word.count("Е") == 1 and word.count("С") == 1 and word.count("А") == 1 and word.count("У") == 1 and word.count("Л") == 1:
                        if word.count("ЕА") == 0 and word.count("ЕУ") == 0 and word.count("АЕ") == 0 and word.count("УЕ") == 0 and word.count("АУ") == 0 and word.count("УА") == 0:
                            counter = counter + 1

print(counter)