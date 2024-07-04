# Find the value of 'a' raised to the power 'b' using recursion

def A_power_of_B(a,b):
    if b==0:
        return 1
    return a*A_power_of_B(a,b-1)

print(A_power_of_B(5,3))