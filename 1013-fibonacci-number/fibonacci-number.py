class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        def fib(n):
            if n == 0 or n == 1:
                return n
            
            if n in dp:
                return dp[n]

            dp[n] = fib(n - 1) + fib(n - 2)
            return fib(n - 1) + fib(n - 2)
        return fib(n)