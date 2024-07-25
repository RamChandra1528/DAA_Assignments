from typing import List
def findContentChildren(g: List[int], s: List[int]) -> int:
  #compute size
  N = len(g)
  M = len(s)
  # Sort the Arrays
  g.sort()
  s.sort()
  # Assign pointers to the start of each array
  i,j =0,0
  count = 0
  while i< N and j<M:
    if g[i]<=s[j]:
      count+=1
      i+=1
      j+=1
    else:
      j+=1
  return count

g = [1,2,3]
s = [1,1]
findContentChildren(g,s)