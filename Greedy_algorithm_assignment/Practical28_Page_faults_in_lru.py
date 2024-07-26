class Solution:
    def pageFaults(self, N, C, pages):

        a=[]
        s=0
        for i in range(len(pages)):
            if pages[i] not in a:
                if len(a)==C:
                    a.pop(0)
                a.append(pages[i])
                s+=1
            else:
                a.remove(pages[i])
                a.append(pages[i])
        return s

N = 9
C = 4
pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
sol = Solution()
print(sol.pageFaults(N, C, pages))