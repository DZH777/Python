"""модуль sole: содержит функции sole, save, show"""
import pickle


_sole_disk_file_s: str = "solecache"
file1 = open(_sole_disk_file_s, 'rb')
_sole_mem_cache_d = pickle.load(file1)
file1.close()


def sole(m, n, t):
    """sole(m, n, t): выполнение вычислений с использованием кэша."""
    global _sole_mem_cache_d
    if (m, n, t) in _sole_mem_cache_d:
        return _sole_mem_cache_d[(m, n, t)]
    else:
        # . . . Очень долгие вычисления . . .
        _sole_mem_cache_d[(m, n, t)] = None  # result
        return None  # result


def save():
    """save(): сохранение обновленного кэша на диске."""
    global _sole_mem_cache_d, _sole_disk_file_s
    file2 = open(_sole_disk_file_s, 'wb')
    pickle.dump(_sole_mem_cache_d, file2)
    file2.close()


def show():
    """show(): вывод кэша."""
    global _sole_mem_cache_d
    print(_sole_mem_cache_d)


# Example intitializate
#  import pickle
#  file = open("solecache",'wb')
#  pickle.dump({}, file)
#  file.close()
