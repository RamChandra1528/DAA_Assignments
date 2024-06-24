def split_array(nums, m):
    def valid(mid):
        current_sum, splits = 0, 1
        for num in nums:
            current_sum += num
            if current_sum > mid:
                current_sum = num
                splits += 1
                if splits > m:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(mid):
            right = mid
        else:
            left = mid + 1
    return left


nums = [7, 2, 5, 10, 8]
m = 2
print(split_array(nums, m))
