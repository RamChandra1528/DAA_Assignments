from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)


sol = Solution()
nums = [-4,-1,0,3,10]
print(sol.sortedSquares(nums)) 