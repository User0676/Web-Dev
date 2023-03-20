def string_splosion(str):
  word = ""
  for i in range(0,len(str)+1):
    word+=str[0:i]
  return word
