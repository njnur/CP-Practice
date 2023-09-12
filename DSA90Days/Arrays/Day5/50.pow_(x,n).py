class Solution:
    """
    Leetcode problem solution of https://leetcode.com/problems/powx-n/
    """
    def fast_exponentiation(self, x: float, n: float) -> float:
        if n == 0:
            return 1.0
        if n % 2 == 0:
            half_portion = self.fast_exponentiation(x, n/2)
            return half_portion * half_portion
        else:
            half_portion = self.fast_exponentiation(x, (n-1)/2)
            return x * half_portion * half_portion

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        return self.fast_exponentiation(x, n)


print(Solution().myPow(x=2.00000, n=10))
print(Solution().myPow(x=2.10000, n=3))
print(Solution().myPow(x=2.00000, n=-2))
