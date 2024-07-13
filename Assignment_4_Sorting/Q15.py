from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(range(1, n + 1))
        actual = sum(set(nums))
        repeated = sum(nums) - actual
        return [repeated, total - actual]


sol = Solution()
nums = [1,2,2,4]
print(sol.findErrorNums(nums))  
