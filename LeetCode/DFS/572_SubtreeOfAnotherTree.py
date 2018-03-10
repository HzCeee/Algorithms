class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSubtreeHelper(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                if isSubtreeHelper(node1.left, node2.left) and isSubtreeHelper(node1.right, node2.right):
                    return True
        
        nodeStack = [s] if s else []
        while nodeStack:
            node = nodeStack.pop()
            if not node:
                continue
                
            if node.val != t.val:
                nodeStack.append(node.left)
                nodeStack.append(node.right)
            else:
                if isSubtreeHelper(node, t): 
                    return True
                else:
                    nodeStack.append(node.left)
                    nodeStack.append(node.right)
        
        return False