class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        
        # Sort the jobs based on profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Initialize the parent array for disjoint-set
        parent = list(range(max_deadline + 1))
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        count_jobs = 0
        max_profit = 0
        
        # Iterate through all given jobs
        for job in Jobs:
            available_slot = find(min(max_deadline, job.deadline))
            if available_slot > 0:
                union(available_slot, available_slot - 1)
                count_jobs += 1
                max_profit += job.profit
        
        return count_jobs, max_profit