"""Rectangle Rotation
Task - https://www.codewars.com/kata/5886e082a836a691340000c3
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?"""

import math
sq2 = math.sqrt(2)

def rectangle_rotation(a,b):
    result = (math.floor(a/sq2)+1)*(math.floor(b/sq2)+1) + (math.floor(a/sq2))*(math.floor(b/sq2))
    if result%2 == 0:
        result = result-1
    return result
