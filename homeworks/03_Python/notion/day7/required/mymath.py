import math

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

def cuboid_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

def add(num1, num2):
    return num1+num2