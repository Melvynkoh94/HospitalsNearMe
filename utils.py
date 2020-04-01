import json 

# with open("wheel.json", "r") as f:
#   wheelInfo = json.loads(f.read())
#   for value in wheelInfo:
#     colour_list.append(value['colour'])
#     text_list.append(value['text'])

hospitals_list = []

# Reads from Json file and then return as a list
def exportFromJson(filename):
  with open(filename, "r") as f:
    hospitalsJson = json.loads(f.read())
    for value in hospitalsJson:
      hospitals_list.append(value)
  return hospitals_list


# exportFromJson("hospitals_list.json")

# for i in range(34):
#   print(hospitals_list[i])


def extractPostalCode(str):
  postalCode = str[-6:]
  return postalCode