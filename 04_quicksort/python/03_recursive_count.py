def count(list):
  if len(list) == 0:
    return 0
  else:
    return arr[0] + count(list[1:])
  
 print(count([1,2,3,4,5]))
