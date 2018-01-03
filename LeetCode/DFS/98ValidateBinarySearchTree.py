import sys

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # if not root:
        #     return True
        
        isValidFlag = [True]
        maximumThreshold = sys.maxsize
        minimumThreshold = - sys.maxsize - 1
        def isValid(node, minimumThreshold, maximumThreshold):
            if not node:
                return
            if node.val >= maximumThreshold or node.val <= minimumThreshold:
                isValidFlag[0] = False
                return
            isValid(node.left, minimumThreshold, node.val)
            isValid(node.right, node.val, maximumThreshold)
        
        isValid(root, minimumThreshold, maximumThreshold)
        return isValidFlag[0]