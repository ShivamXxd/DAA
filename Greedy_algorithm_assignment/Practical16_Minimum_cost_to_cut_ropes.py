import heapq
from typing import List

class Solution:
    def minCost(self, arr: List[int], n: int) -> int:
        heapq.heapify(arr)
        
        total_cost = 0
        
        while len(arr) > 1:
            p1 = heapq.heappop(arr)
            p2 = heapq.heappop(arr)
            
            combined_cost = p1 + p2
            total_cost += combined_cost
            
            heapq.heappush(arr, combined_cost)
        
        return total_cost
