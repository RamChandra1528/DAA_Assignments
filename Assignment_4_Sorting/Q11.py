from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) + 1):
            if len([x for x in nums if x >= i]) == i:
                return i
        return -1


sol = Solution()
nums = [3,5]
print(sol.specialArray(nums))  
