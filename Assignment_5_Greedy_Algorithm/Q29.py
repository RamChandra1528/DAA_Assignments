def largestPermutation(k, arr):
    n = len(arr)
    # Map value to its index for quick lookup
    index_map = {value: i for i, value in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break
        
        # The value that should be at position i for the largest permutation
        largest_value = n - i
        
        if arr[i] == largest_value:
            continue
        
        # Find the index of the largest value
        largest_value_index = index_map[largest_value]
        
        # Swap the largest value with the current value
        arr[i], arr[largest_value_index] = arr[largest_value_index], arr[i]
        
        # Update the index map after the swap
        index_map[arr[largest_value_index]] = largest_value_index
        index_map[arr[i]] = i
        
        # Decrement the swap count
        k -= 1
    
    return arr

print(largestPermutation(1, [4, 2, 3, 5, 1]))  
print(largestPermutation(1, [2, 1, 3]))       
