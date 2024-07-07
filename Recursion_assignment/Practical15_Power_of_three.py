class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

sol = Solution()
print(sol.isPowerOfThree(27))  
print(sol.isPowerOfThree(0))   
print(sol.isPowerOfThree(-1))  
