class MyError(Exception):
    pass


def exc1():
    try:
        n1 = int(input('First number:'))
        assert (n1 != 0), "n1 == 0"  # PYTHONOPTIMIZE=True in Config
        n2 = int(input('Second number:'))
        print("n2/n1 =", n2/n1)
    except ZeroDivisionError:
        print("ZeroDivisionError")


def exc2():
    try:
        raise MyError("Some information about what went wrong", "777", "Add text")
    except MyError as error:
        print("Situation: {0} with {1} and {2}".format(error.args[0], error.args[1], error.args[2]))


def cell_value(string):
    try:
        return float(string)
    except ValueError:
        if string == "":
            return 0
        else:
            return None


def safe_apply(function, x, y, spreadsheet):
    try:
        return function(x, y, spreadsheet)
    except TypeError:
        return None


def get_val(dic, key):
    try:
        return dic[key]
    except KeyError:
        return None


if __name__ == "__main__":
    x = {"a": 1, "b": 2, "c": 3}
    print(get_val(x, "d"))

