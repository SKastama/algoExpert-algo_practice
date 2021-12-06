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


# print(longestPeak([1, 2, 2, -2, -1, 4, 2, 1, 0, -1, 9, 1]))


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
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    pos= 0
    while pos < len(intervals) - 1:
        if intervals[pos][1] >= intervals[pos+1][0]:
            intervals[pos][1]= max(intervals[pos][1], intervals[pos+1][1])
            intervals.pop(pos+1)
        else:
            pos+= 1
    return intervals

# print(mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
# print(mergeOverlappingIntervals([[1, 22], [-20, 30]]))


# Number 10- Uncompleted
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current= self
        while True:
            if current.value > value:
                if current.left is None:
                    current.left= BST(value)
                    break
                else:
                    current= current.left
            else:
                if current.right is None:
                    current.right= BST(value)
                    break
                else:
                    current= current.right
        return self

    def contains(self, value):
        current= self
        while current is not None:
            if current.value > value:
                current= current.left
            elif current.value < value:
                current= current.right
            else:
                return True
        return False

    def remove(self, value):
        current= self
        while current is not None:
            if current.value == value:
                current.pop()
                break
            elif current.value > value:
                current= current.left
            elif current.value < value:
                current= current.right
        # Do not edit the return statement of this method.
        return self


# Number 20.1
def maxSubsetSumNoAdjacent1(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums= []
    maxSums.append(array[0])
    maxSums.append(max(array[0], array[1]))
    i= 2
    while i < len(array):
        currentSum= maxSums[i-2] + array[i]
        if maxSums[i-1] < currentSum:
            maxSums.append(currentSum)
        else:
            maxSums.append(maxSums[i-1])
        i+= 1
    largestSum= max(maxSums)
    return largestSum

# Number 20.2
def maxSubsetSumNoAdjacent2(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    minus1Sum= max(array[0], array[1])
    minus2Sum= array[0]
    i= 2
    while i < len(array):
        currentSum= minus2Sum + array[i]
        minus2Sum= minus1Sum
        if minus1Sum < currentSum:
            minus1Sum= currentSum
        i+= 1
    return minus1Sum

# print(maxSubsetSumNoAdjacent2([7, 10, 12, 7, 9, 14]))


# Number 21
def numberOfWaysToMakeChange(n, denoms):
    ways= [0 for amount in range(n+1)]
    ways[0]= 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]



