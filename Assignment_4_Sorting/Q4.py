from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
       
        min_salary = min(salary)
        max_salary = max(salary)
        
        total_sum = sum(salary) - min_salary - max_salary
     
        avg = total_sum / (len(salary) - 2)
        
        return avg

s = Solution()
print(s.average([1, 3, 5, 7, 2, 8]))  
