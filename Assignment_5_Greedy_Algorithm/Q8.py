from typing import List, Tuple

def candy_store(candies: List[int], k: int) -> Tuple[int, int]:
    N = len(candies)
    candies.sort()

    min_p = 0
    buy = 0
    free = N - 1
    while buy <= free:
        min_p += candies[buy]
        buy += 1
        free -= k

    max_p = 0
    buy = N - 1
    free = 0
    while buy >= free:
        max_p += candies[buy]
        buy -= 1
        free += k

    return min_p, max_p

# Test cases
candies = [3, 2, 1, 4]
k = 2
print(candy_store(candies, k))
