# Compute the sum of digits of a number using recursion
def SumOfDigit(n):
    if n==0:
        return 0
    return n%10 + SumOfDigit(n//10)
    

num = int(input("Enter the number :"))
print(SumOfDigit(num))