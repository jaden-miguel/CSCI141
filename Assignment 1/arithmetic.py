# Author: Jaden Miguel
# Date: 4/12/19
# Prog. Description: Assignment 1
name = input("What is your name? ")
print("Hello", name, end="! ")
firstnum = input("Enter your first number: ")
secondnum = input("Excellent choice. How about the second one? ")
# used for integer conversion
firstnum = int(firstnum)
secondnum = int(secondnum)
# sum and product equations
sumOfNumbers = firstnum + secondnum
prodOfNumbers = firstnum * secondnum
print("Their sum is:", sumOfNumbers)
print("Their product is:", prodOfNumbers)
# remainder and division result equations
remainder = firstnum % secondnum
divresult = firstnum // secondnum
# rephrases division question, prints quotient & remainder
print(
    firstnum, "divided by", secondnum, "is", divresult, "remainder", remainder, sep=" "
)
