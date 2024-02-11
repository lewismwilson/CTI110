# Lewis Wilson
# 11 February 2024
# P1HW2
# a travel expenses calculator

print('This program calculates and displays travel expenses')
your_budget = int(input('Enter Budget: '))
your_destination = input('Enter your travel destination: ',)
est_gas = int(input('How much do you think you will spend on gas? '))
est_accom = int(input('Approximately, how much will you need for accomodation/hotel? '))
est_food = int(input('Lastly, how much do you need for food? '))
your_expenses = est_gas + est_accom + est_food
print('------------Travel Expenses------------')
print('Location:', your_destination)
print('Initial Budget:', your_budget)
print()
print('Fuel:', est_gas)
print('Accomodation:', est_accom)
print('Food:', est_food)
print()
print('Remaining Balance:', your_budget - your_expenses)
