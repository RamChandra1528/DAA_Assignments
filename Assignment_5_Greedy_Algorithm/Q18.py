from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Edge case: if the length of nums is 1 or less, no jumps are needed.
        if len(nums) <= 1:
            return 0
        
        # Initialize the variables.
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Iterate through the array.
        for i in range(len(nums) - 1):  # We do not need to consider the last index.
            # Update the farthest we can reach.
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can reach the end of the array, break out of the loop.
                if current_end >= len(nums) - 1:
                    break
        
        return jumps

solution = Solution()
nums = [2, 3, 1, 1, 4]
print(solution.jump(nums))  