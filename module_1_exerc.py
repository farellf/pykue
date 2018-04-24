"""
This code contains my solutions for ISP Module 1 exercises
"""
import math
import random

def mile_to_feet(distance_in_mile):
  """
  This function converts a distance in feet into mile unit
  Input:
    Distance in mile
  Output:
    The corresponding distance in mile.
  """
  distance_in_feet = distance_in_mile * 5280

  return distance_in_feet

def time_to_seconds(formatted_time):
    """
    This converts a given time into number of seconds.
    Inputs:
        A string representing the time in the format hh:mm:ss
    Output:
        Number of seconds representing that time, i.e there are 86400
        sec in 24 hours or 24:00:00
    """


    [hh, mm, ss] = formatted_time.split(":")
    time_in_sec = int(hh) * 3600 + int(mm) * 60 + int(ss) * 60

    return time_in_sec

def rectangle_perimeter(width, length):
    """
    This code takes a rectangle length and width and computes
    its perimeter
    Input:
        Width = smaller size of the rectangle
        Length = longer size of the rectangle

    Output:
        The perimeter of the rectangle
    """
    return 2 * (width + length)

def rectangle_area(width, length):
    """
    This code takes a rectangle length and width and computes
    its area
    Input:
        Width = smaller size of the rectangle
        Length = longer size of the rectangle

    Output:
        The area of the rectangle
    """
    return width * length

def circle_circonference(radius):
    """
    This code computes the circonference of a circle given its radius
    Input:
        Radius = the radius r of the cicrle

    Output:
        The circonference of the circle of radius r
    """
    return 2 * math.pi * radius

def circle_area(radius):
    """
    This code computes the area of a circle given its radius
    Input:
        Radius = the radius r of the cicrle

    Output:
        The area of the circle of radius r
    """
    return math.pow(radius,2) * math.pi


def future_value(init_amount, rate, years):
    """
    This code computes the future value of a initial placement at
    a given rate for a number of years
    Input:
        init_amount = the initial amount of the placement a year 0
        Rate = the rate of the placement in percentage
        (min is 0 and max is 1)
        Years = the number of year to take into account for computation
    Output:
        The future value after the given years
    """
    return init_amount * math.pow((1 + rate), years)

def concatenate_string(string_list)  :
    """
    This code concatenate many pieces of strings into a larger part
    and print it out to the screen
    Input:
        string_list = a list of strings
    Output:
        The larger string
    """
    larger_string = ""
    for dummy_string in string_list:
        larger_string += (dummy_string + " ")

    print(larger_string)

    return larger_string


def distance_2D(point_A, point_B):
        """
        This code computes the 2D euclidian distance between two points
        A and B
        Inputs:
            Point_A : the coordinates of the first point as a
            tuple (x_a,y_a)
            Point_B : the coordinates of the second point as a tuple
            (x_b,y_b)
        Output:
            Return the 2D distance between A and D
        """
        x_diff = point_A[0] - point_B[0]
        y_diff = point_A[1] - point_B[1]

        return math.sqrt(x_diff ** 2 + y_diff ** 2)

def triangle_area(point_A, point_B, point_C):
    """
    This code computes the area of a triangle given the coordinates of
    its three vertices.
    Input:
        Point_A = first vertice of the triangle as a tuple (x_a,y_a)
        Point_B = second vertice of the triangle as a tuple (x_b,y_b)
        Point_C = third vertice of the triangle as a tuple (x_c,y_c)
    Output:
        The area of the triangle
    """
    # Compute the three distances (edges length) between the vertices.
    a = distance_2D(point_A, point_B)
    b = distance_2D(point_B, point_C)
    c = distance_2D(point_A, point_C)

    # Compute the semi perimeter for the Heron's formula
    semi_peri = (a + b + c) / float(2)

    return math.sqrt(semi_peri * (semi_peri - a) * (semi_peri - b) \
    * (semi_peri - c))

def powerball ():
    """
    This code performs a small Powerball game
    Input:
        None
    Output:
        Print a message to display the randomly chosen numbers in a
        a range [1, 60) and the powerball chosen randomly in [1, 36)
    """
    todays_number = set()
    while len(todays_number) < 5:
        dummy_random = random.randrange(1,60)
        todays_number.add(dummy_random)

    print(todays_number)
    s = todays_number.pop
    print("Todays numbers are {}, {}, {}, {}, {}. \
    The Powerball number is : {:<2}".format(s(),s(),s(),s(),s(),\
    random.randrange(1,36)))


def test_function(function_name, arguments):
    """
    This function helps test any function within this file
    by submitting the function name and its argumentsself.
    Inputs:
        the exact funtion name.
    Output:
        Return the function output for the arguments provided.
    """
    # So far arguments is a single value, I will deal with list later
    try:

        if len(arguments) == 0:
             print(function_name())
        elif len(arguments) == 1:
            print(function_name(arguments[0]))
        else:
            dummy_string = ''
            for arg in arguments:
                dummy_string += "{},".format(arg)
            function_string = dummy_string[:-1]

            # The intention here is to run function_name(function_string)
            # However, function_string is still a string treated as one single\
            # variable by the function being called.
            # Therefore, I just return the string that shoud represent \
            # the values within the brackets. This code will be fixed later.
            # One way is to give the same signature to all the function, or always
            # use a list for their input.
            print(function_string)
    except:
        print("Executing '{}' generated an error".format(function_name))
