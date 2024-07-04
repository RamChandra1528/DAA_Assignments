# Compute the product of digits of a number using recursion

def ProductOfDigit(n):
    if n==0:
        return 1
    # if n<10:
    #     return n
    return n%10 * ProductOfDigit(n//10)
    

num = int(input("Enter the number :"))
print(ProductOfDigit(num))