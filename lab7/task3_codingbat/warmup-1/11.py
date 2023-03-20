def front_back(str):
  if len(str)<=1: return str
  else:
    l = str[len(str)-1:]
    f = str[0:1]
    return l+str[1:len(str)-1]+f
