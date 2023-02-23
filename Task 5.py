#Name:                  Task 5.py
#Author:                Derek Baker
#Date Created:          23-02-2023
#Date Last Modified:    23-02-2023
#
#Purpose:
#
#The purpose of this program is to generate and then cube numbers 1-10

numbers = {}
#defining the variable as a dictionary

for x in range(1, 11):
    numbers[x] = x ** 3
#creating a for loop to generate the numbers 1-10 and then cubing the numbers it generates
    
print(numbers)
#printing the result