import math

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
    longestPeak= 0
    count= 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            count+= 1
            idxL= i
            while idxL > 0:
                if array[idxL] > array[idxL - 1]:
                    count+= 1
                    idxL-= 1
                else:
                    break
            idxR= i
            while idxR < len(array) - 1:
                if array[idxR] > array[idxR + 1]:
                    count+= 1
                    idxR+= 1
                else:
                    break
        if count > longestPeak:
            longestPeak= count
        else:
            count= 0
    
    # longestPeak= 0
    # idx= 1
    # while idx < len(array) - 1:
    #     aPeak= array[idx] > array[idx-1] and array[idx] > array[idx+1]
    #     if not aPeak:
    #         idx+= 1
    #         continue
            
    #     idxL= idx
    #     while idxL >= 0 and array[idxL] > array[idxL - 1]:
    #         idxL-= 1
    #     idxR= idx
    #     while idxR < len(array) - 1 and array[idxR] > array[idxR + 1]:
    #         idxR+= 1
    #     currentPeak= idxR - idxL + 1
    #     longestPeak= max(longestPeak, currentPeak)
    #     idx= idxR

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
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
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
                current= current.left
            else:
                if current.right is None:
                    current.right= BST(value)
                    break
                current= current.right
        return self

    def contains(self, value):
        current= self
        while current is not None:
            if current.value == value:
                return True
            elif current.value > value:
                current= current.left
            elif current.value < value:
                current= current.right
        return False
            

    def remove(self, value, parent=None):
        current= self
        while current is not None:
            if current.value > value:
                parent= current
                current= current.left
            elif current.value < value:
                parent= current
                current= current.right
            else:
                if current.right is not None and current.left is not None:
                    runner= current
                    runner= runner.right
                    while runner is not None:
                        runner= runner.left
                    current.value= runner
                    current.right.remove(current.value, current)
                elif current.left is not None:
                    current.value= current.left.value
                    current.left.remove(current.value, current)
                elif current.right is not None:
                    current.value= current.right.value
                    current.right.remove(current.value, current)
                break
        return self


# Number 11
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, minimum= float('-inf'), maximum= float('inf')):
    if tree is None:
        return True
    if tree.value < minimum or tree.value >= maximum:
        return False
    return validateBst(tree.left, minimum, tree.value) and validateBst(tree.right, tree.value, maximum)


# Number 12
def inOrderTraverse(tree, array=[]):
    if (tree is None):
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    return inOrderTraverse(tree.right, array)

def preOrderTraverse(tree, array=[]):
    if (tree is None):
        return array
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    return preOrderTraverse(tree.right, array)

def postOrderTraverse(tree, array=[]):
    if (tree is None):
        return array
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array


# Number 13
def minHeightBst(array):
    midpoint= math.floor(array.length/2)

    while True:
        # insert(array[midpoint])
        pass


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


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


# Number 13
def minHeightBst(array):
    return callMinHeightBst(array, 0, len(array)-1)
	
def callMinHeightBst(array, start, end):
	if start > end:
		return
	middle= (end+start)//2
	tree= BST(array[middle])
	tree.left= callMinHeightBst(array, start, middle-1)
	tree.right= callMinHeightBst(array, middle+1, end)
	return tree
	
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# Number 14
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
	array= []
	callFindKth(tree, k, array)
	return array[len(array)-k]

def callFindKth(tree, k, array):
	if tree is None:
		return
	callFindKth(tree.left, k, array)
	array.append(tree.value)
	callFindKth(tree.right, k, array)
	return array


# Number 25
def kadanesAlgorithm(array):
    maxEndHere= array[0]
    maxSoFar= array[0]
    for i in range(1, len(array)):
        maxEndHere+= array[i]
        maxEndHere= max(maxEndHere, array[i])
        maxSoFar= max(maxSoFar, maxEndHere)
    return maxSoFar

# print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))


# Number 26
def hasSingleCycle(array):
    idxsSeen= set()
    i= 0
    while True:
        newIdx= (i + array[i])%(len(array))
        if newIdx not in idxsSeen:
            idxsSeen.add(newIdx)
        else:
            return False
        if len(idxsSeen) == len(array):
            break
        i= newIdx
    return True

# print(hasSingleCycle([1, 2]))


# Number 50
def longest_palindromic_substring(string):
    indexes= [0, 0]
    for idx in range(len(string)):
        odd= call_longest_palidrome(idx - 1, idx + 1, string)
        even= call_longest_palidrome(idx, idx + 1, string)
        current_longest= max(odd, even, key= lambda x: x[1] - x[0])
        example= max(odd[1] - odd[0], even[1] - even[0])
        print(current_longest)
        indexes= max(indexes, current_longest, key= lambda x: x[1] - x[0])
    return string[indexes[0]:indexes[1]]


def call_longest_palidrome(start, end, string):
    while start >= 0 and end < len(string):
        if string[start] != string[end]:
            break
        start-= 1
        end+= 1
    return [start + 1, end]

# print(longest_palindromic_substring('abaxyzzyxf'))


def group_anagrams(words):
    hashTable= {}
    output= []
    for i in range(len(words)):
        sortedWord= ''.join(sorted(words[i]))
        if sortedWord in hashTable:
            hashTable[sortedWord].append(words[i])
        else:
            hashTable[sortedWord]= [words[i]]
    for val in hashTable.values():
        output.append(val)
    return output

# print(group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))

