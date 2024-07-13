from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]


sol = Solution()
nums = [1,2,5,2,3]
target = 2
print(sol.targetIndices(nums, target))  
