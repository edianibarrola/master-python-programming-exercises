# class Box(object): #(object) ending not required
#   def __init__(self, color, width, height): # Constructor: These parameters will be used upon class calling(Except self)
#     self.color = color # self refers to global variables that can only be used throughout the class
#     self.width = width
#     self.height = height
#     self.area = width * height
#   def writeAboutBox(self): # self is almost always required for a function in a class, unless you don't want to use any of the global class variables
#     print(f"I'm a box with the area of {self.area}, and a color of: {self.color}!")

# greenSquare = Box("green", 10, 10) #Creates new square
# greenSquare.writeAboutBox() # Calls writeAboutBox function of greenSquare object

class Upper:
    def __init__(self, )