"""
This code contains my solutions for ISP Module 3 exercises
"""
import random
import math
import re

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
        cipher_dict :  a dictionnary where the values are the encrypted
        versions of the keys.
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
