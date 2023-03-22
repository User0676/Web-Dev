def sum67(nums):
  check = False
  sum = 0

  for i in nums:
    if i==6:
      check=True
    
    if check==False:
      sum+=i
    
    if check==True and i==7:
      check=False
    

  return sum