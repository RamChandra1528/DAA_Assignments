class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        if n == 0:
            return 0
        
        # Sort the array initially
        arr.sort()
        
        total_cost = 0
        
        # Continue until only one rope is left
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = arr.pop(0)
            second = arr.pop(0)
            
            # The cost to connect these two ropes
            cost = first + second
            total_cost += cost
            
            # Insert the resulting rope back into the sorted list
            # This maintains the sorted order
            self.insert_sorted(arr, cost)
        
        return total_cost
    
    def insert_sorted(self, arr, value):
        # Insert 'value' into the sorted list 'arr' while maintaining the sorted order
        if not arr or value >= arr[-1]:
            arr.append(value)
        else:
            for i in range(len(arr)):
                if arr[i] > value:
                    arr.insert(i, value)
                    break

solution = Solution()
arr = [4, 3, 2, 6]
n = len(arr)
print(solution.minCost(arr, n)) 
