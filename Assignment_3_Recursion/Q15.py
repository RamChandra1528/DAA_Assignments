class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False  # Zero is not a power of two
        if n == 1:
            return True   # 2^0 = 1, so 1 is a power of two
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)

sol = Solution()
print(sol.isPowerOfThree(16))  
print(sol.isPowerOfThree(18)) 