from Employee import Employee


class Worker(Employee):
    def __init__(self, _id, name, address, age, hours_per_day, hour_rate):
        super().__init__(_id, name, address, age)
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate

    def calculate_salary(self):
        salary = self.hours_per_day * self.hour_rate * 22
        return salary

    def __str__(self):
        return f'\n' * 100 + \
               f'Worker\n' + \
               super().__str__() + \
               f'\n' \
               f'Hours_per_day - {self.hours_per_day}\n' \
               f'Hour_rate - {self.hour_rate}\n' \
               f'Salary - {self.calculate_salary()} $\n'
