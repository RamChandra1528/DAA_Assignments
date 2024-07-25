from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the list of merged intervals with the first interval
        merged_intervals = [intervals[0]]
        
        for current in intervals[1:]:
            # Get the last interval in the merged_intervals list
            last_merged = merged_intervals[-1]
            
            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Otherwise, add the current interval to the merged_intervals list
                merged_intervals.append(current)
        
        return merged_intervals
    