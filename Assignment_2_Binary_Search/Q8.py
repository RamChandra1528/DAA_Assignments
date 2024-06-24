def find_first_last(nums, target):
    def binary_search_left():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left, right = binary_search_left(), binary_search_right()
    if left <= right:
        return [left, right]
    return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_last(nums, target))
