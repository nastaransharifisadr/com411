def direction():
  directions=[ "Move Forward", "Move Backward", "Move Left", "Move Right"]
  return directions

def menu():
  print("Please select a direction:")  
  path= direction()
  for index in range(len(path)):
      print("{0}:{1}".format(index,path[index]))
  num= int(input())
  return path[num]

def run():
  route= []
  print("Working out escape route...")
  for counter in range(5):
     route.append(menu())
     
  print("escape route: {0}".format(route))


run()  