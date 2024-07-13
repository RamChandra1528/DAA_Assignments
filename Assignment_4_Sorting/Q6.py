from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        soldier_count = [(sum(row), idx) for idx, row in enumerate(mat)]        
     
        soldier_count.sort(key=lambda x: (x[0], x[1]))
        
        weakest_rows = [idx for _, idx in soldier_count[:k]]
        
        return weakest_rows


sol = Solution()

mat1 = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k1 = 3

mat2 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
k2 = 2

print(sol.kWeakestRows(mat1, k1))  
print(sol.kWeakestRows(mat2, k2))  
