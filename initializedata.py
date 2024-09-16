import numpy as np

weightrandomizationfactor = 1
biasrandomizationfactor = 1

def initializedata(inputsize, neuronsize, layersize, outputsize):

    n2 = []
    inputs1 = np.zeros((1, inputsize), dtype = float)
    n2.append(inputs1)

    for a in range(0, layersize):
        neurons1 = np.zeros((1, neuronsize), dtype = float)
        n2.append(neurons1)

    outputs1 = np.zeros((1, outputsize), dtype = float)
    n2.append(outputs1)

    dn2 = n2.copy()

    b2 = [[0]]
    for a in range(1, len(n2)):
        b1 = (biasrandomizationfactor * np.random.rand(1, len(n2[a][0]))) - (biasrandomizationfactor / 2)
        b2.append(b1)

    db2 = [[0]]
    for a in range(1, len(n2)):
        db1 = np.zeros((1, len(n2[a][0])), dtype = float)
        db2.append(db1)

    w3 = [[[0]]]
    for a in range(1, len(n2)):
        w2 = (weightrandomizationfactor * np.random.rand(len(n2[a][0]), len(n2[a - 1][0]))) - (weightrandomizationfactor / 2)
        w3.append(w2)

    dw3 = [[[0]]]
    for a in range(1, len(n2)):
        dw2 = np.zeros((len(n2[a][0]), len(n2[a - 1][0])), dtype = float)
        dw3.append(dw2)

    return(n2, b2, w3, dn2, db2, dw3)