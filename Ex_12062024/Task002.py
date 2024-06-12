# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3
#
side1 = int(input("Enter side 1 of triangle: "))
side2 = int(input("Enter side 2 of triangle: "))
side3 = int(input("Enter side 3 of triangle: "))

if side1 == side2 and side1 == side3 and side2 == side3 and side1 !=0 and side2 !=0 and side3 !=0:
    print("Triangle is equilateral")
elif side1 == side2 and side2 != side3 and side1 != side3 and side3 !=0:
    print("Triangle is isosceles")
elif side1 == side3 and side1 != side2 and side3 != side2 and side2 !=0:
    print("Triangle is isosceles")
elif side2 == side3 and side2 != side1 and side3 != side1 and side1 !=0:
    print("Triangle is isosceles")
elif side1 != side2 and side2 != side3 and side3 != side1 and side1 !=0 and side2 !=0 and side3 !=0:
    print("Triangle is scalene")
else:
    print("Triangle is not a triangle")


