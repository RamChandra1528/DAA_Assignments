# For any positive value of N, print N to 1 without using for or while loops via recursion (Countdown)

def PrintValue(N):
    if N == 0:
        return
    PrintValue(N - 1)
    print(N)

PrintValue(10)