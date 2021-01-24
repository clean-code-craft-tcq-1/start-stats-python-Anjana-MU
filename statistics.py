import math

def calculateStats(numbers):
  Dict = {}
  if len(numbers) == 0:
    Dict = dict.fromkeys(['avg','min','max'],math.nan)   #Sets all stats value to Nan for an empty list
  else:
    Dict["avg"] = sum(numbers)/len(numbers)
    Dict["min"] = min(numbers)
    Dict["max"] = max(numbers) 
  return Dict
