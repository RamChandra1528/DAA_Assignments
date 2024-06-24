# Write a program to find the sum of digits of an input number

n = input("Enter a num to get the sum of its digits")
sum =0

for i in n:
    sum+= int(i)
    
print(sum)
