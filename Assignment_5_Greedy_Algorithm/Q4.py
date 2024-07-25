def solve(bt):
    # Step 1: Sort the burst times
    bt.sort()
    
    n = len(bt)
    
    # Step 2: Calculate waiting times
    waiting_time = 0
    total_waiting_time = 0
    
    for i in range(n):
        # waiting_time is the total of previous burst times
        total_waiting_time += waiting_time
        # Add the current process's burst time to waiting_time
        waiting_time += bt[i]
    
    # Step 3: Calculate the average waiting time
    average_waiting_time = total_waiting_time // n
    
    return average_waiting_time

print(solve([4, 3, 7, 1, 2]))  
print(solve([1, 2, 3, 4]))    
