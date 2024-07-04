# Compute sum of first N natural numbers using recursion

def SumOfNaturalNumber(n):
    if n==0:
        return 0
    return n + SumOfNaturalNumber(n-1)


print(SumOfNaturalNumber(5))
