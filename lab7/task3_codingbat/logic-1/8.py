def in1to10(n, outside_mode):
  if outside_mode==False:
    if n>=1 and n<=10:
      return True
    else: return False
  else:
    if n>1 and n<10:
      return False
    else: return True
    