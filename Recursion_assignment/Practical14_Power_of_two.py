class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

sol = Solution()
print(sol.isPowerOfTwo(1))  
print(sol.isPowerOfTwo(16))  
print(sol.isPowerOfTwo(3))  
