#%% exercise_1_7_areas_of_shapes.py
# Exercise 1.7 (areas of shapes)
# Interactive program to compute areas of triangle, rectangle and circle.
# The program:
#  - repeatedly asks which shape to compute,
#  - an empty input exits the loop,
#  - unknown shapes print "Unknown shape!" and continue,
#  - dimensions are read with float(...) (no validation),
#  - area is printed using the 'f' format specifier (six decimals by default).

from math import pi

def area_triangle(base: float, height: float) -> float:
    """Return area of triangle = base * height / 2."""
    return base * height / 2.0

def area_rectangle(width: float, height: float) -> float:
    """Return area of rectangle = width * height."""
    return width * height

def area_circle(radius: float) -> float:
    """Return area of circle = pi * r^2."""
    return pi * (radius ** 2)

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").strip().lower()
        # exit on empty string
        if shape == "":
            break

        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = area_triangle(base, height)
            print(f"The area is {area:f}")
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = area_rectangle(width, height)
            print(f"The area is {area:f}")
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = area_circle(radius)
            print(f"The area is {area:f}")
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
