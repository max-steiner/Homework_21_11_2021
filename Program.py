from Worker import Worker

from Manager import Manager

print("To register a new employee, input the following data after each entry press key [Enter].\n")
print('##########################\n')

_id = int(input("Enter the id of the employee: "))
name = str(input("Enter the name of the employee: "))
address = str(input("Enter the address of the employee: "))
age = int(input("Enter the age of the employee: "))
position = int(input("Enter the position of the employee: [1] - worker, [2] - manager: "))

while position not in [1, 2]:
    input("=Input error! Enter correct data: ")
    if position in [1, 2]:
        break
if position == 1:
    hours_per_day = int(input("Enter the number of hours that the employee must work daily: "))
    hour_rate = int(input("Enter employee hourly rate: "))
    print(Worker(_id, name, address, age, hours_per_day, hour_rate))
else:
    number_of_employees = int(input("Enter number of employees for the manager: "))
    employee_rate = int(input("Enter employee rate for the manager: "))
    print(Manager(_id, name, address, age, number_of_employees, employee_rate))

