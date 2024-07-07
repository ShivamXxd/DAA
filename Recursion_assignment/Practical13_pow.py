class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:  
                result *= current_product
            current_product *= current_product 
            n //= 2 

        return result

sol = Solution()
print(sol.myPow(2.00000, 10))  
print(sol.myPow(2.10000, 3))   
print(sol.myPow(2.00000, -2))  
