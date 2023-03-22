def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if a.find(b)>=0:
    if a[len(a)-len(b):]==b:
      return True
      
  if b.find(a)>=0:
    if b[len(b)-len(a):]==a:
      return True
  return False