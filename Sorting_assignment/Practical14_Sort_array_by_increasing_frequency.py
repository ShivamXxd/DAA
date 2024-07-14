class Solution(object):
    def frequencySort(self, nums):
        from collections import Counter
        
        freq = Counter(nums)
        
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums

solution = Solution()
nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [2, 3, 1, 3, 2]
nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(solution.frequencySort(nums1))  
print(solution.frequencySort(nums2))  
print(solution.frequencySort(nums3))  
