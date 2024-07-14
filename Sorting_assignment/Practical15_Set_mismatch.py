class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        num_set = set()
        duplicated = -1
        
        for num in nums:
            if num in num_set:
                duplicated = num
            num_set.add(num)
        
        total_sum = n * (n + 1) // 2
        actual_sum = sum(num_set)
        missing = total_sum - actual_sum
        
        return [duplicated, missing]

solution = Solution()
nums1 = [1, 2, 2, 4]
nums2 = [1, 1]

print(solution.findErrorNums(nums1)) 
print(solution.findErrorNums(nums2))  
