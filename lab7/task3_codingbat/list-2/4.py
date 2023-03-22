def sum13(nums):
  if len(nums)==0:
    return 0
  
  sum = 0
  check= False
  
  for i in nums:
    if i==13:
      check=True
    if check==False:
      sum+=i
    if check==True and i!=13:
      check=False
  return sum
    