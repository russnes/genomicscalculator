""" Data types for genomic information representation
"""

import re

class Segment(object):
    """Wrapper class for SEGMENT files which contains a list of 
    coordinates (end exclusive) representing regions
    """
    
    def __init__(self, segment_file):
        self.regions = self.parseSegmentFile(segment_file)
    
    def parseSegmentFile(self, segment_file):
        """parses a SEGMENT file to an array of coordinates"""
        regions = list()
        for line in segment_file:
            coordinatesString = re.split(r'\t+', line.rstrip('\n\t'))
            if len(coordinatesString) != 2:
                raise ValueError("Invalid input structure. Each row should contain two tab separated numbers!")
            start = int(coordinatesString[0])
            end = int(coordinatesString[1])
            coordinates = [start, end]
            regions.append(coordinates)
        self.verifyRegions(regions)
        return regions
    
    def verifyRegions(self, regions):
        """ verifies that no regions within the same segment overlaps
        assumes that all coordinates are sorted
        """
        
        i = 0
        numregions = len(regions)
        for coordinates in regions:
            if(i<numregions-1):
                nextcoordinates = regions[i+1]
                if(nextcoordinates[0] < coordinates[1]):
                    raise ValueError("Invalid input structure. Coordinates overlap within segment!")
            i += 1
        return

class Function(object):
    """Wrapper class for FUNCTION files containing list of genome 
    positions
    """
    
    def __init__(self, function_file, genome_length):
        self.positions = self.parseFunctionFile(function_file, genome_length)
    
    def parseFunctionFile(self, function_file, genome_length):
        positions = []
        for line in function_file:
            #TODO check if value has decimals so that it is in the valid float format
            position = float(line)
            positions.append(position)
        self.verifyPositions(positions, genome_length)
        return positions
    
    def verifyPositions(self, positions, genome_length):
        if not genome_length == len(positions):
            raise ValueError('Genome length (' + str(genome_length) + ') is not the same as number of values in '
                                                                      'input file (' + str(len(positions)) + ')')
