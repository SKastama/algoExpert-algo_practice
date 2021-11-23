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

print(smallestDifference([1, 3, 6, 9, 10], [16, 8, -4, 19]))



