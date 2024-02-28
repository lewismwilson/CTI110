# Lewis Wilson
# 27 February 2024
# P2HW1
# a prettier travel expenses calculator

print('This program calculates and displays travel expenses')
your_budget = float(input('Enter Budget: '))
your_destination = input('Enter your travel destination: ',)
est_gas = float(input('How much do you think you will spend on gas? '))
est_accom = float(input('Approximately, how much will you need for accomodation/hotel? '))
est_food = float(input('Lastly, how much do you need for food? '))
your_expenses = est_gas + est_accom + est_food
print('------------Travel Expenses------------')
print('Location:          ', your_destination)
print('Initial Budget:    ', f'${your_budget:.2f}')
print('Fuel:              ', f'${est_gas:.2f}')
print('Accomodation:      ', f'${est_accom:.2f}')
print('Food:              ', f'${est_food:.2f}')
print('---------------------------------------')
print('Remaining Balance: ', f'${your_budget - your_expenses:.2f}')

# Retrieve the user's estimated budget and store it into the variable 'your_budget'
# Retrieve the user's destination and store it into the variable 'your_destination'
# Retrieve the user's estimated gas expenses and store it into the variable 'est_gas'
# Retrieve the user's estimated accomodations expense and store it into the variable 'est_accom'
# Retrieve the user's estimated food expemse and store it into the variable 'est_food'
# Add the values for the estimated costs (est_gas plus est_accom plus eest_food) and store the value in the variable 'your_expenses'
# Print each value labeled accordingly and print the value of 'your_budget' minus 'your_expenses' displayed as "Remaining Balance:"

