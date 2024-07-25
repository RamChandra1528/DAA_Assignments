class Solution:
    def minimumPlatform(self, n, arr, dep):
        # Sort arrival and departure times
        arr.sort()
        dep.sort()

        # Initialize pointers for arrival and departure
        i = 1  # pointer for arrival times
        j = 0  # pointer for departure times
        
        # Initialize the maximum platforms needed and current platforms needed
        max_platforms = 1
        current_platforms = 1
        
        while i < n and j < n:
            # If next event is an arrival, increment platforms needed
            if arr[i] <= dep[j]:
                current_platforms += 1
                i += 1
            # If next event is a departure, decrement platforms needed
            else:
                current_platforms -= 1
                j += 1

            # Update the maximum platforms needed
            if current_platforms > max_platforms:
                max_platforms = current_platforms

        return max_platforms


solution = Solution()
arr = [10, 15, 20, 25, 30]
dep = [12, 18, 25, 30, 35]
print(solution.minimumPlatform(len(arr), arr, dep))  