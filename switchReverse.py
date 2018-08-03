def switchReverse(myList):
  if all(isinstance(n, int) for n in myList)==True:
    myList.reverse()
    return myList
  
  elif all(isinstance(n, str) for n in myList)==True:
    y=[n.upper() for n in myList]
    return y
  
  else:
    return myList
