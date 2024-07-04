# Geek created a random series and given a name geek-onacci series. 
# Given four integers A, B, C, N. A, B, C represents the first three numbers of geek-onacci series. 
# Find the Nth number of the series. The nth number of geek-onacci series is a sum of the last three numbers 
# (summation of N-1th, N-2th, and N-3th geek-onacci numbers)

def Geeknachhi(A,B,C,N):
    if N==1:
        return A
    if N==2:
        return B
    if N==3:
        return C
    return Geeknachhi(A,B,C,N-1)+Geeknachhi(A,B,C,N-2)+Geeknachhi(A,B,C,N-3)


T = int(input().strip())  
results = []
for _ in range(T):
    A, B, C, N = map(int, input().strip().split())
    nth_geekonacci = Geeknachhi(A, B, C, N)
    results.append(nth_geekonacci)
    
print("<------------->\n")
for result in results:
    print(result)