def defround10(n):
  if n%10>=5:
    n=n+(10-n%10)
  else:
    n=n-(n%10)
  return n


def round_sum(a, b, c):
  return defround10(a)+defround10(b)+defround10(c)
  