class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] = -nums[index]
        
        return result

solution = Solution()
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
nums2 = [1, 1, 2]
nums3 = [1]

print(solution.findDuplicates(nums1))  
print(solution.findDuplicates(nums2))  
print(solution.findDuplicates(nums3))  