def reverseWordsInString(string):
    output= []
    output2= []
    startIdx= 0
    for i in range(len(string)):
        if i + 1 == len(string):
            output.append(string[startIdx:len(string)])
        elif string[i] == ' ':
            output.append(string[startIdx:i])
            startIdx= i + 1
    for i in range(len(output)-1, -1, -1):
        output2.append(output[i])
    return ' '.join(output2)

# print(reverseWordsInString("AlgoExpert is the best!"))


def patternMatcher(pattern, string):
    '''Recieves 2 strings as an input, where it returns substrings within inputed string that represent x and y'''
    # 	Initlaize output array
    outputArr= []
    # 	Initilize x and y variables
    x= ''
    y= ''
    current= ''
    for i in range(len(string)):		
        current+= string[i]
        amount_seen= string.count(current)
        variable_not_found= x if x == '' or len(x) <= amount_seen else y
        if amount_seen == pattern.count(variable_not_found):
            variable_not_found= current
            current= ''
    return [x, y]

pattern1= "xxyxxy"
string1= "gogopowerrangergogopowerranger"


# print(patternMatcher(pattern1, string1))

# Find succeser question
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
        return leftChild(node.right)
    return rightParent(node)

def leftChild(node):
	current= node
	while current.left is not None:
		current= current.left
	return current

def rightParent(node):
	current= node
	while current.parent is not None and current.parent.right == current:
		current= current.parent
	return current.parent






def question1(string1, string2):
    char2= set(string2)
    output= ''
    for i in range(len(string1)):
        if string1[i] not in char2:
            output+= string1[i]
    return output

# print(question1('Sarah', 'rh'))

def question2(string):
    charTable= {}
    order= []
    for i in range(len(string)):
        if string[i] not in charTable:
            charTable[string[i]]= 0
            order.append(string[i])
        charTable[string[i]]+= 1
    for i in range(len(order)):
        if charTable[order[i]] == 1:
            return order[i]
    return None

# print(question2('aabbcgg'))

def question3(string):
    longest= 0
    current= ''
    i= 0
    j= i
    while i < len(string):
        if j >= len(string):
            i+= 1
            j= i
        elif string[j] in current:
            longest= max(longest, len(current))
            current= ''
            i+=1
            j=i
        else:
            current+= string[j]
            j+= 1
    return longest

# print(question3("Sarah"))

def taskAssignment(k, tasks):
    output= []
    newArray= []
    for i in range(len(tasks)):
        newArray.append([tasks[i], i])
    newArray.sort()
    for i in range(len(newArray)//2):
        output.append([newArray[i][1], newArray[len(newArray) - 1 - i][1]])
    return output



# Number 27 in progress
# def riverSizes(matrix):
#     riverLen= []
#     riverIdxs= [[False for value in row] for row in matrix]
#     count= 0
#     nodeRow= 0
#     nodeCol= 0
#     i= 0
#     j= 0
#     while nodeRow < len(matrix):
#         if riverIdxs[i][j] == False and matrix[i][j] == 1:
#             riverIdxs[i][j]= True
#             count+= 1
#             if i+1 < len(matrix) and matrix[i+1][j] == 1 and riverIdxs[i+1][j] == False:
#                 i+= 1
#             elif i-1 >= 0 and matrix[i-1][j] == 1 and riverIdxs[i-1][j] == False:
#                 i-= 1
#             elif j+1 < len(matrix[i]) and matrix[i][j+1] == 1 and riverIdxs[i][j+1] == False:
#                 j+= 1
#             elif j-1 >= 0 and matrix[i][j-1] == 1 and riverIdxs[i][j-1] == False:
#                 j-= 1
#             else:
#                 riverLen.append(count)
#                 count= 0
#                 if j+1 < len(matrix[i]):
#                     nodeCol+=1
#                     j= nodeCol
#                     continue
#                 elif j+1 == len(matrix[i]) and i+1 < len(matrix):
#                     nodeRow+= 1
#                     i= nodeRow
#                     nodeCol= 0
#                     j= nodeCol
#                     continue
#                 elif i+1 == len(matrix):
#                     break
#         if riverIdxs[i][j] == False and matrix[i][j] == 0:
#             riverIdxs[i][j]= True
#         if j+1 < len(matrix[i]):
#             nodeCol+=1
#             j+= 1
#         elif j+1 == len(matrix[i]) and i+1 < len(matrix):
#             nodeRow+= 1
#             i+= 1
#             nodeCol= 0
#             j= 0
#         elif i+1 == len(matrix):
#             break
#     return riverLen

matrix1= [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
# print(riverSizes(matrix1))



# riverLen= []
#     riverIdxs= [[False for value in row] for row in matrix]
#     row= 0
#     i= 0
#     j= 0
#     count= 0
#     while row < len(matrix):
#         i= row
#         while j < len(matrix[i]):
#             if matrix[i][j] == 1 and riverIdxs[i][j] == False:
#                 riverIdxs[i][j] == True
#                 count+= 1
#                 if matrix[i+1][j] == 1 and matrix[i+1][j] is not None:
#                     i+= 1
#                     continue
#                 elif matrix[i-1][j] == 1 and matrix[i-1][j] is not None:
#                     i-= 1
#                     continue
#                 elif matrix[i][j+1] == 1 and matrix[i][j+1] is not None:
#                     j+= 1
#                     continue
#                 elif matrix[i][j-1] == 1 and matrix[i][j-1] is not None:
#                     j-= 1
#                     continue
#                 else:
#                     riverLen.append(count)
#                     count= 0
#             else:
#                 j+= 1
#         row+= 1
#     return riverLen