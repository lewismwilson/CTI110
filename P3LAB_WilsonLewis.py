#Lewis Wilson
#11 March 2024
#P3LAB
#checks if a given year is a leap year or not

is_leap_year = False
is_century = False
   
input_year = int(input())

if input_year%100 == 0:
    is_century = True
    
elif input_year%4 == 0:
    is_leap_year = True
    
else:
    is_leap_year = False
    
if is_century == True and input_year%400 == 0:
    is_leap_year = True
    
if is_leap_year == True:
    print(input_year, '- leap year')
        
else:
    print(input_year, '- not a leap year')


#Sets intial variables for leap year and century as 'False'
#Recieve a year from user input and check if it a century year by seeing if it is evenly divisible by 100.
#If it is, the century variable is set to 'True', otherwise it will remain 'False'
#Checks if the input year is evenly divisible by four.
#If it is, the leap year variable is set to 'True', otherwise it will remain 'False'.
#Checks if a century year is also evenly divisible by 400.
#If it is, the leap year variable is set to 'True', otherwise, it is set to 'False'
#Print "(input year) - leap year" if the leap year variable is 'True'.
#Print "(input year) - not a leap year" if the leap year variable is 'False'.
