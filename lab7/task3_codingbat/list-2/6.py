def has22(nums):
  isTwo = False
  
  for i in nums:
    if i == 2 and isTwo==False:
      isTwo = True
    elif i==2 and isTwo==True:
      return True
    
    if i!=2:
      isTwo = False
  return False
