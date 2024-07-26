import math
class Solution:
    @staticmethod
    def minimumDays(S, N, M):
        diff = N - M
        if diff < 0 or (S > 6 and diff * 6 < M):
            return -1
        else:
            return math.ceil((S * M) / N)
