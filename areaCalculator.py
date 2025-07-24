import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

# Example usage
print("Select shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    r = float(input("Enter radius of the circle: "))
    print(f"Area of Circle = {area_of_circle(r):.2f}")

elif choice == '2':
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    print(f"Area of Rectangle = {area_of_rectangle(l, w):.2f}")

elif choice == '3':
    b = float(input("Enter base of the triangle: "))
    h = float(input("Enter height of the triangle: "))
    print(f"Area of Triangle = {area_of_triangle(b, h):.2f}")

else:
    print("Invalid choice")
