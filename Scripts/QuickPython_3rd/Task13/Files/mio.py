"""mio: модуль (содержит функции capture_output, restore_output, print_file и clear_file )"""
import sys


_file_object = None


def capture_output(file="capture_file.txt"):
    """capture_output(file='capture_file.txt'): перенаправление стандартного вывода в 'file'."""
    global _file_object
    print("output will be sent to file: {0}".format(file))
    print("restore to normal by calling 'mio.restore_output()'")
    _file_object = open(file, 'w')
    sys.stdout = _file_object


def restore_output():
    """restore_output(): восстановление стандартного вывода по умолчанию (также закрывает файл сохранения)"""
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()
    print("standard output has been restored back to normal")


def print_file(file="capture_file.txt"):
    """print_file(file="capture_file.txt"): передача заданного файла в стандартный вывод"""
    f = open(file, 'r')
    print(f.read())
    f.close()


def clear_file(file="capture_file.txt"):
    """clear_file(file="capture_file.txt"): очистка содержимого заданного файла"""
    f = open(file, 'w')
    f.close()
