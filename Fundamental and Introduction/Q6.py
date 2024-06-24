# Write a program to generate the Fibonacci sequence up to a given number of terms


n = int(input("Enter a num to get the fibonacci sequence"))

a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    c = a+b
    print(c)
    a = b
    b = c
