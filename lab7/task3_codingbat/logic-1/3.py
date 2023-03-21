def squirrel_play(temp, is_summer):
  if temp>=60:
    if is_summer:
      if temp<=100: return True
    else:
      if temp<=90: return True
  return False