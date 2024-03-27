# Lewis Wilson
# 27 March 2024
# P4LAB2
# Output increments of 5

int1 = int(input())
int2 = int(input())
num = 0

if int2 < int1:
    print("Second integer can't be less than the first.")
elif int2 >= int1:
    num = int1
    while num <= int2:
        print(num, end=" ")
        num += 5
    print()

# Program recieves two integers from input and checks if the second integer is
# less than the first. If it is, a message is displayed saying that it can't be.
# If the second integer is greater than the first, then a while loop prints integers
# in increments of 5 starting with the first given integer and ending with the
# second given integer. 
