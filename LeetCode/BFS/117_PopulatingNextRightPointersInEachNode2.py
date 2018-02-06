# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        nodeQueue = [root]
        while nodeQueue:
            prevNode = None
            for node in nodeQueue:
                if not prevNode:
                    prevNode = node
                    continue
                prevNode.next = node
                prevNode = node
                
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]