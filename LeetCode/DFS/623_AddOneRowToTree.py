class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        nodeStack = [(root, 1)] if root else []
        
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left, newRoot.right = root, None
            return newRoot
        
        while nodeStack:
            node, depth = nodeStack.pop()
            if not node:
                continue
            if depth + 1 == d:
                leftChild, rightChild = node.left, node.right
                node.left, node.right = TreeNode(v), TreeNode(v)
                node.left.left, node.right.right = leftChild, rightChild
                continue
            nodeStack.append((node.left, depth+1))
            nodeStack.append((node.right, depth+1))
        
        return root
        
            