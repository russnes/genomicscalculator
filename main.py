import argparse
import os.path
import overlapcalculator
import pearsoncorrelationcoefficientcalculator
import meanofcoveredpositionscalculator
from datatypes import Segment, Function

def parseInputFile(inputFile):
    """ Parses content of input file to appropriate wrapper class
    """
    
    genome_length = 10000000 #TODO should this be defined with a static maybe or something? Or would it be inside the file header for some formats?
    extension = os.path.splitext(inputFile.name)[1]
    if extension == '.s':
        return Segment(inputFile)
    elif extension == '.f':
        return Function(inputFile, genome_length)
    else:
        raise ValueError('Invalid file format of ' + inputFile.name)

def evaluateInputs(parsed_file_1, parsed_file_2):
    """ Performs the appropriate calculations based on the types of inputs
    """
    functions = []
    segments = []
    if type(parsed_file_1) is Segment:
        segments.append(parsed_file_1)
    elif type(parsed_file_1) is Function:
        functions.append(parsed_file_1)
    else:
        raise ValueError("Parsed file 1 is not of valid type. It is type: " + str(type(parsed_file_1)))

    if type(parsed_file_2) is Segment:
        segments.append(parsed_file_2)
    elif type(parsed_file_2) is Function:
        functions.append(parsed_file_2)
    else:
        raise ValueError("Parsed file 2 is not of valid type. It is type: " + str(type(parsed_file_2)))

    if len(segments) == 2:
        overlap = overlapcalculator.calculateOverlap(segments[0], segments[1])
        print("Overlap: " + str(overlap))
        
    elif len(functions) == 2:
        r = pearsoncorrelationcoefficientcalculator.calculatePearsonCorrelationCoefficient(functions[0], functions[1])
        print("r is " + str(r))
    else:
        mean_of_covered_positions = meanofcoveredpositionscalculator.calculateMeanOfCoveredPositions(segments[0], functions[0])
        print("Mean of covered positions: " + str(mean_of_covered_positions))

arg_parser = argparse.ArgumentParser(description='Genomic problem solver')
arg_parser.add_argument('file1', metavar='file1', type=argparse.FileType('r'),
                    help='file of either .s (SEGMENT) or .f (FUNCTION) format')
arg_parser.add_argument('file2', metavar='file2', type=argparse.FileType('r'),
                    help='file of either .s (SEGMENT) or .f (FUNCTION) format')

args = arg_parser.parse_args()
file1 = args.file1
file2 = args.file2

parsed_file_1 = parseInputFile(file1)
file1.close()
parsed_file_2 = parseInputFile(file2)
file2.close()

evaluateInputs(parsed_file_1, parsed_file_2)
