import numpy as np
from sigmoid import *
from getmax import *

def runnetwork(input, dataset, targetoutput):

    [n2, b2, w3, dn2, db2, dw3] = dataset

    n2[0] = input

    for a in range(1, len(n2)):
        n2[a] = np.matmul(w3[a], (n2[a - 1].T)).T
        n2[a] = np.add(n2[a], b2[a])
        n2[a] = sigmoid(n2[a])

    output = n2[len(n2) - 1]

    outputvalue = getmax(output[0])

    costfunction = output - targetoutput

    cost = 0
    for a in range(0, len(costfunction[0])):
        cost = cost +  costfunction[0][a] ** 2

    for layer in range(len(n2) - 1, 0, -1):
        if layer == len(n2) - 1:
            dn2[layer] = 2 * costfunction
        else:
            dn2[layer] = (np.matmul(w3[layer + 1].T, ((n2[layer + 1] * (1 - n2[layer + 1])) * dn2[layer + 1]).T)).T

        db2[layer] =  db2[layer] + (n2[layer] * (1 - n2[layer])) * dn2[layer]

        dw3[layer] = dw3[layer] + np.matmul(((n2[layer] * (1 - n2[layer])) * dn2[layer]).T, n2[layer - 1]) #check if this should be n2[layer-1] or not and try to sort through that

    dataset = [n2, b2, w3, dn2, db2, dw3]

    return (outputvalue, output, cost, costfunction, dataset)



def dryrunnetwork(input, dataset):

    [n2, b2, w3, dn2, db2, dw3] = dataset

    n2[0] = input

    for a in range(1, len(n2)):
        n2[a] = np.matmul(w3[a], (n2[a - 1].T)).T
        n2[a] = np.add(n2[a], b2[a])
        n2[a] = sigmoid(n2[a])

    output = n2[len(n2) - 1]

    outputvalue = getmax(output[0])

    return outputvalue