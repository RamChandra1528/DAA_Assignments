# Check is a String is Palindrome using recursion

def Palindrome(st):

    if st == '':
        return True
    if st[0] == st[-1]:
        return Palindrome(st[1:-1])
    else:
        return False
    
t= Palindrome("abbab")
print(t)