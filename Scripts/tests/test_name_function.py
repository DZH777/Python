import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Igor Joplin' работают правильно?"""
        formatted_name = get_formatted_name('igor', 'joplin')
        self.assertEqual(formatted_name, 'Igor Joplin')

    def test_first_last_middle_name(self):
        """Имена вида 'Igor Joplin Alex' работают правильно?"""
        formatted_name = get_formatted_name('igor', 'joplin', 'alex')
        self.assertEqual(formatted_name, 'Igor Alex Joplin')

unittest.main()
