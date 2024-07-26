from typing import List
import math

class Solution:
    def candyStore(self, arr: List[int], N: int, K: int) -> List[int]:
        arr.sort()
        
        buy_count = math.ceil(N / (K + 1))
        
        min_amt = 0
        max_amt = 0
        
        for i in range(buy_count):
            min_amt += arr[i]
    
        for i in range(1, buy_count + 1):
            max_amt += arr[-i]
        
        return [min_amt, max_amt]
