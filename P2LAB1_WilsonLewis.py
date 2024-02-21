# Lewis Wilson
# 20 February 2024
# P2LAB1
# A program that outputs gas cost for 20, 75, and 500 miles given gas mileage and cost


gas_mileage = float(input())
gas_cost = float(input())

gas_20 = (20 / gas_mileage) * gas_cost
gas_75 = (75 / gas_mileage) * gas_cost
gas_500 = (500 / gas_mileage) * gas_cost

print(f'{gas_20:.2f} {gas_75:.2f} {gas_500:.2f}')
