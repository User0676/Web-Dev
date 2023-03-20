def front3(str):
  if len(str)<3:
    return str+str+str
  else:
    m = str[0:3]
    return m+m+m
