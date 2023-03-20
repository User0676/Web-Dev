def array_front9(nums):
  cnt = 0
  for i in nums:
    if i == 9:
      return True
    cnt+=1
    if cnt>=4 or cnt == len(nums):
      return False
  return False
