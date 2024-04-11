# Lewis Wilson
# 11 April 2024
# P5HW
# A program that gives simple math quizes

import random

guesses = 0
in_quiz = True

def main_menu():
    '''Generates the main menu displaying options for the user to select'''
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit\n')
    pass

def add_quiz():
    '''Generates two random numebrs for user to guess the sum of'''
    global guesses
    a = random.randint(0,9999)
    b = random.randint(0,9999)
    guess = False

    print(f'  {a}')
    print(f'+ {b}')
    user_guess = int(input('Enter answer.\n'))
    while guess == False:
        if user_guess > (a + b):
            guesses += 1
            print('Sorry, your guess is too high.')
            user_guess = int(input('Try again: '))
        elif user_guess < (a + b):
            guesses += 1
            print('Sorry, your guess is too low.')
            user_guess = int(input('Try again: '))
        elif user_guess == (a + b):
            guesses += 1
            print('Congratulations!!! Your answer is correct.')
            print(f'Number of guesses: {guesses}\n')
            guess = True
            guesses = 0
    pass

def sub_quiz():
    '''Generates two random numbers for user to guess difference of'''
    global guesses
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    guess = False

    print(f'  {a}')
    print(f'- {b}')
    user_guess = int(input('Enter answer.\n'))
    while guess == False:
        if user_guess > (a - b):
            print('Sorry, your guess is too high.')
            user_guess = int(input('Try again: '))
            guesses += 1
        elif user_guess < (a - b):
            print('Sorry, your guess is too low.')
            user_guess = int(input('Try again: '))
            guesses += 1
        elif user_guess == (a - b):
                guesses += 1
                print('Congratulations!!! Your answer is correct.')
                print(f'Number of guesses: {guesses}\n')
                guess = True
                guesses = 0
    pass

print('Welcome to Math Quiz\n')
while in_quiz == True:
    main_menu()
    user_quiz = int(input('Please choose one of the menu options: '))
    if user_quiz == 1:
        add_quiz()
    elif user_quiz == 2:
        sub_quiz()
    elif user_quiz == 3:
        print('Thank you for playing...')
        print('Bye!!')
        break
    elif user_quiz > 3 or user_quiz < 1:
        print()
        print("!!!!INVALID ENTRY!!!! Please enter: '1', '2', or '3'\n")
        print('Try again...\n')

# Three functions are defined: one to generate the selection menu, one to generate an addition quiz and one to generate a subtraction quiz.
# The program prompts the user to enter a numbered entry from the Menu and generates the appropriate quiz based on the user's entry.
# If the user's input is not on the menu, they are informed that they made an invalid entry and are asked to try again. Once they begin a quiz,
# if the user enter's an incorrect answer they are told if their guess was 'too high' or 'too low' and are prompted to try again.
# Once they guess correctly, they are congratulated, told how many guesses they made and brought back to the 'Main Menu'to make a new selection.
# Upon giving the correct entry to exit the program, the user is thanked and the program terminates. 
