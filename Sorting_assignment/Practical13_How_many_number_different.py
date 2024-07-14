class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        
        result = [rank[num] for num in nums]
        
        return result
    
solution = Solution()
nums1 = [8, 1, 2, 2, 3]
nums2 = [6, 5, 4, 8]
nums3 = [7, 7, 7, 7]

print(solution.smallerNumbersThanCurrent(nums1))  
print(solution.smallerNumbersThanCurrent(nums2)) 
print(solution.smallerNumbersThanCurrent(nums3))  
