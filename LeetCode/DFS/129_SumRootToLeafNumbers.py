# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curNum = 0
        pathSumList = []
        def sumNumbersHelper(node, curNum):
            if not node: return
            if not node.left and not node.right:
                pathSumList.append(curNum * 10 + node.val)
            sumNumbersHelper(node.left, curNum * 10 + node.val)
            sumNumbersHelper(node.right, curNum * 10 + node.val)
        
        sumNumbersHelper(root, curNum)
        
        return sum(pathSumList)