import numpy as np
import random
import math
from typing import List  # for the function annotation
from Classes_and_Functions.classes import Pattern, Index


"""This file contains all the functions needed for the wavefunction collapse algorithm.
The docstrings of each funciton should be self explanatory.
"""


def get_all_rotations(pixelMatrix):
    """
    Return original array as well as rotated by 90, 180 and 270 degrees in the form of tuples
    #range(start,stop,increment) will be used 
    """
    pixelMatrix_rotated_1 = [[pixelMatrix[j][i] for j in range(
        len(pixelMatrix))] for i in range(len(pixelMatrix[0])-1, -1, -1)]
    pixelMatrix_rotated_2 = [[pixelMatrix_rotated_1[j][i] for j in range(len(
        pixelMatrix_rotated_1))] for i in range(len(pixelMatrix_rotated_1[0])-1, -1, -1)]
    pixelMatrix_rotated_3 = [[pixelMatrix_rotated_2[j][i] for j in range(len(
        pixelMatrix_rotated_2))] for i in range(len(pixelMatrix_rotated_2[0])-1, -1, -1)]
    return tuple(tuple(row) for row in pixelMatrix), \
        tuple(tuple(row) for row in pixelMatrix_rotated_1), \
        tuple(tuple(row) for row in pixelMatrix_rotated_2), \
        tuple(tuple(row) for row in pixelMatrix_rotated_3)


def get_all_rotations2(pixelMatrix):
    """
    Return original array in the form of tuples. This function will be used for the flower case
    #range(start,stop,increment) will be used 
    """
    pixelMatrix_rotated_1 = [[pixelMatrix[j][i] for j in range(
        len(pixelMatrix))] for i in range(len(pixelMatrix[0])-1, -1, -1)]
    pixelMatrix_rotated_2 = [[pixelMatrix_rotated_1[j][i] for j in range(len(
        pixelMatrix_rotated_1))] for i in range(len(pixelMatrix_rotated_1[0])-1, -1, -1)]
    pixelMatrix_rotated_3 = [[pixelMatrix_rotated_2[j][i] for j in range(len(
        pixelMatrix_rotated_2))] for i in range(len(pixelMatrix_rotated_2[0])-1, -1, -1)]
    return tuple(tuple(row) for row in pixelMatrix_rotated_1), \
        tuple(tuple(row) for row in pixelMatrix_rotated_1), \
        tuple(tuple(row) for row in pixelMatrix_rotated_1), \
        tuple(tuple(row) for row in pixelMatrix_rotated_1)


def get_overlapping_tiles(pattern: Pattern, overlap: tuple):
    """
    This function receives the next pattern after the base pattern and 'overlap' 
    ,which is the relative index of the propagation direction.
    It returns a tuple of overlapping elemnet(s) coresponding to each direction of propagation  
    """
    if overlap == (0, 0):
        return pattern.pixels
    if overlap == (-1, -1):
        return tuple([pattern.pixels[1][1]])
    if overlap == (0, -1):
        return tuple(pattern.pixels[1][:])
    if overlap == (1, -1):
        return tuple([pattern.pixels[1][0]])
    if overlap == (-1, 0):
        return tuple([pattern.pixels[0][1], pattern.pixels[1][1]])
    if overlap == (1, 0):
        return tuple([pattern.pixels[0][0], pattern.pixels[1][0]])
    if overlap == (-1, 1):
        return tuple([pattern.pixels[0][1]])
    if overlap == (0, 1):
        return tuple(pattern.pixels[0][:])
    if overlap == (1, 1):
        return tuple([pattern.pixels[0][0]])


UP = (0, -1)   # index of the pixel above relative to the pixel of interest
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
dirs = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]


def valid_dirs(pos, output_size):
    """
    receive coordinated of the pixel of interest and return a list of possible propagation directions
    ,which are up,left,down,right,up_left,up_right,down_right,down_left as tuples of relative propagatible indices
    """

    x, y = pos  # pixel oordinate of the place of interest in the output

    valid_directions = []

    if x == 0:
        valid_directions.extend([RIGHT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_RIGHT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_RIGHT])
        else:
            valid_directions.extend([DOWN, DOWN_RIGHT, UP, UP_RIGHT])
    elif x == output_size[0]-1:
        valid_directions.extend([LEFT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_LEFT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_LEFT])
        else:
            valid_directions.extend([DOWN, DOWN_LEFT, UP, UP_LEFT])
    else:
        valid_directions.extend([LEFT, RIGHT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_LEFT, DOWN_RIGHT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_LEFT, UP_RIGHT])
        else:
            valid_directions.extend(
                [UP, UP_LEFT, UP_RIGHT, DOWN, DOWN_LEFT, DOWN_RIGHT])

    return valid_directions


def initialize_wave_function(size, patterns):
    """
    Initialize wave function of the size[0]xsize[1] list // receive input as tuple of the size of the input
    Coefficients govern how frequent patterns occur in each tile. At the begining, there is full set
    of patterns available at every possition 
    """

    coefficients = []

    for col in range(size[0]):
        row = []
        for r in range(size[1]):
            row.append(patterns)
        coefficients.append(row)
    return coefficients


def get_possible_patterns_at_position(position, coefficients):
    """
    Return list of possible patterns at position (x, y)
    """
    x, y = position
    possible_patterns = coefficients[x][y]
    return possible_patterns


def get_shannon_entropy(position, coefficients, probability):
    """
    Calcualte the Shannon Entropy of the wavefunction at position (x, y)
    """
    x, y = position
    entropy = 0

    # A cell with one valid pattern has 0 entropy
    if len(coefficients[x][y]) == 1:
        return 0

    for pattern in coefficients[x][y]:
        # recall that probability is a dictionary of probabilities where the key is the corresponding pattern
        entropy -= probability[pattern] * math.log(probability[pattern], 2)

    # Add noise to break ties and near-ties
    entropy -= random.uniform(0, 0.1)
    return entropy


def get_min_entropy_pos(coefficients, probability):
    """
    Return position of tile with the lowest non-zero entropy for non fullly collapsed wavefunctions
    Return None for fully collapsed wavefunction

    """
    minEntropy = None  # since zero is meaningful had to resort to None
    minEntropyPos = None

    # x, y positions don't make sense but could be my brain is being daft
    for x, col in enumerate(coefficients):
        for y, row in enumerate(col):
            entropy = get_shannon_entropy((x, y), coefficients, probability)

            if entropy == 0:
                continue   # to skip the tiles with zero entropy

            if minEntropy is None or entropy < minEntropy:
                minEntropy = entropy
                minEntropyPos = (x, y)
    return minEntropyPos


def is_fully_collapsed(coefficients):
    """
    Check if wave function is fully collapsed, meaning that for each tile available there is only one pattern
    """
    for col in coefficients:
        for entry in col:
            if (len(entry) > 1):
                return False
    return True


def post_collasping(coefficients):
    """
    Create arrays of output pixels extracted from coefficients elements at a moment in time
    Using the fact that each pattern has equal intersection with all of its adjacent patterns. 
    If we get only first pixel from each pattern, we get unique part of each.
    """
    final_pixels = []

    for i in coefficients:
        row = []
        for j in i:

            if isinstance(j, list):  # If the pixel is not yet collapsed
                first_pixels = 0
                for k in j:
                    first_pixels += k.pixels[0][0]
                # average over all of the first tiles in the list of possible tiles
                first_pixel = first_pixels / len(j)

            else:  # if the pixel has been collapsed
                first_pixel = j.pixels[0][0]

            row.append(first_pixel)
        final_pixels.append(row)

    return final_pixels
