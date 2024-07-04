# Find sum of Array elements using recursion

def SumArray(num):
    if len(num)==0:
        return 0
    return num[0] + SumArray(num[1:])


ls = [1,2,3,4,5,5]

print(SumArray(ls))