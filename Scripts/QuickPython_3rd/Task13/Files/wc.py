""" Читает файл и возвращает количество строк, слов и символов - по аналогии с утилитой UNIX wc """
import argparse
import os


def print_result(all_features, count_rows, count_words, count_symbols, max_row_len, count_bytes, arg):
    if all_features:
        print("Количество строк:", count_rows)
        print("Количество слов:", count_words)
        print("Количество символов:", count_symbols)
        print("Максимальная длина строки:", max_row_len)
        print("Количество байт:", count_bytes)
        return
    if arg["l"]:
        print("Количество строк:", count_rows)
    if arg["w"]:
        print("Количество слов:", count_rows)
    if arg["m"]:
        print("Количество символов:", count_rows)
    if arg["L"]:
        print("Максимальная длина строки:", count_rows)
    if arg["c"]:
        print("Количество байт:", count_rows)


def main(file_name, all_features, arg):
    count_rows = 0
    count_words = 0
    count_symbols = 0
    max_row_len = 0
    with open(os.path.abspath(file_name), encoding="utf-8") as infile:  # Открывает файл
        for line in infile:
            count_rows += 1  # Количество строк
            count_words += len(line.split())  # Количество слов
            count_symbols += len(line.strip("\n"))  # Количество символов
            max_row_len = max_row_len if len(line.strip("\n")) < max_row_len else len(line.strip("\n"))  # Максимальная длина строки
    count_bytes = os.path.getsize(os.path.abspath(file_name))  # Количество байт
    print_result(all_features, count_rows, count_words, count_symbols, max_row_len, count_bytes, arg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", default=False, action='store_true', help="wc -l filename - Вывести количество строк")
    parser.add_argument("-w", default=False, action='store_true', help="wc -w filename - Вывести количество слов")
    parser.add_argument("-m", default=False, action='store_true', help="wc -m filename - Вывести количество символов")
    parser.add_argument("-L", default=False, action='store_true', help="wc -L filename - Вывести длину самой длинной "
                                                                       "строки")
    parser.add_argument("-c", default=False, action='store_true', help="wc -c filename - Вывести количество байт")
    parser.add_argument("filename", help="wc filename - Вывести все варианты")
    args = parser.parse_args()
    allfeatures = True
    for el in vars(args):
        if vars(args)[el] is True:
            allfeatures = False
            break
    main(args.filename, allfeatures, vars(args))
