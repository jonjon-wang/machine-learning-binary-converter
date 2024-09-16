def getmax(array):
    
    max = 0
    for a in range(1, len(array)):
        if array[a] > array[max]:
            max = a
    
    return max