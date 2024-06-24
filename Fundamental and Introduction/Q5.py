# Write a program to check if an input number is prime or not

n = int(input("Enter a num to check if it is prime or not"))

flag = True
for i in range(2,n//2):
    if n % i == 0:
        flag = False

if flag:
    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")
