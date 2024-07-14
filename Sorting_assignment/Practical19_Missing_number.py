class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

solution = Solution()
nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(solution.missingNumber(nums1))  
print(solution.missingNumber(nums2))  
print(solution.missingNumber(nums3))  
