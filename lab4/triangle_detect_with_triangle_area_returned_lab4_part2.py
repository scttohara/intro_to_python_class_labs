"""
program takes 3 user inputs and returns if it a triangle and the area squared

"""


def detect_triangle_and_return_area_squared():
    """

    :return: str with triangle, or not triangle, and the area squared
    """
    a = float(input("Lets see if we can make a triangle\nPlease enter a float for length 'a':\n"))

    b = float(input("Please enter another float for length 'b':\n"))

    c = float(input("Please enter one last float for length 'c':\n"))

    #  semi-perimeter calculation
    s = (a + b + c) / 2.0

    #  area_squared calculation using heron's formula
    area_squared = (s * (s - a) * (s - b) * (s - c))

    if area_squared > 0:
        print("IS A TRIANGLE: AREA SQUARED = " + str(area_squared))
    else:
        print("IS NOT A TRIANGLE: AREA SQUARED = " + str(area_squared))


detect_triangle_and_return_area_squared()

"""
TESTS
"""
#  should return yes triangle
"""
detect_triangle_and_return_area_squared(5, 5, 5)

detect_triangle_and_return_area_squared(10, 10, 2)

detect_triangle_and_return_area_squared(3, 4, 5)

detect_triangle_and_return_area_squared(6, 8, 7)

print("\n")

#  should return no triangle

detect_triangle_and_return_area_squared(10, 10, 30)

detect_triangle_and_return_area_squared(1, 3, 7)

detect_triangle_and_return_area_squared(18, 27, 44.999999999999999)
"""
