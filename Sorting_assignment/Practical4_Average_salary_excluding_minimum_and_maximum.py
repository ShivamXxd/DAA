class Solution(object):
    def average(self, salary):
        s=0.0
        salary.sort()
        salary.pop(0)
        salary.pop()
        for i in salary:
            s=s+i
        var=s/len(salary)
        return var