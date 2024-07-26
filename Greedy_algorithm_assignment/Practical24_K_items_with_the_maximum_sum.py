class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        rem = k - numOnes - numZeros
        if rem <= 0:
            return numOnes
        return numOnes - rem

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
sol = Solution()
print(sol.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))