from utilities.url_utilities import load_uls_from_file


def test_load_uls_from_file():
    test_urls = load_uls_from_file("input.txt")
    assert(len(test_urls) > 1)