import json 

hospitals_list = []

# Reads from Json file and then return as a list
def exportFromJson(filename):
  with open(filename, "r") as f:
    hospitalsJson = json.loads(f.read())
    for value in hospitalsJson:
      hospitals_list.append(value)
  return hospitals_list


def extractPostalCode(str):
  postalCode = str[-6:]
  return postalCode


# Given a list of postal codes, returns a sorted list using recursion (decomposition)
# Decomposition: Using divide and conquer method to break a problem into smaller problems
def sortPostalCodes(l):
  if len(l) <= 1: # base case
    return l
  else: # recurive step
    return sortPostalCodes([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
        sortPostalCodes([e for e in l[1:] if e > l[0]])

postalCode_list = ['529889', '258500', '768828', '574623', '119074', '609606', '427990', '188770', '544886', '169608', '308433', '159964', '229899', '217562', '228510', '329563', '307677', '289891', '619771', '547530', '539747', '609606', 
'768024', '169610', '169609', '308433', '308205', '168751', '168582', '544835', '529895', '329562', '569766', '659674']
postalCode_list = [int(i) for i in postalCode_list]
# print(sortPostalCodes(postalCode_list))
