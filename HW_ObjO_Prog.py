# Homework Object Oriented Programming

# Problem: Fill in the line methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.  
class Line:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5

	def slope(self):
		return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

# Testing class
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.coor1)
print(li.coor2)
slope = li.slope()
print("The Line slope is: {}".format(slope))
print("The Line distance is: {}\n".format(li.distance()))

# Problem: Fill in the class
class Cylinder:

	pi = 3.1415

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return Cylinder.pi*(self.radius**2)*self.height

	def surface_area(self):
		top_bottom = 2 * (Cylinder.pi * (self.radius**2))
		sides = 2 * Cylinder.pi * self.radius * self.height
		return top_bottom + sides

# Testing of the Cylinder Class:
c = Cylinder(2,3)
print("The volume of the cylinder is: {}".format(c.volume()))
print("The surface area of the cylinder is: {}\n".format(c.surface_area()))

