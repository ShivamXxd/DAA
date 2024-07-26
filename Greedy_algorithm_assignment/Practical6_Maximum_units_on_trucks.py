from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        p = 0
        for i, j in boxTypes:
            if i < truckSize:
                p += i * j
                truckSize -= i
            else:
                p += truckSize * j
                break
        return p

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
sol = Solution()
print(sol.maximumUnits(boxTypes=boxTypes, truckSize=truckSize))