# For any positive value of N, print 1 to N without using for or while loops via recursion (Reverse Countdown)

def PrintValue(N):
    if N == 0:
        return
    print(N)
    PrintValue(N - 1)

PrintValue(10)
    