def guess_number(n, guess):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def guess(num):
    pick = 6
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1

n = 10
print(guess_number(n, guess))
