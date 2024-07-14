class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldiers_count = [(sum(row), index) for index, row in enumerate(mat)]
        
        soldiers_count.sort(key=lambda x: (x[0], x[1]))
        
        return [index for _, index in soldiers_count[:k]]

solution = Solution()
mat1 = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k1 = 3
print(solution.kWeakestRows(mat1, k1))  

mat2 = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]
k2 = 2
print(solution.kWeakestRows(mat2, k2))  
