# Number 7
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	sums= []
	branchSumsCall(root, 0, sums)
	return sums
		
def branchSumsCall(root, runningSum, sums):
    if (root == None):
        return 
    runningSum += root.value
    if (root.left == None and root.right == None):
        sums.append(runningSum)
        return 

    branchSumsCall(root.left, runningSum, sums)
    branchSumsCall(root.right, runningSum, sums)

# Number 8
def nodeDepths(node, depth = 0):
    if (node == None):
        return 0
    return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)


# Number 9
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for i in self.children:
            i.depthFirstSearch(array)
        return array

# Number 10
def minimumWaitingTime(queries):
	queries.sort()
	sums = 0
	for i in range(len(queries)):
		sums+= sum(queries[0:i])
	return sums

# print(minimumWaitingTime([3, 2, 1, 2, 6]))

# Number 11
def classPhotos(redShirtHeights, blueShirtHeights):
    pos= 0
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    if (redShirtHeights[0] > blueShirtHeights[0]):
        backrow= redShirtHeights
        frontrow= blueShirtHeights
    else:
        backrow= blueShirtHeights
        frontrow= redShirtHeights
    while (pos < len(backrow)):
        if (backrow[pos] > frontrow[pos]):
            pos+= 1
        else:
            return False
    return True

# # print(classPhotos([6, 9, 2, 4, 5], [5, 8, 1, 3, 4]))
# print(classPhotos([6], [6]))
# print(classPhotos([1, 1, 1, 1, 1, 1, 1, 1], [5, 6, 7, 2, 3, 1, 2, 3]))

# Number 12
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    sums= 0
    if fastest:
        for i in range(len(redShirtSpeeds)):
            rider1= redShirtSpeeds[i]
            rider2= blueShirtSpeeds[len(blueShirtSpeeds) - 1 - i]
            sums+= max(rider1, rider2)
    if not fastest:
        for i in range(len(redShirtSpeeds)):
            rider1= redShirtSpeeds[i]
            rider2= blueShirtSpeeds[i]
            sums+= max(rider1, rider2)
    return sums

# print(tandemBicycle([1, 7, 8], [2, 5, 6], True))
# print(tandemBicycle([1, 7, 8], [2, 5, 6], False))

# Number 13
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    runner = linkedList
    while runner.next is not None:
        if runner.value == runner.next.value:
            temp= runner.next.next
            runner.next = temp
        else:
            runner= runner.next
    return linkedList

# Number 14
def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)

# print(getNthFib(6))

# Number 15
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multplier = 1):
	pdtSum = 0
	for i in array:
		if type(i) is list:
			pdtSum+= productSum(i, multplier + 1)
		else: 
			pdtSum+= i
	return pdtSum * multplier

# Number 16
import math
def binarySearch(array, target):
	return binarySearchCall(array, target, 0, len(array) - 1)
	
def binarySearchCall(array, target, left, right):
	if left > right:
		return -1
	midpoint= math.floor((left + right)// 2)
	if array[midpoint] == target:
		return midpoint
	elif array[midpoint] < target:
		left= midpoint + 1
		return binarySearchCall(array, target, left, right)
	else:
		right= midpoint - 1
		return binarySearchCall(array, target, left, right)

# Number 17
def findThreeLargestNumbers(array):
    largest= [float('-inf'), float('-inf'), float('-inf')]
    for i in range(len(array)):
        if array[i] > largest[0] and array[i] <= largest[1]:
            largest[0]= array[i]
        elif array[i] > largest[1] and array[i] <= largest[2]:
            largest[0]= largest[1]
            largest[1]= array[i]
        elif array[i] > largest[2]:
            largest[0]= largest[1]
            largest[1]= largest[2]
            largest[2]= array[i]
    return largest
# print(findThreeLargestNumbers([141, -22, 100, 180, 99, 122]))

# Number 18
def bubbleSort(array):
    nums= array
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

# Number 19
def insertionSort(array):
    for i in range(1, len(array)):
        current= array[i]
        j= i-1
        while current < array[j] and j >= 0:
            array[j+1]= array[j]
            j-= 1
        array[j+1]= current
    return array
# print(insertionSort([3, 5, 2, 8]))

# Number 20
def selectionSort(array):
	pos= 0
	while pos < len(array)-1:
		smallPos= pos
		for i in range(pos + 1, len(array)):
			if array[i] < array[smallPos]:
				smallPos= i
		array[pos], array[smallPos] = array[smallPos], array[pos]
		pos+= 1
	return array

# Number 21
import math
def isPalindrome(string):
    halfString= int(math.floor(len(string)/2))
    for i in range(halfString):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True
# print(isPalindrome("abccba"))

# Number 22
alphabet={
		"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i", "10":"j", "11":"k",
		"12":"l", "13":"m", "14":"n", "15":"o", "16":"p", "17":"q", "18":"r", "19":"s", "20":"t", "21":"u",
		"22":"v", "23":"w", "24":"x", "25":"y", "26":"z"
}
def caesarCipherEncryptor(string, key):
	newLetters = []
	newKey = key % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# print(caesarCipherEncryptor("abc", 9))

# Number 23
def runLengthEncoding(string):
    output= []
    count= 0
    for i in range(len(string) - 1):
        print(string[i])
        if string[i] != string[i+1] or count == 9:
            count= str(count)
            output.append(count)
            output.append(string[i])
            count= 0
        count+= 1
    count= str(count)
    output.append(count)
    output.append(string[len(string) - 1])
    return "".join(output)

print(runLengthEncoding("AAAAAAAAAAABBCCCC"))

