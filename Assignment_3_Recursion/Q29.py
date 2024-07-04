def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    
    sorted_arr = insertion_sort(arr[1:])
    key = arr[0]
    i = len(sorted_arr) - 1
    sorted_arr.append(key)
    
    while i >= 0 and sorted_arr[i] > key:
        sorted_arr[i+1] = sorted_arr[i]
        i -= 1
    
    sorted_arr[i+1] = key
    
    return sorted_arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
