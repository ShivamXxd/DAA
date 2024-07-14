class Solution(object):
    def sortEvenOdd(self, nums):
        odd_indices = nums[1::2]
        even_indices = nums[0::2]
        
        odd_indices.sort(reverse=True)
    
        even_indices.sort()
        
        result = []
        odd_iter = iter(odd_indices)
        even_iter = iter(even_indices)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(next(even_iter))
            else:
                result.append(next(odd_iter))
        
        return result

solution = Solution()
nums1 = [4, 1, 2, 3]
nums2 = [2, 1]
print(solution.sortEvenOdd(nums1))  
print(solution.sortEvenOdd(nums2))  
