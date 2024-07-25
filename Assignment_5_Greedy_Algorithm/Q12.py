from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the end time of the first interval
        end = intervals[0][1]
        count = 0
        
        # Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous interval, it is overlapping
            if intervals[i][0] < end:
                count += 1
            else:
                # Update the end time to the end of the current interval
                end = intervals[i][1]
        
        return count


solution = Solution()
intervals1 = [[1,2],[2,3],[3,4],[1,3]]
print(solution.eraseOverlapIntervals(intervals1)) 

intervals2 = [[1,2],[1,2],[1,2]]
print(solution.eraseOverlapIntervals(intervals2)) 
intervals3 = [[1,2],[2,3]]
print(solution.eraseOverlapIntervals(intervals3))  
