from typing import List

def findPlatform(arr: List[int], dep: List[int], n: int) -> int:
    # Sort arrival and departure times
    arr.sort()
    dep.sort()
    
    # Initialize variables
    platform_needed = 1
    max_platforms = 1
    i = 1
    j = 0
    
    # Traverse through sorted arrival and departure times
    while i < n and j < n:
        # If the next event is an arrival, increment platforms needed
        if arr[i] <= dep[j]:
            platform_needed += 1
            i += 1
        # If the next event is a departure, decrement platforms needed
        else:
            platform_needed -= 1
            j += 1
        
        # Update max_platforms if needed
        max_platforms = max(max_platforms, platform_needed)
    
    return max_platforms

def main():
    arr = [100, 300, 500]
    dep = [900, 400, 600]

    n = len(arr)

    print("Minimum number of platforms required:", findPlatform(arr, dep, n))

if __name__ == '__main__':
    main()
