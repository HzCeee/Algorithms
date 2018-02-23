# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minValue = root.val if root else float('inf')
        
        # return the minimum value larger than minValue in the subtree rooted with node
        def findSecondMinimumValueHelper(node):
            if not node:
                return None
            if node.val > minValue: return node.val
            
            leftFind = findSecondMinimumValueHelper(node.left)
            rightFind = findSecondMinimumValueHelper(node.right)
            
            if leftFind and rightFind:
                return min(leftFind, rightFind)
            elif leftFind:
                return leftFind
            elif rightFind:
                return rightFind
            else:
                return False
        
        res = findSecondMinimumValueHelper(root)
        
        return res if res else -1
            