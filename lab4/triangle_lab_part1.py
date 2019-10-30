"""
program reads three user inputs from 3 prompts. returns TRIANGLE or NOT TRIANGLE

"""
"""

    how to detect a triangle

    Three line segments, a, b, and c, can form a triangle if and only if
    length(a) + length(b) > length(c) AND
    length(a) + length(c) > length(b) AND
    length(b) + length(c) > length(a)
    """


def triangle_detect():
    """
    Identifies a triangle, given three sides by a user then tells the user
    if the three sides could form a triangle

    :return: nothing
    """
    a = float(input("Lets see if we can make a triangle\nPlease enter a float for length 'a':\n"))

    b = float(input("Please enter another float for length 'b':\n"))

    c = float(input("Please enter one last float for length 'c':\n"))

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("\nIS A TRIANGLE")
        return 0
    else:
        print("\nIS NOT A TRIANGLE")
        return 1


triangle_detect()

"""
simple TESTS
"""
#  should return yes triangle
"""
triangle_detect(5, 5, 5)

triangle_detect(10, 10, 2)

triangle_detect(3, 4, 5)

triangle_detect(6, 8, 7)

print("\n")

#  should return no triangle

triangle_detect(10, 10, 30)

triangle_detect(1, 3, 7)

triangle_detect(18, 27, 44.999999999999999)

"""
