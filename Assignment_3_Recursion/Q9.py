# Find length of string recursion

def FindLength(str1):
    if str1 == "":
        return 0
    else:
        return 1 + FindLength(str1[1:]) 
    
print(FindLength("RamChandra"))
