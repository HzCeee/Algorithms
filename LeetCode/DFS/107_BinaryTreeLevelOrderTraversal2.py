# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class DFSRecursionSolution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = 0
        levelOrderTraversal = []
        
        def levelOrderBottomHelper(node, depth):
            if not node:
                return
            
            if depth + 1 > len(levelOrderTraversal):
                levelOrderTraversal.append([])
                
            levelOrderTraversal[depth].append(node.val)
            
            levelOrderBottomHelper(node.left, depth+1)
            levelOrderBottomHelper(node.right, depth+1)
        
        levelOrderBottomHelper(root, depth)
        
        return levelOrderTraversal[::-1]


class DFSStackSolution:
    def levelOrderBottom(self, root):
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
                
        return levelOrderTraversal[::-1]