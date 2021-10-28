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

