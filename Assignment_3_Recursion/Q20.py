# Count Number of Zeros in a Number using recursion

def CountZero(num):
    if num == 0:
        return 1
    
    if num < 10:
        return 0
    
    last = num % 10
    restdigit = num//10
    
    return (1 if last == 0 else 0) + CountZero(restdigit)
    
print(CountZero(90))