class Employee():
    """Информация о сотруднике."""

    def __init__(self, first_name, last_name, salary, middle_name=''):
        """Сохраняет информацию о сотруднике."""
        self.first_name = first_name
        self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        self.salary = salary
        
    def show_fio(self):
        """Выводит ФИО сотрудника."""
        if self.middle_name:
            print((self.last_name + ' ' + self.first_name + ' ' + self.middle_name).title())
        else:    
            print((self.last_name + ' ' + self.first_name).title())

    def show_salary(self):
        """Выводит зарплату сотрудника."""
        if self.middle_name:
            print((self.last_name + ' ' + self.first_name[:1] + '.' + self.middle_name[:1] + '.').title() + ' - ' + str(self.salary))
        else:   
            print((self.last_name + ' ' + self.first_name[:1] + '.').title() + ' - ' + str(self.salary))

    def give_raise(self, salary=5000):
        """Увеличивает зарплату сотрудника на заданную величину."""
        self.salary += salary
