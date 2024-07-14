class Solution(object):
    def findRelativeRanks(self, score):
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}
        
        for i in range(len(sorted_scores)):
            if i == 0:
                rank_map[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_scores[i]] = "Bronze Medal"
            else:
                rank_map[sorted_scores[i]] = str(i + 1)
        
        result = []
        for s in score:
            result.append(rank_map[s])
        
        return result

solution = Solution()
score1 = [5, 4, 3, 2, 1]
score2 = [10, 3, 8, 9, 4]

print(solution.findRelativeRanks(score1))  
print(solution.findRelativeRanks(score2))  
