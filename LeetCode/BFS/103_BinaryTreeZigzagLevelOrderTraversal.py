# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = 0
        levelOrderTraversal = []
        
        nodeQueue = [root]
        
        while nodeQueue and root:
            values = [node.val for node in nodeQueue if node]
            
            if depth % 2 == 0:
                levelOrderTraversal.append(values)
            else:
                levelOrderTraversal.append(values[::-1])
            
            nodeQueue = [childNode for node in nodeQueue if node for childNode in [node.left, node.right] if childNode]
            depth += 1
                    
        return levelOrderTraversal