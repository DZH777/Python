import argparse
from utilities import url_utilities


def main(pi_database, pi_url_file):
    big_world_list = []
    print("We are going to work with", pi_database)
    print("We are going to scan with", pi_url_file)
    urls = url_utilities.load_uls_from_file(pi_url_file)
    for url in urls:
        print("Reading", url)
        page_content = url_utilities.load_page(url)
        words = url_utilities.scrape_page(page_content)
        big_world_list.extend(words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing URLs to read")
    args = parser.parse_args()
    database = args.database
    url_file = args.input
    main(database, url_file)
