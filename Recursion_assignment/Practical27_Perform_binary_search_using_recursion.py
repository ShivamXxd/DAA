class Solution(object):
    def search(self,nums,target):
        start=0
        end=len(nums)-1
        mid=start+(end-start)//2

        while start <=end:
            if target ==nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    start=mid+1
                    mid=start+(end-start)//2
                elif target < nums[mid]:
                    end=mid-1
                    mid=start+(end-start)//2
                else:
                    return mid
        return -1
    