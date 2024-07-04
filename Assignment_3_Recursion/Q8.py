# Reverse a number using recursion
import math

def Reverse_Number(n,res=0):
    if n==0:
        return res
    res = res*10 + n%10
    return Reverse_Number(n//10,res)

print(Reverse_Number(123453))