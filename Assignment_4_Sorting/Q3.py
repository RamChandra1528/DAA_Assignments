def playGame(nums: List[int]) -> List[int]:
    nums.sort()  
    arr = []
    
    while nums:
        alice_move = nums.pop(0) 
        if nums:
            bob_move = nums.pop(0) 
            arr.append(bob_move)  
        arr.append(alice_move)  
    
    return arr


nums = [5, 4, 2, 3]
output = playGame(nums)
print(output)  
