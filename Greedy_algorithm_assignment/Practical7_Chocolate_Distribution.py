class Solution:
    def findMinDiff(self, A, N, M):
        if M > N:
            raise ValueError("Window size M cannot be greater than the number of elements N")
        
        A.sort()
        
        res = float('inf')
        
        for i in range(N - M + 1):
            min_ele = A[i]
            max_ele = A[i + M - 1]
            res = min(res, max_ele - min_ele)
        
        return res
