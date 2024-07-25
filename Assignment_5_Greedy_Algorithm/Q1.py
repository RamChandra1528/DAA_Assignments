def K_largest(nums:list[int],K:int)->int:
  nums.sort(reverse=True)

  sum = 0
  for i in range(K):
    sum += nums[i]
  return sum
  # return sum(nums.sort(reverse=True)[:k])


nums = [24,3,-1,2,32,1,32]
k = 3
t= K_largest(nums,k)
print(t)
