# Lewis Wilson

# 27 Feb 2024

# P2LAB2

# A program that calculates products and averages of given numbers and displays them as integers as well as floating point decimals to the thousandths place.

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
avg = (num1 + num2 + num3 + num4)/4

print(f'{product:.0f} {avg:.0f}')
print(f'{product:.3f} {avg:.3f}')

# Recieve 4 inputs as floats from user.
# Multiply all 4 inputs and store the value in the 'product' variable.
# Add all 4 inputs and divide them by 4 and store the value in the 'avg' variable.
# Print 'product' and 'avg' rounded to a whole number.
# Print 'product' and 'avg' rounded to the third decimal place.
