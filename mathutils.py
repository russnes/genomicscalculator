"""Math utilities
"""

def mean(numbers):
    """returns the arithmetic mean of a given list of numbers"""
    return float(sum(numbers)) / max(len(numbers), 1)
