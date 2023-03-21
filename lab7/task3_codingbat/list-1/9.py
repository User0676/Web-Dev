def sum2(nums):
  cnt = 0
  x = 0
  for i in nums:
    cnt=cnt+i
    x=x+1
    if(x>1):return cnt
  return cnt
    