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
        
        nodeStack = [[root, depth]]
        
        while nodeStack:
            node, depth = nodeStack.pop()
            if node:
                if depth + 1 > len(levelOrderTraversal):
                    levelOrderTraversal.append([])
                levelOrderTraversal[depth].append(node.val)
                
                nodeStack.append([node.right, depth+1])
                nodeStack.append([node.left, depth+1])
        
        return levelOrderTraversal