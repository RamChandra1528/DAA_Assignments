def find_floor_ceil(arr, target):
    left, right = 0, len(arr) - 1
    floor, ceil = -1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid], arr[mid]
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        else:
            ceil = arr[mid]
            right = mid - 1
    return floor, ceil


arr = [1, 2, 4, 6, 10]
target = 5
print(find_floor_ceil(arr, target))
