def cat_dog(str):
    count = 0
    for i in range(len(str)):
        cursor = str[i:i+3]
        if cursor == "dog": count +=1
        if cursor == "cat": count-=1
    if count==0: return True
    return False
