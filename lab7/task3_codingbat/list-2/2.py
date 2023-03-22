def big_diff(nums):
  min_val = 9999999
  max_val = -9999999
  
  for i in nums:
    if i<min_val:
      min_val = i
    if i>max_val:
      max_val = i
  return max_val-min_val
      