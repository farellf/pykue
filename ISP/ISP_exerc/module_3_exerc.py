"""
This code contains my solutions for Interactive Scription with Python
Course, Rice University on Coursera : Module 3 exercises

@__f_f__, April 2018.
"""
import random
import math
import re
import csv

PATH = "" # Set path for your files.

def is_empty(my_dict):
    """
    This code tests whether a the dictionnary my_dict is empty or not.
    It returns True or False accordingly.
    Input:
        my_dict = a dictionnary
    Output:
        True or False.
    """
    return len(my_dict) == 0

def value_sum(my_dict):
    """
    This code sums all values in a dictionnary, assuming that all
    values are numbers. It returns the computed sum.
    Input:
        my_dict : the dictionnary with the given key,value pairs
    Output:
        The sum of all values.
    """
    val_sum = 0
    for key,val in my_dict.items():
        val_sum += val

    return val_sum


def make_dict(key_val_list):
    """
    This function creates a dictionnary from a list of tuples (a,b)
    and returns the computed dictionnary.
    Input:
        a list of tuples (pairs)
    Output:
        the corresponding dictionnary
    """

    output_dict = {}
    for (key,val) in key_val_list:
        output_dict[key] = val

    return output_dict

def encrypt(phrase, cipher_dict):
    """
    This code computes a simple substitution cipher which is an
    encryption scheme where each letter in an alphabet is replaced
    by a different letter in the same alphabet with the restriction
    that each letter's replacement is unique.
    Input:
        phrase : the string to encrypt
        cipher_dict :  a dictionnary where the values are
        the encrypted versions of the keys.
    Output:
        the cipher
    """

    cipher = ""
    for char in phrase:
        cipher += cipher_dict[char]
    return cipher

def make_decipher_dict(cipher_dict):
    """
    This function takes a cipher dictionary 𝚌𝚒𝚙𝚑𝚎𝚛_𝚍𝚒𝚌𝚝 and returns
    a new dictionary 𝚍𝚎𝚌𝚒𝚙𝚑𝚎𝚛_𝚍𝚒𝚌𝚝 with the property that applying
    𝚍𝚎𝚌𝚒𝚙𝚑𝚎𝚛_𝚍𝚒𝚌𝚝 to a phrase encrypted using 𝚌𝚒𝚙𝚑𝚎𝚛_𝚍𝚒𝚌𝚝 returns
    the original phrase.
    """

    decipher_dict = {}
    for key,val in cipher_dict.items():
        decipher_dict[val] = key

    return decipher_dict

def decrypt(cipher, cipher_dict):
    """
    This function duplicates the role of make_decipher_dict,
    so that it can use the same cipher_dict for both encryption and
    decryption.
    """

    phrase = ""
    dummy_key_list = list(cipher_dict.keys())
    dummy_val_list = list(cipher_dict.values())
    for char in cipher:
        if char in cipher_dict.values():
            phrase += dummy_key_list[dummy_val_list.index(char)]
    return phrase

def make_cipher_dict(alphabet):
    """
    This code computes a cipher_dict from a given set of characters
    in alphabet. It is a simple cipher based on randomization.
    """

    alphabet_list = list (alphabet)
    random.shuffle(alphabet_list)
    cipher_dict = {}
    for char in alphabet:
        cipher_dict[char] = alphabet_list.pop()

    return cipher_dict

def 𝚍𝚒𝚌𝚝_𝚌𝚘𝚙𝚒𝚎𝚜(𝚖𝚢_𝚍𝚒𝚌𝚝, 𝚗𝚞𝚖_𝚌𝚘𝚙𝚒𝚎𝚜):
    """
    This function takes a  dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 and an integer
    𝚗𝚞𝚖_𝚌𝚘𝚙𝚒𝚎𝚜 and returns  a list consisting of 𝚗𝚞𝚖_𝚌𝚘𝚙𝚒𝚎𝚜 copies
    of 𝚖𝚢_𝚍𝚒𝚌𝚝.
    """

    return [dict(my_dict) for num in range(num_copies)]


def make_dict_lists(𝚕𝚎𝚗𝚐𝚝𝚑):
    """
    A function  that takes an integer 𝚕𝚎𝚗𝚐𝚝𝚑 returns a dictionary
    whose keys are in 𝚛𝚊𝚗𝚐𝚎(𝚕𝚎𝚗𝚐𝚝𝚑) and whose corresponding values
    are lists of zeros whose length match the key.
    """
    return dict([(key,[0] * key) for key in range(length)])

def make_grade_table(name_list, grades_list):

    """
    Define a function 𝚖𝚊𝚔𝚎_𝚐𝚛𝚊𝚍𝚎_𝚝𝚊𝚋𝚕𝚎(𝚗𝚊𝚖𝚎_𝚕𝚒𝚜𝚝, 𝚐𝚛𝚊𝚍𝚎𝚜_𝚕𝚒𝚜𝚝) that
    takes a list of names 𝚗𝚊𝚖𝚎_𝚕𝚒𝚜𝚝 and a list of grade lists
    𝚐𝚛𝚊𝚍𝚎𝚜_𝚕𝚒𝚜𝚝 and returns a dictionary whose keys corresponds to
    names 𝚗𝚊𝚖𝚎_𝚕𝚒𝚜𝚝 and whose corresponding values are the items
    𝚐𝚛𝚊𝚍𝚎𝚜_𝚕𝚒𝚜𝚝.
    """

    return dict([(name, grade) for (name, grade) in \
    zip(name_list, grades_list)])

def read_csv_file(filename):
    """
    Given a file path specified as the string, 𝚏𝚒𝚕𝚎_𝚗𝚊𝚖𝚎 ,
    load the associated CSV file and return
    a nested list whose entries are the fields in the CSV file.
    Each entry in the returned table is of type 𝚜𝚝𝚛
    """
    nested_list = []
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for dummy_row in csvreader:
            nested_list.append(dummy_row)
    return nested_list

def write_csv_file(csv_table, filename):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated
    CSV file with the name file_name
    """
    with open(filename, 'wt', newline ='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',', quoting \
        = csv.QUOTE_MINIMAL)
        for dummy_row in csv_table:
            csvwriter.writerow(dummy_row)

def select_columns(my_table, col_indices):
    """
    Input: Nested list my_table and a list of integers col_indices
    Output: Nested list corresponding to sub-table formed by
    columns in col_indices
    """
    output_list = []

    for dummy_row in my_table:
        output_col = []
        for dummy_idx in col_indices:
            output_col.append(dummy_row[dummy_idx])
        output_list.append(output_col)

    return output_list

def sort_by_column(my_table, col_idx):
    """
    Input: Nested list my_table and an integer col_idx
    Action: Mutate the order of the rows in my_table such that the
    entries in the column col_idx appear in DESCENDING order when
    interpreted as numbers
    """
    my_table.sort(
    key = lambda dummy_row : float(dummy_row[col_idx]),reverse = True)
