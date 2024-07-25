def minJumpsToGroup(S):
    MOD = 10**9 + 7
    
    # Extract the positions of all 'x'
    positions = [i for i, char in enumerate(S) if char == 'x']
    
    if not positions:
        return 0  # No 'x' in the string
    
    # Find the median position
    n = len(positions)
    median_index = n // 2
    median = positions[median_index]
    
    # Calculate the total number of jumps
    total_jumps = 0
    for i, pos in enumerate(positions):
        # Calculate the target position of 'x' relative to the median
        target_position = median - (median_index - i)
        total_jumps += abs(pos - target_position)
        total_jumps %= MOD
    
    return total_jumps

# Example usage
S1 = ". . . . x . . x x . . . x . ."
S2 = "x x x . . . . . . . . x x x x x x"
print(minJumpsToGroup(S1))  
print(minJumpsToGroup(S2))  
