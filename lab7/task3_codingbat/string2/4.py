def count_code(str):
  count = 0
  for i in range(len(str)):
      cursor = str[i:i+4]
      if cursor[:2] == "co" and cursor[len(cursor)-1:len(cursor)]=="e": count +=1
  return count
