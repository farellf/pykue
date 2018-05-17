"""
This code contains my solutions for ISP Module 2 exercises
"""
import random
import math
import re

def string_first_last(a_string):
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


def string_middle(a_string):
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



def string_to_int(int_string):
    """
    This function takes as input the string 𝚒𝚗𝚝_𝚜𝚝𝚛𝚒𝚗𝚐 and checks
    whether 𝚒𝚗𝚝_𝚜𝚝𝚛𝚒𝚗𝚐 can be converted to a non-negative integer.
    If so, the function returns that integer.
    Otherwise, the function returns the integer -𝟷.
    """
    try:
        # alternatively on can use is_digit() and int without a try
        # clause
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

def compute_primes(bound):
    """
    This function returns a list of the prime numbers in
    range(2, bound)
    Input:
        bound: the upper bound of the ranger to search in.
    Output:
        A list of primes numbers in range [0, bound)
    """
    primes_list = list(range(2, bound))
    for divisor in range(2, bound):
        if divisor in primes_list:
            div_index = primes_list.index(divisor)
            for num in primes_list[div_index + 1 :]:
                if num % divisor == 0:
                    primes_list.remove(num)
    return primes_list

def is_prime(number):
    """
    This function test whether a number is prime and returns True or
    False accordingly.
    Input:
        number : number to test.
    Output:
        A boolean True if the number is prime and False otherwise.
    """
    # Create a list of primes numbers between 2 and the number to test
    primes_list = compute_primes(number + 1)

    return number in primes_list

def primes_list(n, max):
    """
    This function computes a list that contains n random primes
    numbers within the range [0, max]
    Input:
        n =  the number of primes numbers to compute.
        max =  the upper bound of the range of interest.
    Output:
        a list containing n randoms prime numbers between 2 and max
    """
    primes_list = compute_primes(max + 1)
    num_primes = len(primes_list)
    n_primes = []
    if num_primes < n:
        print("There is/are only {} prime(s) for the specified range.\
        Please try with a bigger max value.".format(num_primes))
        n_primes = primes_list
    else:
        while len(n_primes) < n:
            n_primes.append(random.choice(primes_list))
    return n_primes

def list_first_last(a_list):
    """
    This code prints out the first and last character of a list.
    Input:
        a_list : input list
    Output:
        a list of two elements representing the first and last
        last elements of the list.
    """
    if len(a_list) >= 2:
        return [a_list[0], a_list[-1]]
    else:
        print("Please, provide a list with two elements at least")

def list_middle(a_list):
    """
    This code prints out the middle sublist obtaining by excluding
    the first and last elements of the input list a_list
    Input:
        a_list : input list
    Output:
        a sublist representing the middle elements of the provided
        list without first and last elements.
    """
    if len(a_list) >= 3:
        return a_list[1:-1]
    else:
        print("Please, provide a list with three at least elements.")

def true_false():
    pass

def word_count(text, word):
    """
    This function takes a string 𝚝𝚎𝚡𝚝 and a string 𝚠𝚘𝚛𝚍 as input.
    It then splits the string of text into a list of words and count
    the number of times that 𝚠𝚘𝚛𝚍 appears in the text.
    """
    return word.count(text)


def list_max(num_list):
    """
    This function takes a non-empty list of numbers 𝚗𝚞𝚖_𝚕𝚒𝚜𝚝 and
    returns maximum (largest) number in the list, without using
    built-in python max function.
    """
    largest = - (math.inf)
    if len(num_list) > 0:
        largest = num_list[0]
        for dummy_num in num_list:
            if dummy_num > largest:
                largest =  dummy_num
    return largest

def concatenate_int(int_list):
    """
    The function takes a list of non-negative integers in int_list and
    𝚌𝚘𝚗𝚌𝚊𝚝𝚎𝚗𝚊𝚝𝚎 into a single integer formed by concatenating the
    digits of the integer in the list
    """
    args = tuple(int_list)
    length = len(int_list)
    return ("{:d}" * length).format(*args)

def flatten(a_nested_list):
    """
    Given a list whose items are list,
    return the list formed by joining all of these lists
    """
    flattened_list = []
    for sublist in a_nested_list:
        flattened_list.extend(sublist)
    return flattened_list

def remove_duplicates(a_list):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    no_duplicates = set(a_list)
    return list(no_duplicates)

### The following codes implement functions to update codeskulptor
### docs in order to take into account changes from Python 2
### to Python 3, especially for print statements.

def update_line(line):
    """
    This function takes a string 𝚕𝚒𝚗𝚎 corresponding to a single line
    of Python 2 code. If the line corresponds to a 𝚙𝚛𝚒𝚗𝚝 statement,
    the function updates the string such that the arguments to 𝚙𝚛𝚒𝚗𝚝
    are enclosed in parentheses. Any white space corresponds
    to indentation is preserved. If the line does not correspond to a
    𝚙𝚛𝚒𝚗𝚝 statement, the line is left unchanged.
    Input:
        line : a string line
    Output:
        line : an updated string line.
    """
    # Find the index of the print statemen within the line
    if "print" in line:
        print_idx = line.find("print")
        return "{}print({})".format(line[:print_idx],\
        line[print_idx + 6 : ])
    return line
# print(update_line(""))
# print(update_line("foobar()"))
# print(update_line("print 1 + 's' + 1"))
# print(update_line("    print 2, 3, 4"))

def update_pre_block(pre_block):
    """
    This function takes a string 𝚙𝚛𝚎_𝚋𝚕𝚘𝚌𝚔 corresponding to code
    example enclosed by a pair of <𝚙𝚛𝚎>...</𝚙𝚛𝚎> tags and returns
    a version of the text with the syntax of any enclosed 𝚙𝚛𝚒𝚗𝚝
    statements updated from Python 2 to Python 3.
    Input:
        pre_block :  the bloc to update
    Output:
        an updated pre_block
    """
    # Split the pre_block into line if any \n character present
    blocks = pre_block.split("\n")
    updated_pre_block = []

    for line in blocks:
        updated_pre_block.append(update_line(line))
    num_prints = len(updated_pre_block)
    return ("{}\n" * (num_prints - 1) + "{}").format(*updated_pre_block)


def update_file(input_file_name, output_file_name):
    """
    This function opens and reads the file specified by the string
    input_file_name, processed the <pre> blocks in the loaded text to
    update print syntax, and finally writes the update text to
    the file specified by the string output_file_name
    """

    file_to_process = open(input_file_name, 'r')
    f = file_to_process.read()
    output_file = open(output_file_name, 'w')

    # ****** Regex option to explore laterself *****
    # pattern = r'<pre>(.*)</pre>'
    # for line in file_to_process.readlines():
    #     match = re.search(pattern, line)
    #     if match and "print" in match.group(1):
    #         updated_pre_block = update_pre_block(match.group(1))
    #         output_file.write(updated_pre_block + "\n")
    #     else:
    #         output_file.write(line)

    blocks = f.split("<pre class='cm'>")
    first_block = blocks[0]
    print(first_block)
    updated_blocks = first_block
    for block in blocks[1:]:
        updated_blocks += "<pre class='cm'>"
        [pre_block, remaining] = block.split("</pre>", 1)
        updated_blocks += update_pre_block(pre_block)
        updated_blocks += "</pre>"
        updated_blocks += remaining
    output_file.write(updated_blocks)
    file_to_process.close()
    output_file.close()
