def xyz_there(str):
  
  for i in range(len(str)):
    cursor = str[i:i+3]
    if cursor == "xyz":
        if str[i-1:i+3]!=".xyz":
          return True
  return False    
    