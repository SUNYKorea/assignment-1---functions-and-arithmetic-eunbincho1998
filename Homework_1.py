# Name: Eunbin Cho
# SBUID: 115935488

# Remove the ellipses (...) when writing your solutions.

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



'''
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    ...

def euclidean_distance(x1, y1, x2, y2):
    ...

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    ...


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    ...

def apothem(number_sides, length_side):
   ...

def polygon_area(number_sides, length_side):
   ...


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