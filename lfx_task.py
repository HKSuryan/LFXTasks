def prog(listOfInteger:list):
  for ele in listOfInteger:
    if not isinstance(ele, int):
       return"Error: List is not a list of integers"

  if isinstance(listOfInteger,str) or len(listOfInteger) == 0:
    return"Error: List is not a list of integers"

  
  if len(listOfInteger)%10 != 0:
    return"Error: List is not a multiple of 10 in length"

  else:
    return [listOfInteger[i] for i in range(len(listOfInteger)) if (i+1)%2 != 0 and (i+1)%3 != 0]

#Example
print(prog([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))


#Empty list

print(prog([]))

#List with length not a multiple of 10
print(prog([1,2,3,4,5,6,7,8]))

#List with other datatypes also included
print(prog([1,2,3,4,5,6,7,"Hi",9,10,11,12,13,14,15,"Hello",17,18,19,20]))

#List with length 9 (boundary of not a multiple of 10):
print(prog([1,2,3,4,5,6,7,8,9]))


#List with negative integers
print(prog([1,2,3,4,5,6,7,8,9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]))
