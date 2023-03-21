def lone_sum(a, b, c):
  if a==b:
    if a==c:
      a=b=c=0
    else:
      a=b=0
  if b==c:
    b=c=0
  if a==c:
    a=c=0
    
  return a+b+c