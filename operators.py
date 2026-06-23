# 23-june-2002
# operators
# 1. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# standard equation y = mx + c
import math 
m1 = 2

# for x - intercept y = 0 --> x = - c/m
c = -2
x = - c // m1

# for y - intercept x = 0 --> y = c
y = c 

print("slope: ", m1)
print(f"X intercept : {x}, 0")
print(f"Y intercept: {y}, 0")

# 2 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10

# slope
m2 = (y2 - y1) // (x2 - x1)

# euclidean distance 
eucild_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

print(f"Slope: {m2}")
print(f"Euclidean distance: {eucild_distance:.2f}")

# 3 compare both slopes
print(m1 >= m2) # True
print(m2 <= m1) # True 2 == 2

# 4 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = (x)**2 + (6 * x) + 9

print(f"Y = {y} at x = -3")

# 5 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") != len("dragon")) # False becaues I applied != that reverse the statemnt

#6 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))

months = years * 12
weeks = years * 52
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60 

print(f"You have lived for {seconds} seconds.")

#7 Write a Python script that displays the following table
a , b, d, e, f = 1, 2, 3, 4, 5

print(a * 1, a, a * 1, a ** 2, a ** 3 )
print(b * 1, a, b * 1, b ** 2, b ** 3 )
print(d * 1, a, d * 1, d ** 2, d ** 3 )
print(e * 1, a, e * 1, e ** 2, e ** 3 )
print(f * 1, a, f * 1, f ** 2, f ** 3 )
