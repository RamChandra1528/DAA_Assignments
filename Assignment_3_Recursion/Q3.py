# Given two numbers x and y find the product using recursion

def ProductOfwoNum(x,y):
    if x==0:
        return 0
    return y+ProductOfwoNum(x-1,y)

print(ProductOfwoNum(2,5))