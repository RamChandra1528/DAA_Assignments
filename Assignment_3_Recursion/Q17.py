
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence.

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

sol = Solution()
print(sol.fib(10))  
