import math
def SurvivelDays(S:int,N:int,M:int)->int:
  sundays = S//7
  buy_days = S - sundays
  total_food  = S*M
  total_days = math.ceil(total_food/(N+M))

  if total_days <= buy_days:
    return total_days
  else:
    return -1
  
print(SurvivelDays(10,16,2))