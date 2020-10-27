def movements():
  path=[ "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  path= movements()
  print("{0} for {1} steps".format(path[0],path[1])) 
  print("{0} for {1} steps".format(path[2],path[3])) 
  print("{0} for {1} steps".format(path[4],path[5])) 
  print("{0} for {1} steps".format(path[6],path[7])) 
run() 


  