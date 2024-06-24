def target_indices_after_sorting(nums, target):
    nums.sort()
    indices = []
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    return indices


nums = [1, 2, 5, 2, 3]
target = 2
print(target_indices_after_sorting(nums, target))
