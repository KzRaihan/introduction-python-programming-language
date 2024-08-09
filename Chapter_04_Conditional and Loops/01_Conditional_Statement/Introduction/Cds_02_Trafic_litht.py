# Traffic light problem
"""
  >> if light red = stop
  >> if light yellow = slow down
  >> if light green = go
  >> otherwise = light can't work or light is broken.
"""
# input form user
light = input("Enter light color: ")

if(light == "red" or light == "Red" or light == "RED"):
    print("Stop\n")
elif(light == "yellow"):
    print("Slow down\n")
elif(light == "green"):
    print("Go\n")
else:
    print("Light is broken")
