import re
import string
from urllib.request import urlopen

from bs4 import BeautifulSoup


def load_uls_from_file(file_path: str):
    try:
        with open(file_path) as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("The file", file_path, "could not be found.")
        exit(2)


def load_page(url: str):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    return html


def scrape_page(page_contents: str):
    chicken_noodle = BeautifulSoup(page_contents, "html5lib")
    # remove all javascript and stylesheet code
    for script in chicken_noodle(["script", "style"]):
        script.extract()
    # get text
    text = chicken_noodle.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ' '.join(chunk for chunk in chunks if chunk)
    plain_text = ''.join(filter(lambda x: x in string.printable, text))

    clean_words = []

    words = plain_text.split(" ")
    for word in words:
        clean = True

        # no punctuation
        for punctuation_marks in string.punctuation:
            if punctuation_marks in word:
                clean = False

            # no numbers
            if any(char.isdigit() for char in word):
                clean = False

            # at least two characters but no more than 10
            if len(word) < 2 or len(word) > 10:
                clean = False

            if not re.match(r'^\w+$', word):
                clean = False

            if clean:
                try:
                    clean_words.append(word.lower())
                except UnicodeEncodeError:
                    print(".")

    return clean_words
