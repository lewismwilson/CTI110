#Lewis Wilson

#27 March 2024

#P4HW1

#Calculates and displays grades from input


#Function to return a letter grade given a value

def grade_calc(value):
    if value >= 90:
        grade = "A"
    elif value >= 80:
        grade = "B"
    elif value >= 70:
        grade = "C"
    elif value >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


# Asks for a quantity of grades to input and adds them to a list
num_scores = int(input('How many scores do you want to enter? '))
scores = []
a = 1

for i in range(num_scores):
    score = float(input(f'Enter score #{a}: '))
    if score >= 0:
        scores.append(score)
        a += 1
    elif score < 0:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f'Enter score #{a} again: '))
        scores.append(score)
        a += 1

# Calculates the lowest grade, drops it from the list and determines a letter grade for the average score
low_grade = min(scores)
scores.remove(min(scores))
letter_grade = grade_calc(sum(scores)/len(scores))

# Displays the lowest grade, the new scores after dropping the lowest grade, shows the average score and letter grade for the average.
print()
print('------------Results---------------------')
print(f'Lowest Score  :   {low_grade}')
print(f'Modified List :   {scores}')
print(f'Scores Average:   {sum(scores)/len(scores):.2f}') 
print(f'Grade         :   {letter_grade}')
print('----------------------------------------')

# The program starts by creating a function to determine a letter grade from a given value.
# The user is then prompted for a quantity of grades to be entered into a list.
# The user inputs the identified number of scores and they are added to a list one by one.
# The lowest score is identified and droppped from the list. The list is then averaged and given a letter grade.
# The results are displayed for the user to see: "Lowest grade," "Modified list," "Scores Average," and finally "Grade."
