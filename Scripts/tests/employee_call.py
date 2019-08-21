from employee import Employee

new_employee = Employee('владимир', 'иванов', 20000, 'петрович')
new_employee.show_fio()
new_employee.show_salary()
new_employee.give_raise(10000)
new_employee.show_salary()
new_employee.give_raise()
new_employee.show_salary()

