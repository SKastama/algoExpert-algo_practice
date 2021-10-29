# # This is the class of the input root. Do not edit it.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def branchSums(root):
# 	sums= []
# 	branchSumsCall(root, 0, sums)
# 	return sums
		
# def branchSumsCall(root, runningSum, sums):
#     if (root == None):
# 		return 
# 	runningSum += root.value
# 	if (root.left == None and root.right == None):
# 		sums.append(runningSum)
# 		return 
	
#     branchSumsCall(root.left, runningSum, sums)
# 	branchSumsCall(root.right, runningSum, sums)

# def nodeDepths(node, depth = 0):
#     if (node == None):
# 	    return 0
#     return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)



# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# # for the depthFirstSearch method.
# # Feel free to add new properties
# # and methods to the class.
# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name

#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self

#     def depthFirstSearch(self, array):
#         array.append(self.name)
#         for i in self.children:
#             i.depthFirstSearch(array)
#         return array

# def minimumWaitingTime(queries):
# 	queries.sort()
# 	sums = 0
# 	for i in range(len(queries)):
# 		sums+= sum(queries[0:i])
# 	return sums

# print(minimumWaitingTime([3, 2, 1, 2, 6]))

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

# print(classPhotos([6, 9, 2, 4, 5], [5, 8, 1, 3, 4]))
print(classPhotos([6], [6]))
print(classPhotos([1, 1, 1, 1, 1, 1, 1, 1], [5, 6, 7, 2, 3, 1, 2, 3]))