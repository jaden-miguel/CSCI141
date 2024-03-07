# Name: Jaden Miguel
# Date: 30 April 2019
# Purpose: First part of Lab 4, triangle.py

star_val = ("*")

width = int(input("How wide would you like your triangle? Enter an integer value: "))
print()


for i in range (0, width):
    
    for j in range(0, i+1):
        print(star_val, end="")
    print()
    
    

for i in range(width, 0, -1):
    for j in range(0, i-1):
        print(star_val, end="")
    print()