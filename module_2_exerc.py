"""
This code contains my solutions for ISP Module 1 exercises
"""

def first_last(a_string):
    """
    This code prints out the first and last character of a string.
    Input:
        a_string : input string
    Output:
        a string of two characters representing the first and last
        last character of the string provided.
    """
    if len(a_string) >= 2:
        return a_string[0] + a_string[-1]
    else:
        print("Please, provide a string with two characters at least")


def middle(a_string):
    """
    This code prints out the middle substring of a string by removing
    first and last characters.
    Input:
        a_string : input string
    Output:
        a substring representing the middle characters of the provided
        string without first and last characters.
    """
    if len(a_string) >= 3:
        return a_string[1:-1]
    else:
        print("Please, provide a string with three characters at least")

def threes(a_string):
    """
    This code prints out a string formed by extrated two sliced
    versions of the provided string, each slice being three characters
    long.
    Input:
        a_string : input string
    Output:
        A concatenate string of two three-characters sliced substrings
        of a_string
    """
    if len(a_string) >= 3:
        return a_string[: 3] + a_string[-3 :]
    else:
        print("Please, provide a string with three characters at least")

def echo(a_string, repeats):
    """
    This function takes a string 𝚌𝚊𝚕𝚕 and an integer 𝚛𝚎𝚙𝚎𝚊𝚝𝚜
    and prints 𝚛𝚎𝚙𝚎𝚊𝚝𝚜 copies of the string a_string to console,
    each on a separate line.
    Input:
        a_string : string to display
        repeats : number of repetitions
    Output:
        output_message : the resulting string to display.
    """

    if len(a_string) <= 0:
        print("Please, provide a string with one character at least")
    elif repeats <= 0:
        print("Enter a positive number for the second argument")
    else:
        output_message = (a_string + "\n") * repeats
        print(output_message)

def is_substring(a_string, a_substring):
    """
    This function tests if a given string is a substring of another
    and return True of False accordingly.
    Input:
        a_string : the string to test against.
        a_substring : the string to test.
    Output:
        Boolean True if a_substring is a substring of a_string and
        False, otherwise
    """
    return (a_substring in a_string)

def name_tag(name, topic):
    """
    This function takes two strings 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚝𝚘𝚙𝚒𝚌 and returns
    the string "𝙷𝚒! 𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 𝚇𝚇𝚇. 𝚃𝚑𝚒𝚜 𝚕𝚎𝚌𝚝𝚞𝚛𝚎 𝚌𝚘𝚟𝚎𝚛𝚜 𝚈𝚈𝚈."
    where 𝚇𝚇𝚇 is replaced by 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚈𝚈𝚈 is replaced by 𝚝𝚘𝚙𝚒𝚌
    Input:
        name : a string representing the name to print out.
        topic : a string representing the related topic
    Output:
        None, just a print out.
    """

    print("Hi! My name is {name}. This lecture covers {topic}.".\
    format(name = name, topic = topic))



def make_int(int_string):
    """
    This function takes as input the string 𝚒𝚗𝚝_𝚜𝚝𝚛𝚒𝚗𝚐 and checks
    whether 𝚒𝚗𝚝_𝚜𝚝𝚛𝚒𝚗𝚐 can be converted to a non-negative integer.
    If so, the function returns that integer.
    Otherwise, the function returns the integer -𝟷.
    """
    try:
        int_int = int(int_string)
    except:
        print("The input string cannot be converted to an integer")
        #raise
        return -1
    else:
        return int_int

def name_swap(name_string):
    """
    This function converts an input string 𝚗𝚊𝚖𝚎_𝚜𝚝𝚛𝚒𝚗𝚐 of the form
    "f𝚒𝚛𝚜𝚝 l𝚊𝚜𝚝" into the form "𝙻𝚊𝚜𝚝 𝙵𝚒𝚛𝚜𝚝" and returns
    this converted string
    Input:
        name_string = a string that in the form 'Firstname Lastname'
    Output:
        a string of the form 'Lastname Firstname'
    """
    names = name_string.split(' ')
    if len(names) <= 1 or len (names) > 3:
        print("Please provide a first name and a last name separated\
        by a single space")
    else:
        return names[-1].capitalize() + " " + names[0].capitalize()
