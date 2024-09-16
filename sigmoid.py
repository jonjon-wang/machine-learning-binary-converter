import numpy

def sigmoid(array):
    
    return 1 / (1 + numpy.exp(-array))