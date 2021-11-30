# Number 1
def threeNumberSum(array, targetSum):
    array.sort()
    output= []
    for i in range(len(array) - 1):
        left= i+1
        right = len(array) - 1
        while left < right:
            tempSum= array[i] + array[left] + array[right]
            if tempSum == targetSum:
                temp= [array[i], array[left], array[right]]
                output.append(temp)
                right-= 1
                left+= 1
            if tempSum > targetSum:
                right-= 1
            if tempSum < targetSum:
                left+= 1
    return output

# print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))


# Number 2- Uncompleted
def smallestDifference(arrayOne, arrayTwo):
    output= float('inf')
    arrayOne.sort()
    arrayTwo.sort()
    pointerOne= 0
    pointerTwo= 0
    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        absDif= abs(arrayOne[pointerOne] - arrayTwo[pointerTwo])
        if absDif == 0:
            output= [arrayOne[pointerOne], arrayTwo[pointerTwo]]
            break
        elif absDif < output:
            output= [arrayOne[pointerOne], arrayTwo[pointerTwo]]
        if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
            pointerOne+= 1
        else:
            pointerTwo+= 1
    return output

# print(smallestDifference([1, 3, 6, 9], [8, -4, 11]))


# Number 3
def moveElementToEnd(array, toMove):
    pointOne= 0
    pointTwo= len(array) - 1
    while pointOne < pointTwo:
        if array[pointTwo] == toMove:
            pointTwo-= 1
            continue
        if array[pointOne] == toMove:
            temp= array[pointOne]
            array[pointOne]= array[pointTwo]
            array[pointTwo]= temp
            pointTwo-= 1
        pointOne+= 1
    return array

# print(moveElementToEnd([2, 4, 2, 5, 6, 2, 2], 2))


# Number 4
def isMonotonic(array):
    # if len(array) <= 1:
    #     return True
    # for i in range(1, len(array)):
    #     if array[i] == array[i - 1]:
    #         continue
    #     elif array[i] > array[i - 1]:
    #         trend= "Increase"
    #         break
    #     elif array[i] < array[i - 1]:
    #         trend= "Decrease"
    #         break
    # for i in range(1, len(array)):
    #     if array[i] == array[i - 1]:
    #         continue
    #     if array[i] > array[i - 1] and trend != "Increase":
    #         return False
    #     if array[i] < array[i - 1] and trend != "Decrease":
    #         return False
    # return True 

    # Smarter way
    NonDecreasing= True
    NonIncreasing= True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            NonDecreasing= False
        if array[i] > array[i - 1]:
            NonIncreasing= False
    return NonDecreasing or NonIncreasing

# print(isMonotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]))


# Number 5
def spiralTraverse(array):
    output= []
    sR= 0
    sC= 0
    eR= len(array) - 1
    eC= len(array[0]) - 1
	
    while sR <= eR and sC <= eC:
        for col in range(sC, eC + 1):
            output.append(array[sR][col])

        for row in range(sR + 1, eR + 1):
            output.append(array[row][eC])

        for col in reversed(range(sC, eC)):
            if sR == eR:
                break
            output.append(array[eR][col])

        for row in reversed(range(sR + 1, eR)):
            if sC == eC:
                break
            output.append(array[row][sC])
        sR+= 1
        sC+= 1
        eR-= 1
        eC-= 1
    return output

data= [
    [1,  2,  3,  4],
    [10, 11, 12, 5],
    [9,  8,  7,  6],
]
data2= [
    [1,  2,  3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9,  8,  7],
]

# print(spiralTraverse(data2))


# Number 6
# def longestPeak(array):
    # First find all peaks
#     maxPeak= 0
#     i = 0
#     while i < len(array):
#         if array[i] > array[i-1] and array[i] > array[i+1]:
            
    

#     # Then find longest peak

# print(longestPeak([1, 2, 3, 0, -1, 4, 2, 9, 1]))


# Number 7
def arrayOfProducts(array):
    output= []
    for i in range(len(array)):
        product= 1
        for j in range(len(array)):
            if j == i:
                continue
            product*= array[j]
        output.append(product)
    return output
print(arrayOfProducts([3, 1, 2]))
