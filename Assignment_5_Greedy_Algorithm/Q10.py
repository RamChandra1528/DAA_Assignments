def scheduled_job(jobs: list[list[int]]) -> tuple[int, int]:
    N = len(jobs)
    if N == 0:
        return 0, 0
    if N == 1:
        return 1, jobs[0][2]
    
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline
    max_deadline = max(job[1] for job in jobs)
    
    # Create a schedule array for max_deadline number of days
    slots = [None] * max_deadline
    
    count = 0
    total_profit = 0
    
    for job in jobs:
        job_id, deadline, profit = job
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(deadline - 1, -1, -1):
            if slots[j] is None:
                slots[j] = job_id
                count += 1
                total_profit += profit
                break
    
    return count, total_profit

# Example usage:
jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 3, 15]]
print(scheduled_job(jobs))
