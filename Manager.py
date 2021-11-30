from Employee import Employee


class Manager(Employee):
    def __init__(self, _id, name, address, age, number_of_employees, employee_rate):
        super().__init__(_id, name, address, age)
        self.number_of_employees = number_of_employees
        self.employee_rate = employee_rate

    def calculate_salary(self):
        salary = self.number_of_employees * self.employee_rate
        return salary

    def __str__(self):
        return f'\n' * 100 + \
               f'Manager\n' + \
               super().__str__() + \
               f'\n' \
               f'Number_of_employees - {self.number_of_employees}\n' \
               f'Employee_rate - {self.employee_rate}\n' \
               f'Salary - {self.calculate_salary()} $'

