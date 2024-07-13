from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


sol = Solution()
nums = [1,1,2,2,2,3]
print(sol.frequencySort(nums)) 
