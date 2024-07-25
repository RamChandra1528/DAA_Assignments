def FRACTIONAL_KNAPSACK(weight: list[int], value: list[int], c: int) -> float:
    N = len(value)
    items = [[weight[i], value[i]] for i in range(N)]

    # Sort the items based on value per unit of weight in descending order
    items.sort(reverse=True, key=lambda x: x[1] / x[0])

    total_value = 0.0
    current_w = 0

    for w, v in items:
        if current_w + w <= c:
            total_value += v
            current_w += w
        else:
            total_value += v * ((c - current_w) / w)
            break

    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
c = 50
FRACTIONAL_KNAPSACK(weights,values,c)