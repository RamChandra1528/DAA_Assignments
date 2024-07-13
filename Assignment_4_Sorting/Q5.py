from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[i] for i in range(0, len(nums), 2)]
        odd = [nums[i] for i in range(1, len(nums), 2)]
        
        even.sort()
        odd.sort(reverse=True)
        
        result = []
        even_index, odd_index = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[even_index])
                even_index += 1
            else:
                result.append(odd[odd_index])
                odd_index += 1
                
        return result


sol = Solution()
nums = [4,1,2,3]
print(sol.sortEvenOdd(nums)) 