'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

'''

import math

class Circle:
  def area(self, radius):
    r = radius**2
    area = math.pi*r
    print("Area of trhe circle is: {:.2f}".format(area))

c = Circle()
radius = float(input("Enter radius of the circle: "))
c.area(radius)