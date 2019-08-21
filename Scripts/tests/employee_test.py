import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание сотрудника."""
        self.salary = 20000
        self.salary1 = 25000
        self.salary2 = 32000
        self.my_employee = Employee('владимир', 'иванов', self.salary, 'петрович')

    def test_default_salary(self):
        """Проверяет, что зарплата по умолчанию добавляется."""
        self.my_employee.give_raise()
        self.assertEqual(self.salary + 5000, self.salary1)

    def test_custom_salary(self):
        """Проверяет, что зарплата добавляется."""
        self.my_employee.give_raise(7000)
        self.assertEqual(self.salary + 12000, self.salary2)

unittest.main()
