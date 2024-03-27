# Lewis Wilson
# 11 March 2024
# P4HW2
# This program determines and display multiple employee's pay stats. 

employee = ''
overtime_total = 0
salary_total = 0
employees = []

while employee != "Done":
    
    overtime = 0
    overtime_hours = 0
    employee = input('Enter employee\'s name or "Done" to terminate: ')
    if employee == 'Done':
        print()
        break
    else:
        hours = float(input("Enter number of hours worked: "))
        pay_rate = float(input("Enter employee's pay rate: "))

        salary = hours * pay_rate
        
        employees.append(employee)

        if hours > 40:
            overtime_hours = hours - 40
            overtime = overtime_hours * (pay_rate * 1.5)
            salary = (40 * pay_rate) + overtime
            overtime_total += overtime
            
        salary_total += salary
            
        
        print('--------------------------------------')
        print('Employee name:   ', employee)
        print()
        print("Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
        print('--------------------------------------------------------------------------------')
        print(f'{hours:<16.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime:<16.2f}{salary - overtime:<15.2f}{salary:.2f}')
        print()


print(f'Total number of employees entered: {len(employees)}')
print(f'Total amount paid for overtime: ${overtime_total:.2f}')
print(f'Total amount paid for regular hours: ${salary_total-overtime_total:.2f}')
print(f'Total amount paid in gross: ${salary_total:.2f}')

# Recieve an employee's name(or enter 'Done' to end the program and display totals), number of hours worked and their pay rate. Their name is entered into a
# list of employees.
# Overtime and overtime hours are initially set to zero to ensure they don't recieve extra pay if they haven't worked extra hours.
# Salary is calculated and stored in it's respective variable and added to Salary Total.
# Overtime hours and pay are calculated and stored in their respective variables, and salary is recalculated. Overtime is added to the Overtime Total.
# Employee's name and stats are displayed on screen in their respective columns.
# Once 'Done' is entered, total number of employees is displayed along with Total Overtime paid, Total regular hours paid, and Gross salary paid.

