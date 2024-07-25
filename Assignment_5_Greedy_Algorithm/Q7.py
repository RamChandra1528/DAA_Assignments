def get_choco(chocolates:list[int],M:int)->int:
  N = len(chocolates)
  if N<M:
    return -1
  chocolates.sort()
  min_diff = float('inf')
  i = 0
  j = M- 1
  while j<N:
    min_diff = min(min_diff,chocolates[j]-chocolates[i])
    i+=1
    j+=1
  return min_diff

M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
get_choco(A,M)