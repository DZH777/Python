import argparse
import os
import pathlib
import random
import string


# Files size in the directory
def get_size(path, var):
    size = 0
    if var == 'os':
        for f in os.listdir(path):
            size += os.path.getsize(os.path.join(path, f))
    else:
        for file in path.iterdir():
            size += file.stat().st_size
    return size


# Create files
def create_files(path, reg, cnt):
    if reg == 'U':
        letters = string.ascii_uppercase
    else:
        letters = string.ascii_lowercase
    for i in range(1, cnt):
        f = open(path + '\\text' + str(i) + '.txt', 'w')
        f.write(''.join(random.choice(letters) + str(j) for j in range(i*100)))
        f.close()


# Remove files
def remove_files(path, var):
    if var == 'os':
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
    else:
        for file in path.iterdir():
            file.unlink()


# Using os library
def os_using(pdir):
    print('Before create dir', os.listdir(os.getcwd()))
    os.mkdir(pdir)
    print('After create dir', os.listdir(os.getcwd()))
    create_files(os.path.abspath(os.path.join(os.getcwd(), pdir)), 'U', 20)
    print('After create files', os.listdir(os.path.join(os.getcwd(), pdir)))
    print('Files size', get_size(os.path.abspath(os.path.join(os.getcwd(), pdir)), 'os'))
    remove_files(os.path.abspath(os.path.join(os.getcwd(), pdir)), 'os')
    print('After remove files', os.listdir(os.path.join(os.getcwd(), pdir)))
    os.rmdir(pdir)
    print('After remove dir', os.listdir(os.getcwd()))


# Using pathlib library
def pathlib_using(pdir):
    print('Before create dir', list(pathlib.Path().iterdir()))
    newpath = pathlib.Path(pdir)
    newpath.mkdir(parents=True)
    print('After create dir', list(pathlib.Path().iterdir()))
    create_files(str(newpath.absolute()), 'L', 10)
    print('After create files', list(newpath.iterdir()))
    print('Files size', get_size(newpath.absolute(), 'pathlib'))
    remove_files(newpath.absolute(), 'pathlib')
    print('After remove files', list(newpath.iterdir()))
    newpath.rmdir()
    print('After remove dir', list(pathlib.Path().iterdir()))


# Using walk function
def using_walk():
    for root, dirs, files in os.walk(os.curdir):
        print("{0} has {1} files".format(root, len(files)))
        # Check dirs with .git name
        if ".git" in dirs:
            # Remove .git from list
            dirs.remove(".git")


def main(pdir, pwg):
    os_using(pdir)
    pathlib_using(pdir)
    if pwg:
        using_walk()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--walk", default=False, dest="walk", action='store_true', help="Execute using_walk")
    args = parser.parse_args()
    wg = args.walk
    indir = "textdir"
    main(indir, wg)
