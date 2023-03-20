def last2(str):
  word = str[len(str)-2:len(str)]
  cnt = 0
  for i in range(0,len(str)-2):
    j = i+2
    if str[i:j] == word:
      cnt+=1
  return cnt
    