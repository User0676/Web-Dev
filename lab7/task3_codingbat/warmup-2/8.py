def array123(nums):
  check1 = False
  check2 = False
  check3 = False
  
  for i in nums:
    if i == 1:
      check1 = True
    if i ==2:
      check2 = True
    if i == 3:
      check3 = True
  if check1 == check2 ==check3 == True:
    return True
  return False
      