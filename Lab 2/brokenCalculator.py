# Author : Jaden Miguel
# Description : Lab 2, CSCI 141
# Date : April 16, 2019
# get the first and second integers
firstInput = int(input("Please enter the first integer "))
secondInput = int(input("Please enter a second integer "))
# A. print out "Fixing notation!"
print("Fixing notation!")
# B. Extract the integer and decimal portions from the first integer input
int1 = firstInput // 10
dec1 = firstInput % 10
# C. Print the reformatted first input
print(int1, dec1, sep=".")
# D. Extract the integer and decimal portions from the second integer
input
int2 = secondInput // 10
dec2 = secondInput % 10
# E. Print the reformatted second input
print(int2, dec2, sep=".")
# F. Perform calculations for the product of the reformatted (decimal) values
firstCalc = (int1 * int2)
secondCalc = (int1 * dec2 * 0.1)
thirdCalc = (dec1 * 0.1 * int2)
fourthCalc = (dec1 * 0.1 * dec2 * 0.1)
finalCalc = (firstCalc + secondCalc + thirdCalc + fourthCalc)
# G. Print out the final result
print("The product is:", finalCalc)