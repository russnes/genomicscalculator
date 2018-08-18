""" Pearson Correlation Coefficient calculator
"""

from math import sqrt
from datatypes import Function
from mathutils import mean

def __sumPositionsMinusMeanMultiplied(positionsX, meanX, positionsY, meanY):
    if len(positionsX) != len(positionsX):
        raise ValueError("Position lists are not of equal length! " + str(len(positionsX)) + ":" + str(len(positionsX)))
    sum = 0
    for i in range(0, len(positionsX)):
        x = positionsX[i]
        x_i_minus_x_mean = x - meanX

        y = positionsY[i]
        y_i_minus_y_mean = y - meanY

        sum += (x_i_minus_x_mean * y_i_minus_y_mean)
    return sum

def __sumPositionsMinusMeanSquared(positions, mean):
    """ Returns the square of the sum of each number in positions minus mean 
    sum(positions[i]-mean)) to the power of two
    """
    sum_value = 0
    for position in positions:
        positionMinusMean = position - mean
        sum_value += pow(positionMinusMean, 2)
    return sum_value

def calculatePearsonCorrelationCoefficient(function1, function2):
    """ Returns the sample Pearson correlation coefficient of the two number lists
    """
    if not type(function1) is Function:
        raise ValueError("function1 is not of Function type: " + str(type(function1)))
    if not type(function2) is Function:
        raise ValueError("function2 is not of Function type: " + str(type(function2)))
    
    positions_x = function1.positions
    positions_y = function2.positions
    mean_x = mean(positions_x)
    mean_y = mean(positions_y)
    
    #this could perhaps have been named in a better way, but now tries to translate the formula to english
    sqrt_sum_positions_minus_mean_squared_x = sqrt(__sumPositionsMinusMeanSquared(positions_x, mean_x))
    sqrt_sum_positions_minus_mean_squared_y = sqrt(__sumPositionsMinusMeanSquared(positions_y, mean_y))
    multipliedSquareRoots = sqrt_sum_positions_minus_mean_squared_x * sqrt_sum_positions_minus_mean_squared_y
    r = __sumPositionsMinusMeanMultiplied(positions_x, mean_x, positions_y, mean_y) / multipliedSquareRoots
    return r
