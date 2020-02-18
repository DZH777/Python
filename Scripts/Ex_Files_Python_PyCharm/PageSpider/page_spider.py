import os
import argparse


def main(database, url_file):
    print("We are going to work with", database)
    print("We are going to scan with", url_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing URLs to read")
    args = parser.parse_args()
    database = args.database
    url_file = args.input
    main(database, url_file)