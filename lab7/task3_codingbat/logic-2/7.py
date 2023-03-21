def make_chocolate(small, big, goal):
  need_big = goal//5
  if need_big>big:
    need_big=big
  need_small = goal - (need_big*5)
  if need_small>small:
    return -1
  else: return need_small
  