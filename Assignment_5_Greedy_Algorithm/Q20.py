from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize candies array where each child gets 1 candy initially
        candies = [1] * n
        
        # First pass: from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Second pass: from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up all candies
        return sum(candies)


def main():
    solution = Solution()
    ratings = [1, 0, 2]
    print("Total candies needed:", solution.candy(ratings))

if __name__ == '__main__':
    main()
