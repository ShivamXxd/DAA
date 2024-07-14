class Solution(object):
    def numberGame(self, nums):
        arr = []
        nums.sort()  
        
        while nums:
            alice_move = nums.pop(0)
            bob_move = nums.pop(0)
            arr.append(bob_move)
            arr.append(alice_move)
        
        return arr

solution = Solution()
nums1 = [5, 4, 2, 3]
print(solution.numberGame(nums1))  

nums2 = [2, 5]
print(solution.numberGame(nums2))