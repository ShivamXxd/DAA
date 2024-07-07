class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b


sol = Solution()
print(sol.fib(2))  
print(sol.fib(3))  
print(sol.fib(4))  
