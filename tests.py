import random
import numpy as np

def addingtestset(length, bits):

    result = []
    for a in range(0, length):
        A = []
        B = []
        for a in range(0, int(bits/2)):
            A.append(random.randint(0, 1))
            B.append(random.randint(0, 1))

        Avalue = 0
        Bvalue = 0

        for a in range(0, len(A)):
            Avalue = Avalue + A[a] * (2 ** a)

        for a in range(0, len(B)):
            Bvalue = Bvalue + B[a] * (2 ** a)

        sum = Avalue + Bvalue

        output = []
        for a in range(0, (2 ** (len(A) + 1)) - 1):
            if a == sum:
                output.append(1)
            else:
                output.append(0)

        input = A + B

        testset = [np.array([input]), np.array([output])]
        result.append(testset)
    return result



def binarytestset(length, bits):

    testset = []
    for a in range(0, length):
        input = []
        for a in range(0, bits):
            input.append(random.randint(0, 1))

        value = 0
        for a in range(0, len(input)):
            value = value + input[a] * (2 ** a)

        output = []
        for a in range(0, (2 ** (bits))):
            if a == value:
                output.append(1)
            else:
                output.append(0)

        testset.append([np.flip(np.array([input])), np.array([output])])
    return testset