# Write a program to check if an input number is an Armstrong number
n = input("Enter a num to check if it is an armstrong number")
sum =0

for i in n:
    sum+= int(i)*int(i)*int(i)
    
if sum == int(n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
