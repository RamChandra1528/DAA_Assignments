from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current_gas drops below 0, reset start_index and current_gas
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        # If total gas is less than total cost, it's not possible to complete the circuit
        if total_gas < total_cost:
            return -1
        
        return start_index

solution = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(gas, cost))  
