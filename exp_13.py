''' 13. WAP that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle.'''

def isRightTriangle(a, b, c):  # Function to check if the triangle is a right triangle
    sides = sorted([a,b,c]) # Sort the sides to identify the hypotenuse
    return sides[0]**2 + sides[1]**2 == sides[2]**2  # Check Pythagorean theorem

# Main Execution
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if isRightTriangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")