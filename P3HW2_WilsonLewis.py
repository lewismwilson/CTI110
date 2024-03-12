# Lewis Wilson
# 11 March 2024
# P3HW2
# This program determines an employee's gross pay

employee = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

overtime = 0
overtime_hours = 0

salary = hours * pay_rate

if hours > 40:
    overtime_hours = hours - 40
    overtime = overtime_hours * (pay_rate * 1.5)
    salary = (40 * pay_rate) + overtime

print('--------------------------------------')
print('Employee name:   ', employee)
print()
print("Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
print('--------------------------------------------------------------------------------')
print(f'{hours:<16.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime:<16.2f}{salary - overtime:<15.2f}{salary:.2f}')

# Recieve an employee's name, number of hours worked and their pay rate
# Overtime and overtime hours are initially set to zero to ensure they don't recieve extra pay if they haven't worked extra hours.
# Salary is calculated and stored in it's respective variable.
# Overtime hours and pay are calculated and stored in their respective variables, and salary is recalculated.
# Employee's name and stats are displayed on screen in their respective columns.

