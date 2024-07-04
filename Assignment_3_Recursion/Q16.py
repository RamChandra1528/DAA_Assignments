class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False 
        if n == 1:
            return True   
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)

sol = Solution()
print(sol.isPowerOfFour(16))  
print(sol.isPowerOfFour(18)) 