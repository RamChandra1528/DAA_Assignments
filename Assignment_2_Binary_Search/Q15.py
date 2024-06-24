def count_rotations(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % len(arr)
        prev = (mid - 1 + len(arr)) % len(arr)
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [15, 18, 2, 3, 6, 12]
print(count_rotations(arr))
