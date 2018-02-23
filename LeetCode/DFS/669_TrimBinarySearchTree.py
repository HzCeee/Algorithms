# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # return the root in the subtree of node within the range [L, R]
        def trimBSTHelper(node):
            if not node:
                return None
            leftNode = trimBSTHelper(node.left)
            rightNode = trimBSTHelper(node.right)
            if L <= node.val <= R:
                rootNode = node
                rootNode.left, rootNode.right = leftNode, rightNode
            else:
                if leftNode and rightNode:
                    rootNode = leftNode if leftNode.val <= rightNode.val else rightNode
                    leftChildNode = trimBSTHelper(leftNode)
                    rootNode.left, rootNode.right = leftChildNode, rightNode
                elif leftNode:
                    rootNode = leftNode
                    leftChildNode, rightChildNode = trimBSTHelper(leftNode.left), trimBSTHelper(leftNode.right)
                    rootNode.left, rootNode.right = leftChildNode, rightChildNode
                elif rightNode:
                    rootNode = rightNode
                    leftChildNode, rightChildNode = trimBSTHelper(rightNode.left), trimBSTHelper(rightNode.right)
                    rootNode.left, rootNode.right = leftChildNode, rightChildNode
                else:
                    rootNode = None
            return rootNode
        
        return trimBSTHelper(root)
                