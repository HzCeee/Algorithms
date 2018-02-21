# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root: None}
        nodeStack = [root] if root else []
        while nodeStack and p not in parent or q not in parent:
            node = nodeStack.pop()
            if node.left: 
                parent[node.left] = node
                nodeStack.append(node.left)
            if node.right:
                parent[node.right] = node
                nodeStack.append(node.right)
        ancestor = []
        while p:
            ancestor.append(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        
        return q