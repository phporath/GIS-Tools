uniqueList = []
def isDuplicate(inValue):
  if inValue in uniqueList:
    return 1
  else:
    uniqueList.append(inValue)
    return 0
	
---------

# trocar o !SNV_ROD_CO! pelo campo em questão.
isDuplicate (!SNV_ROD_CO!)
