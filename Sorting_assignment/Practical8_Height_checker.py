class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        
        diff_count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                diff_count += 1
        
        return diff_count

solution = Solution()
heights1 = [1, 1, 4, 2, 1, 3]
heights2 = [5, 1, 2, 3, 4]
heights3 = [1, 2, 3, 4, 5]

print(solution.heightChecker(heights1))  
print(solution.heightChecker(heights2))  
print(solution.heightChecker(heights3))  
