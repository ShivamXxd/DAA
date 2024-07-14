class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
    
solution = Solution()
nums1 = [1, 3, 4, 2, 2]
nums2 = [3, 1, 3, 4, 2]
nums3 = [3, 3, 3, 3, 3]

print(solution.findDuplicate(nums1))  
print(solution.findDuplicate(nums2))  
print(solution.findDuplicate(nums3))  
