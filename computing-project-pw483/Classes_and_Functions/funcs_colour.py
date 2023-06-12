import numpy as np
import random
import math
from typing import List  # for the function annotation
from Classes_and_Functions.classes import Pattern, Index


"""This file contains all the functions needed for the colour array encryption, used for the coloured input images.
The docstrings of each funciton should be self explanatory.
"""


def Is_element_in_dict(dict, element: List):
    """
    This function returns boolean result of whether the pixel element has been assigned a key in dict or not.  
    """

    t_or_f = []  # initialise a list to store the boolean result after checking with all the keys

    for x in dict:

        t_or_f2 = []     # store the boolean result after comparing all colour elements to colour elements

        for y in range(len(element)):
            # Check for each colour inside the pixel element

            # round to 3 decimal places since human eye resolution is not high enough to distinguish pixel elements to higher degree
            if round(dict[x][y], 3) == round(element[y], 3):
                t_or_f2.append(True)

            else:
                t_or_f2.append(False)

        # all() gives True result if all of the colour elements inside the pixel match those in one of the dict values otherwise False
        t_or_f.append(all(t_or_f2))

    # any() returns True if any of the pixel elements have been assigned a key in dict
    return any(t_or_f)


def find_key(dict, element: List):
    """
    Find dictionary key from its value (element:List)
    """
    for i in dict:

        t_or_f = []

        for j in range(3):

            if round(dict[i][j], 3) == round(element[j], 3):
                t_or_f.append(True)
            else:
                t_or_f.append(False)

        if all(t_or_f):
            return i


def find_enclosed_positions(size, pixels: List):
    """"
    Receive the pixel matrix and its size
    Return a list containing all the positions that are enclosed in 4 directions by other colour
    """
    positions = []
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            up = pixels[i][j-1]
            down = pixels[i][j+1]
            left = pixels[i-1][j]
            right = pixels[i+1][j]
            centre = pixels[i][j]

            potential_enclosement_check = all(
                [up == down, up == left, up == right])

            if potential_enclosement_check and up != centre:
                positions.append([i, j])
    return positions


def read_pattern_array(N, colour, pattern: Pattern):
    """
    This function receives the patten size(NxN), the colour dictionary and the pattern of consideration 
    Return readable_array for plt.imshow()
    """
    readable_array = np.zeros(
        (N, N, 3))  # initialise the desired array as shape (N,N.3)

    for m in range(N):
        for n in range(N):
            key_mn = pattern.pixels[m][n]
            for o in range(3):
                readable_array[m][n][o] = colour[key_mn][o]

    return readable_array
