# Find mean of Array elements using recursion

def SumArray(num):
    if len(num)==0:
        return 0
    return num[0] + SumArray(num[1:])


def Mean_find(num):
    if len(num)==0:
        return 0
    total_sum = SumArray(num)
    return total_sum / len(num)


ls = [1,2,3,4,5,5]

print(Mean_find(ls))