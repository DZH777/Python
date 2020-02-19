import argparse


def main(pi_database, pi_url_file):
    print("We are going to work with", pi_database)
    print("We are going to scan with", pi_url_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing URLs to read")
    args = parser.parse_args()
    database = args.database
    url_file = args.input
    main(database, url_file)
