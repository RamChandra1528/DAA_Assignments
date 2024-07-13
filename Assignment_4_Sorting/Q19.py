from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


sol = Solution()
nums = [3,0,1]
print(sol.missingNumber(nums)) 
