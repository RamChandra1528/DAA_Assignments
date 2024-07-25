from typing import List

def catchThieves(arr: List[str], n: int, k: int) -> int:
    police = []
    thieves = []
    
    # Store indices of police and thieves
    for i in range(n):
        if arr[i] == 'P':
            police.append(i)
        elif arr[i] == 'T':
            thieves.append(i)
    
    i = 0  # Pointer for police
    j = 0  # Pointer for thieves
    caught = 0
    
    # Process the indices
    while i < len(police) and j < len(thieves):
        if abs(police[i] - thieves[j]) <= k:
            # If distance between police and thief is within k, catch the thief
            caught += 1
            i += 1
            j += 1
        elif police[i] < thieves[j]:
            # If current police is before the current thief, move to next police
            i += 1
        else:
            # If current thief is before the current police, move to next thief
            j += 1
    
    return caught

arr1 = ['P', 'T', 'T', 'P', 'T']
k1 = 1
print(catchThieves(arr1, len(arr1), k1))  

arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
k2 = 2
print(catchThieves(arr2, len(arr2), k2))  

arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
k3 = 3
print(catchThieves(arr3, len(arr3), k3))  
