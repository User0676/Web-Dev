def pos_neg(a, b, negative):
  if negative == True:
    if a<0 and b<0:
      return True
  else:
    if a<0 and b>0:
      return True
    elif b<0 and a>0:
      return  True
  return False
