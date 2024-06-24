# Write a program to calculate the factorial of a given number

n = int(input("Enter a num to get the factorial of taht num"))
def fact(n):
    if n==0 or n==1:
        return 1
    return n* fact(n-1)

print(f"The factorial of {n} is {fact(n)}")

