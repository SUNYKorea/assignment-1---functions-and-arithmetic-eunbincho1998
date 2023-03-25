# Name: Eunbin Cho
# SBUID: 115935488

# Remove the ellipses (...) when writing your solutions.
'''
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):                               #convert fahrenheit to celsius
   celsius = (5/9)*(fahrenheit - 32)
   return celsius

def what_to_wear(celsius):                                        #returns the appropriate clothing choice based on temperature in celsius
   if celsius < -10:
      return "Puffy Jacket"
   if celsius == -10:
      return "Puffy Jacket or Scarf"
   if -10 < celsius < 0:
      return "Scarf" 
   if celsius == 0:
      return "Scarf or Sweater"
   if 0 < celsius < 10:
      return "Sweater"
   if celsius == 10:
      return "Sweater or Light Jacket"
   if 10 < celsius < 20:
      return "Light Jacket"
   if celsius == 20:
      return "Light Jacket or T-shirt"
   if celsius > 20:
      return "T-shirt"

print()
print("Let's convert the temperature from Fahrenheit to Celsius and see what clothing is recommended!")     #instruction
print()

TemperatureFahrenheit = float(input("What is the temperature in Fahrenheit? Temperature in Fahrenheit:  ")) 
ConvertedCelsius = fahrenheit2celsius(TemperatureFahrenheit)
DegreeSymbol = u"\N{DEGREE SIGN}"                                                   #to print degree sign
print()

print("The given temperature in Celsius is " + str(ConvertedCelsius) + DegreeSymbol + "C")
print()

SuggestedClothing = what_to_wear(ConvertedCelsius)                                  #takes the converted temperature to recommend clothes
print("Recommended clothing: " + SuggestedClothing)




# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):                        #Area function
    Area = abs((((x1*y2)+(x2*y3)+(x3*y1))-((x1*y3)+(x2*y1)+(x3*y2)))/2)
    return Area

def euclidean_distance(x1, y1, x2, y2):                                    #Distance function
    Distance = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5
    return Distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):                    #Perimeter function
    LengthOfSide1 = euclidean_distance(x1, y1, x2, y2)                     #Using Distance function
    LengthOfSide2 = euclidean_distance(x2, y2, x3, y3)
    LengthOfSide3 = euclidean_distance(x3, y3, x1, y1)
    Perimeter = LengthOfSide1 + LengthOfSide2 + LengthOfSide3
    return Perimeter

print()
print("Let's solve for the area and the perimeter of a triangle with its vertices!")         #Instruction
print()

x1 = float(input("What is x1? x1 = "))                                                       #Value inputs of three vertices
y1 = float(input("What is y1? y1 = "))
x2 = float(input("What is x2? x2 = "))
y2 = float(input("What is y2? y2 = "))
x3 = float(input("What is x3? x3 = "))
y3 = float(input("What is y3? y3 = "))
print()

TriangleArea = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)                                #Using area function
print("The area of the triangle is " + str(TriangleArea) + " squared units.")

TrianglePerimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)                       #Using perimeter function
print("The perimeter of the triangle is " + str(TrianglePerimeter) + " units.")
'''

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    rad = deg * math.pi / 180
    return rad

def apothem(number_sides, length_side):
   

def polygon_area(number_sides, length_side):
   

deg = float(input("angle = "))
rad = deg2rad(deg)
print(rad)
'''
# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

'''