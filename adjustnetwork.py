import numpy as np

def adjustnetwork(batchsize, dataset):

    [n2, b2, w3, dn2, db2, dw3] = dataset

    for layer in range(1, len(n2)):
        b2[layer] = b2[layer] - (db2[layer] / batchsize)
        w3[layer] = w3[layer] - (dw3[layer] / batchsize)

    db2 = [[0]]
    dw3 = [[[0]]]

    for layer in range(1, len(n2)):
        db1 = np.zeros((1, len(n2[layer][0])), dtype = float)
        db2.append(db1)

        dw2 = np.zeros((len(n2[layer][0]), len(n2[layer - 1][0])), dtype = float)
        dw3.append(dw2)

    dataset = [n2, b2, w3, dn2, db2, dw3]

    return dataset