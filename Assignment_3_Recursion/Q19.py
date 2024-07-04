def special_fibonacci_optimized(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    
    remainder = n % 3
    
    if remainder == 0:
        return a
    elif remainder == 1:
        return b
    else:
        return a ^ b


# data = input().strip().split('\n')

# T = int(data[0].strip())

# results = []
# for i in range(1, T + 1):
#     a, b, n = map(int, data[i].strip().split())
#     results.append(special_fibonacci_optimized(a, b, n))


# for result in results:
#     print(result)
