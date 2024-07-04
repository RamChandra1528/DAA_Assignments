def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    

    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort_recursive(arr, n - 1)
    return arr


arr = [34, 12, 11, 22, 25, 64, 90]
sorted_arr = bubble_sort_recursive(arr)
print("Sorted array:", sorted_arr)
