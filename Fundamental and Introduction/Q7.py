# Write a program to check if an input string is a palindrome

a = input("Enter a string:")

b = a[::-1]

if b == a:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")
    