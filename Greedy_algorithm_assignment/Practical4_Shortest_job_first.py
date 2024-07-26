class Solution:
    @staticmethod
    def solve(bt):
        bt.sort()
        waiting_time = 0
        time = 0
        
        for i in range(len(bt)):
            time += bt[i]
            waiting_time += (time - bt[i])
        
        return waiting_time // len(bt)  
