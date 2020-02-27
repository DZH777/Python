import mio
import os


# Using walk function
def using_walk():
    for root, dirs, files in os.walk(os.curdir):
        print("{0} has {1} files".format(root, len(files)))
        # Check dirs with .git name
        if ".git" in dirs:
            # Remove .git from list
            dirs.remove(".git")


def main():
    mio.capture_output()
    using_walk()
    mio.restore_output()
    print("Captured.")
    mio.print_file()
    mio.clear_file()
    print("Printed.")


if __name__ == "__main__":
    main()
