''' #1 Write a program to check is a given number is
    even or odd
    positive, negative or zero'''
    
n = int(input("enter an integer:"))
if n<0:
    print(n,"is negative integer")
else:
    print(n,"is positive integer")
    
if n%2 == 0:
    print(n," is even integer")
else:
    print(n," is even integer")
    
