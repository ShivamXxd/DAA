from typing import List, Tuple

class Job:
    def __init__(self, id: int, deadline: int, profit: int):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    
    def JobScheduling(self, Jobs: List[Job], n: int) -> Tuple[int, int]:
        
        max_deadline = max(job.deadline for job in Jobs)
        
        
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
    
        slots = [-1] * (max_deadline + 1)
        
        total_jobs = 0
        total_profit = 0
        
    
        for job in Jobs:
            
            for slot in range(job.deadline, 0, -1):
                if slots[slot] == -1:
                    slots[slot] = job.id  
                    total_profit += job.profit
                    total_jobs += 1
                    break
        
        return total_jobs, total_profit
