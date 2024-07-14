class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  
        n = len(nums)
        
        for i in range(n):
            if nums[i] >= i + 1 and (i == n - 1 or nums[i + 1] < i + 1):
                return i + 1
            
        return -1

solution = Solution()
nums1 = [3, 5]
nums2 = [0, 0]
nums3 = [0, 4, 3, 0, 4]

print(solution.specialArray(nums1))  
print(solution.specialArray(nums2))  
print(solution.specialArray(nums3))  
