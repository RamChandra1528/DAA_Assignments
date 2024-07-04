# Reverse a string uing recursion

def Reverse_String(st):
    if st == '':
        return ''
    return st[-1] + Reverse_String(st[:-1])

print(Reverse_String("ram_siyA"))