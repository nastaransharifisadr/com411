def direction():
  directions=[ "Move Forward", "Move Backward", "Move Left", "Move Right"]
  return directions

def menu():
  print("Please select a direction:")  
  path= direction()
  for index in range(len(path)):
      print("{0}:{1}".format(index,path[index]))




menu() 
