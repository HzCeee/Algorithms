# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # return the merge tree given two roots
        def mergeTreesHelper(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            
            node1.val += node2.val
            
            node1.left = mergeTreesHelper(node1.left, node2.left)
            node1.right = mergeTreesHelper(node1.right, node2.right)
            return node1
        
        return mergeTreesHelper(t1, t2)