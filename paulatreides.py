from initializedata import *
from runnetwork import *
from adjustnetwork import *

from tests import *

from displaydata import *

inputbits = 4

layersize = 16
layernumber = 2

batchsize = 50
iterationlength = 2000

testset = binarytestset(1, inputbits) #dry testrun to find input and outputs

inputsize = len(testset[0][0][0])
outputsize = len(testset[0][1][0])

dataset = initializedata(inputsize, layersize, layernumber, outputsize) 



for a in range(0, iterationlength):
    testset = binarytestset(batchsize, inputbits)

    for test in range(0, batchsize):
        [outputvalue, output, cost, costfunction, dataset] = runnetwork(testset[test][0], dataset, testset[test][1])
        
        if test == 0:
            print(round(cost, 2), (testset[test][0][0]), "=", outputvalue)

    dataset = adjustnetwork(batchsize, dataset)

displaydata(dataset)