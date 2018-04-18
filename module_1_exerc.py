"""
This code contains my solutions for ISP Module 1 exercises
"""

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

<<<<<<< HEAD
def time_to_seconds(formatted_time):
=======
def time_to_second(formatted_time):
>>>>>>> b632ee2525ca48d3d3180d6dd2e6de215f009495
    """ This converts a given time into number of seconds.
    Inputs:
        A string representing the time in the format hh:mm:ss
    Output:
        Number of seconds representing that time, i.e there are 86400 sec\
        in 24 hours or 24:00:00
    """

    [hh, mm, ss] = formatted_time.split(":")
    time_in_sec = int(hh) * 3600 + int(mm) * 60 + int(ss) * 60
    return time_in_sec


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
