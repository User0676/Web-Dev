def rotate_left3(nums):
  m = nums[0]
  for i in range(0,len(nums)-1):
    nums[i] = nums[i+1]
  nums[len(nums)-1] = m
    
  return nums