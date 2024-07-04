def max_and_min_value_in_array(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    mid = len(arr) // 2
    left_min, left_max = max_and_min_value_in_array(arr[:mid])
    right_min, right_max = max_and_min_value_in_array(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

ls = [1, 3, 4, 2, 4, 52, 1, 4]
print(max_and_min_value_in_array(ls))  