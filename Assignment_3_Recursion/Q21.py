# vNumber of Steps to Reduce a Number to Zero using recursion
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)
        else:
            return 1 + self.numberOfSteps(num - 1)


s = Solution()

print(s.numberOfSteps(123))