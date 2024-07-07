class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0 and (n - 1) % 3 == 0

sol = Solution()
print(sol.isPowerOfFour(16))  
print(sol.isPowerOfFour(5))   
print(sol.isPowerOfFour(1))   
