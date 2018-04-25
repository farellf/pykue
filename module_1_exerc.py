"""
This code contains my solutions for ISP Module 1 exercises
"""
import math
import random

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

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
    print("Todays numbers are {}, {}, {}, {}, {}. \n \
    The Powerball number is : {:*^15}".format(s(),s(),s(),s(),s(),\
    random.randrange(1,36)))

def is_even(number):
    """
    This code tests if a given number is even, then returns true or
    false, otherwise.
    Input:
        number = the number (should be integer type) to test.
    Output:
        A boolean True or False.
    """
    return (number % 2 == 0)

def is_cool(name):
    """
    This funny code tests if a given name is cool, then returns true or
    false, otherwise. The coolest names are hard coded in the list
    cool_list below.
    Input:
        name = the name (should be a string) to test.
    Output:
        A boolean True or False.
    """
    cool_list = ["FARELL", "JOE", "STEPHEN", "JOHN"]

    return (name.upper() in cool_list)

def is_lunchtime(hour, is_am):
    """
    This code tests if it is lunctime given the time.
    Input:
        hour = current hour in two digits integers hh
        is_am = Boolean True if is am, False if pm
    Output:
        A boolean True or False.
    """

    return ((hour == 12 and not is_am) or (hour == 11 and is_am))

def is_leap_year(year):
    """
    This code tests if a given year is leap and return true or False
    accordingly.
    Input:
        year = year to test as four digits integer
    Output:
        A boolean True if the year is leap or False, otherwise.
    """

    return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))

def interval_intersect(a,b,c,d):
    """
    This code tests if two intervals intersect
    Input:
        (a,b) represents first interval [a, b]
        (c,d) represents second interval [c, d]
    Output:
        A boolean True if the the intersection is not empty
         or False, otherwise.
    """
    return (a <= c <= b <= d) or (c <= a <= d <= b)


def name_lookup(firstname):
    """
    This funny code lookups the nam of a person given its firstname
    Input:
        firstname = a string
    Output:
        Returns the name corresponding to that firstname if it exists
        in the table or print an error message.
    """
    names_dict = {"JOE":"Warren", "SCOTT": "Rixner", "JOHN" : "GREINER",\
    "STEPHEN" : "Wong"}

    if firstname.upper() in names_dict:
        return names_dict[firstname.upper()]
    else:
        print("There is no entry for that firstname")
        return '""'

def test_function(function_name, *args):
    """
    This function helps test any function within this file
    by given its name followed by its arguments.
    Inputs:
        function_name : the exact name of the function
        *args : arguments of the function to call separated by a comma
    Output:
        Return the function output for the arguments provided.
    """
    try:
        print("Executing the function {}".format(function_name))
        print("...")
        return_value =function_name(*args)
        print("The function returned : {}".format(return_value))
    except:
        print("The called function returned an error")
    finally:
        print("Thanks for testing!")

# Uncomment to test by providing the name of the function to tests
# followed by its arguments
#test_function(function_name, *args)
