def count_negatives(grid):
    count = 0
    for row in grid:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid - 1
            else:
                left = mid + 1
        count += len(row) - left
    return count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(count_negatives(grid))
