class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeQueue = [root] if root else [None]
        maxWidth = -float("inf")
        while any(nodeQueue):
            values = [node.val if node else None for node in nodeQueue]
            if any(map(lambda x: True if x is not None else False, values)):
                leftPtr, rightPtr = 0, len(values) - 1
                while values[leftPtr] is None:
                    leftPtr += 1
                while values[rightPtr] is None:
                    rightPtr -= 1
                width = rightPtr - leftPtr + 1
            else:
                width = 0
            maxWidth = max(maxWidth, width)
            
            nextNodeQueue = []
            for index, node in enumerate(nodeQueue):
                if leftPtr <= index <= rightPtr:
                    nextNodeQueue += [node.left, node.right] if node else [None, None]
            nodeQueue = nextNodeQueue
        
        return maxWidth
        