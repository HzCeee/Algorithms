# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = 0
        levelOrderTraversal = []
        
        nodeQueue = [[root, depth]]
        
        while nodeQueue:
            node, depth = nodeQueue.pop()
            if node:
                if depth + 1 > len(levelOrderTraversal):
                    levelOrderTraversal.append([])
                levelOrderTraversal[depth].append(node.val)
                
                nodeQueue.append([node.right, depth+1])
                nodeQueue.append([node.left, depth+1])
        
        return levelOrderTraversal