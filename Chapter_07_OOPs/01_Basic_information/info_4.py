# Create a class Room to calculate the area of the different Room(Study_Room, Family_Room)
class Room:
    # attributes
    lenght = 0.0
    breadth = 0.0
    
    # method
    def calculate_area(self):
        print("Area of the Room: ",self.length * self.breadth)

# Create object of Room class
# first object
Study_Room = Room()
Study_Room.length = 10.50
Study_Room.breadth = 12.80
Study_Room.calculate_area()

# second object
Family_Room = Room()
Family_Room.length = 20.25
Family_Room.breadth = 25.50
Family_Room.calculate_area()