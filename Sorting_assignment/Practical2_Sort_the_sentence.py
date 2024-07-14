class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        
        words.sort(key=lambda x: int(x[-1]))
        
        sorted_sentence = ' '.join(word[:-1] for word in words)
        
        return sorted_sentence

solution = Solution()
s1 = "is2 sentence4 This1 a3"
print(solution.sortSentence(s1))  

s2 = "Myself2 Me1 I4 and3"
print(solution.sortSentence(s2))  
