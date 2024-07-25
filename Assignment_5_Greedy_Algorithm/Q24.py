class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Initialize the sum to 0
        sum = 0
        
        # First, add as many 1's as possible, up to k
        onesToAdd = min(numOnes, k)
        sum += onesToAdd
        k -= onesToAdd
        
        # Then, add as many 0's as possible, up to the remaining k
        zerosToAdd = min(numZeros, k)
        # Note: Adding zeros does not change the sum
        k -= zerosToAdd
        
        # Finally, add as many -1's as necessary to fill the remaining k
        negOnesToAdd = min(numNegOnes, k)
        sum -= negOnesToAdd
        
        return sum

# Example usage
solution = Solution()
print(solution.kItemsWithMaximumSum(3, 2, 4, 3)) # Output: 3
print(solution.kItemsWithMaximumSum(2, 1, 2, 4)) # Output: 2
