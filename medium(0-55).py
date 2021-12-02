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


# Number 2
def smallestDifference(arrayOne, arrayTwo):
    output= []
    absVal= float('inf')
    arrayOne.sort()
    arrayTwo.sort()
    point1= 0
    point2= 0
    while point1 < len(arrayOne) and point2 < len(arrayTwo):
        if arrayOne[point1] == arrayTwo[point2]:
            output= [arrayOne[point1], arrayTwo[point2]]
            break
        absValTemp= abs(arrayOne[point1]- arrayTwo[point2])
        if absValTemp < absVal:
            absVal= absValTemp
            output= [arrayOne[point1], arrayTwo[point2]]
        if arrayOne[point1] < arrayTwo[point2]:
            point1+= 1
            continue
        elif arrayOne[point1] > arrayTwo[point2]:
            point2+= 1
    return output

# print(smallestDifference([1, -3, 6, 7], [8, -4, 11]))


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
def longestPeak(array):
    # longestPeak= 0
    # count= 0
    # for i in range(1, len(array) - 1):
    #     if array[i] > array[i-1] and array[i] > array[i+1]:
    #         count+= 1
    #         idxL= i
    #         while idxL > 0:
    #             if array[idxL] > array[idxL - 1]:
    #                 count+= 1
    #                 idxL-= 1
    #             else:
    #                 break
    #         idxR= i
    #         while idxR < len(array) - 1:
    #             if array[idxR] > array[idxR + 1]:
    #                 count+= 1
    #                 idxR+= 1
    #             else:
    #                 break
    #     if count > longestPeak:
    #         longestPeak= count
    #     else:
    #         count= 0
    
    longestPeak= 0
    idx= 1
    while idx < len(array) - 1:
        aPeak= array[idx] > array[idx-1] and array[idx] > array[idx+1]
        if not aPeak:
            idx+= 1
            continue
            
        idxL= idx
        while idxL >= 0 and array[idxL] > array[idxL - 1]:
            idxL-= 1
        idxR= idx
        while idxR < len(array) - 1 and array[idxR] > array[idxR + 1]:
            idxR+= 1
        currentPeak= idxR - idxL + 1
        longestPeak= max(longestPeak, currentPeak)
        idx= idxR

    return longestPeak


print(longestPeak([1, 2, 2, -2, -1, 4, 2, 1, 0, -1, 9, 1]))


# Number 7
# O(n^2) time complexity solution
def arrayOfProducts1(array):
    output= []
    for i in range(len(array)):
        product= 1
        for j in range(len(array)):
            if j == i:
                continue
            product*= array[j]
        output.append(product)
    return output

# print(arrayOfProducts1([3, 1, 2]))


# Number 8
def firstDuplicateValue(array):
    numberCount= set()
    for i in range(len(array)):
        if array[i] in numberCount:
            return array[i]
        numberCount.add(array[i])
    return -1

# print(firstDuplicateValue([7, 4, 2, 7, 5, 3, 2]))


# Number 9
# def mergeOverlappingIntervals(intervals):
    



