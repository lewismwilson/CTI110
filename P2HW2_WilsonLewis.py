#Lewis Wilson

#27 February 2024

#P2HW2

#Calculates and displays grades from a list

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

grades_list = [mod1, mod2, mod3, mod4, mod5, mod6]


print('------------Results------------')
print(f'Lowest Grade:      {min(grades_list)}')
print(f'Highest Grade:     {max(grades_list)}')
print(f'Sum of Grades:     {sum(grades_list)}')
print(f'Average:           {sum(grades_list)/len(grades_list):.2f}')
print('----------------------------------------')

# Recieve 6 grades as float inputs one at a time from user and store each value in it's respective 'mod#' variable
# Create a list 'grades_list' that stores each inputed grade
# Print the results displaying the lowest grade in the list, the highest grade in the list, the sum of the grades in the list and the average grade.

