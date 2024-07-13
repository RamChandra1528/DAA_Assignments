from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(x < num for x in nums) for num in nums]


sol = Solution()
nums = [8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))  
