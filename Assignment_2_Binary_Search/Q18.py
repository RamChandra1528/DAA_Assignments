def arrange_coins(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        current = mid * (mid + 1) // 2
        if current == n:
            return mid
        elif current < n:
            left = mid + 1
        else:
            right = mid - 1
    return right


n = 5
print(arrange_coins(n))
