def centered_average(nums):
  min_val = 9999999
  max_val = -9999999
  for i in nums:
    if i<min_val:
      min_val = i
    if i>max_val:
      max_val = i
    
  sum = 0
  size = -2
    
  for i in nums:
    if i==min_val:
      i=0
      min_val = 999999999
    elif i==max_val:
      i=0
      max_val=999999999
    else:sum+=i
    size+=1
  
  return sum/size