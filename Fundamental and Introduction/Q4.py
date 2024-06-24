# Write a program to find factors of a given number


n = int(input("Enter a num to get the factors of taht num"))
factorList = [1]

for i in range(2,n):
    if n%i == 0:
        factorList.append(i)

print(f"The factors of {n} are {factorList}")