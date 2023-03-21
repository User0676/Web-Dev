def has23(nums):
  check2 = False
  check3 = False
  
  for i in nums:
    if i == 2:
      check2 = True
    if i==3:
      check3 = True
  return (check2 or check3)