""" Mean of covered positions calculator
"""

from mathutils import mean
from datatypes import Segment, Function

def calculateMeanOfCoveredPositions(segment, function):
    """ Returns the mean of the value of positions in the given function by the 
    ranges in the given segment
    """
    
    if not type(segment) is Segment:
        raise ValueError("segment is not of Segment type: " + str(type(segment)))
    if not type(function) is Function:
        raise ValueError("function is not of Function type: " + str(type(function)))
    
    regions_iterator = iter(segment.regions)
    coordinates = next(regions_iterator)
    numbers_in_range = []
    
    for i in range(0, len(function.positions)):
        current_position_value = function.positions[i]
        
        #this looping could perhaps be done more elegantly
        while coordinates is not None and i > coordinates[1]:
            coordinates = next(regions_iterator, None)
        if coordinates is None:
            break
        
        if i < coordinates[1] and i >= coordinates[0]:
            numbers_in_range.append(current_position_value)
    
    mean_of_numbers_in_range = mean(numbers_in_range)
    return mean_of_numbers_in_range
