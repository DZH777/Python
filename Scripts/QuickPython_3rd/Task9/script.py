def test(*args):
    rev = list(args)
    rev.reverse()
    return rev

print(test(1,2,3,4,5,6,7))
