# Name: Jaden Miguel
# Date: 30 April 2019
# Purpose: Second part of Lab 4, flag.py, drawing an ASCII american flag

space = " "


#set range for flag, which is 13 lines
for i in range (1, 14):
    
    if i <= 9 and i % 2 != 0:
        print("*" " " * 6, "=" * 42)
    
    elif i <= 9 and i % 2 == 0:
        print(" " "*" * 5, space, "=" * 42)
    
    elif i > 9:
        print("=" * 55)
    