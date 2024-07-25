from typing import List

class Solution:
    def assignMiceHoles(self, N: int, mice: List[int], holes: List[int]) -> int:
        # Sort mice and holes
        mice.sort()
        holes.sort()
        
        # Find the maximum distance any mouse has to travel
        max_time = 0
        for i in range(N):
            max_time = max(max_time, abs(mice[i] - holes[i]))
        
        return max_time

def main():
    solution = Solution()
    N = 3  # Number of mice and holes
    mice = [4, -4, 2]  # Positions of mice
    holes = [4, 0, 5]  # Positions of holes
    
    print("Minimum maximum distance:", solution.assignMiceHoles(N, mice, holes))

    # Test case 2
    N = 2
    mice = [4, 2]
    holes = [1, 7]
    
    print("Minimum maximum distance:", solution.assignMiceHoles(N, mice, holes))

if __name__ == '__main__':
    main()
