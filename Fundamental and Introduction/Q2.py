#Write a program to calculate the sum of the first N natural numbers

n = int(input("Enter an integer to get the sum of first natural numbers to it..."))
sum = 0

for i in range(0,n+1):
    sum+= i
print(sum)