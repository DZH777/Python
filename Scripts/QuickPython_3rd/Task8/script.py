""" Читает файл и возвращает количество строк, слов
    и символов - по аналогии с утилитой UNIX wc
"""
infile = open('word_count.tst') # Открывает файл
lines = infile.read().split("\n") #Читает файл с разбивкой по строкам
line_count = len(lines) #Определяет количество строк функцией len()
word_count = 0 #Инициализирует другие счетчики
char_count = 0 #Инициализирует другие счетчики
for line in lines: #Перебирает строки файла
    words = line.split() #Выполняет разбивку по словам
    word_count += len(words) 
    char_count += len(line) #Возвращает количество символов
print("File has {0} lines, {1} words, {2} characters".format
                (line_count, word_count, char_count)) #Выводит результаты


"Better version"
# initialze counts
line_count = 0
word_count = 0
char_count = 0

# open the file
with  open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                               word_count, char_count))
