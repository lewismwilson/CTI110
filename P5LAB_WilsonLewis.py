# Lewis Wilson
# 11 April 2024
# P5LAB
# Program that tells you how many days were in February on a given year

def days_in_feb(user_year):
	'''Tells how many days were in February of a given year'''
	is_leap_year = False
	is_century = False

	if user_year%100 == 0:
    		is_century = True   
	elif user_year%4 == 0:
    		is_leap_year = True    
	else:
    		is_leap_year = False    
	if is_century == True and user_year%400 == 0:
    		is_leap_year = True
	if is_leap_year == True:
    		return 29
	else:
    		return 28

if __name__ == '__main__':
    user_year = int(input())
    print(f'{user_year} has {days_in_feb(user_year)} days in February.')

#Takes a year as user input and runs it through a function that first determines
#if the year is a century year or not then determines if it is a leap year or not,
#then if it a century year, it determines if it is a leap year or not. Finally
#the function retruns either '29' if the year is a leap year and '28' if it is not.
#The program then prints out a statement saying how many days were in February of
#the given year.
