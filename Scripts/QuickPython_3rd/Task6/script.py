cleaned_words = []
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower().strip() # Привести к одному регистру
        table = line.maketrans(":;!,--.-", "        ") # Удалить знаки препинания
        cleaned_words.extend(line.translate(table).split()) # Разбить на слова
    outfile.write('\n'.join(cleaned_words)) # Записать все слова по одному на строку файла
