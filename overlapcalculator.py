""" Segment overlap calculator
"""

from datatypes import Segment

def __getNumberOfOverlaps(coordinates_x, coordinates_y):
    """ Returns the number of overlapping points for two coordinates known to overlap
    """
    
    start_diff = coordinates_y[0] - coordinates_x[0]
    end_diff = coordinates_y[1] - coordinates_x[1]
    
    if(start_diff < 0):
        range_start = coordinates_x[0]
    else:
        range_start = coordinates_y[0]
    if(end_diff >= 0):
        range_end = coordinates_x[1]
    else:
        range_end = coordinates_y[1]

    overlaps = abs(range_end-range_start)
    return overlaps

def __checkOverlap(range_x, range_y):
    """ Returns a positive number if there is an overlap, and a negative if there is not
    The absolute of the returned number indicates which range is ending before the other as follows:
    1 if range_x ends before range_y
    2 if range_y ends before range_x
    """
    start_x = range_x[0]
    end_x = range_x[1]
    start_y = range_y[0]
    end_y = range_y[1]
    if(start_x < end_y):
        if(end_x-1 >= start_y):
            # there is an overlap with this range
            
            #After determining the overlap for the current pair of coordinates, the range that is ending
            # before the other indicates which segment to increment
            if end_y > end_x:
                return 1
            else:
                return 2
        else:
            # this x coordinate starts and stops before the current y coordinate begins
            # continue to the next x coordinate
            return -1
    else:
        # the current X range begins after the current Y has finished. Continue to the next Y
        return -2

def calculateOverlap(segment_x, segment_y):
    """ Returns the overlap in number of positions between the regions of two Segments
    """
    
    if not type(segment_x) is Segment:
        raise TypeError("segment_x is not a Segment object: " + str(type(segment_x)))
    if not type(segment_y) is Segment:
        raise TypeError("segment_y is not a Segment object: " + str(type(segment_y)))
    
    # as the coordinates may not overlap within one file, we can make one assumption:
    # the next range will always begin after the current ends
    xi = 0
    yi = 0
    total_overlap = 0
    # loops through both segments and checks for overlaps
    while xi < len(segment_x.regions) and yi < len(segment_y.regions):
        range_x = segment_x.regions[xi]
        range_y = segment_y.regions[yi]
        
        overlap_result = __checkOverlap(range_x, range_y)
        if overlap_result > 0:
            range_overlap = __getNumberOfOverlaps(range_x, range_y)
            total_overlap += range_overlap
        
        which_segment_to_increment = abs(overlap_result)
        if which_segment_to_increment == 1:
            xi += 1
        elif which_segment_to_increment == 2:
            yi += 1
    
    return total_overlap
