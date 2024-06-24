def find_in_mountain_array(arr, target):
    def peak_index_in_mountain_array():
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(left, right, target, ascending=True):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                if ascending:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if ascending:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    peak = peak_index_in_mountain_array()
    index = binary_search(0, peak, target)
    if index != -1:
        return index
    return binary_search(peak + 1, len(arr) - 1, target, ascending=False)


arr = [1, 2, 3, 4, 5, 3, 1]
target = 3
print(find_in_mountain_array(arr, target))
