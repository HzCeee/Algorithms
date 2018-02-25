# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serializedData = ""
        nodeQueue = [root] if root else []
        while nodeQueue:
            for node in nodeQueue:
                if node:
                    serializedData += str(node.val) + ' '
                else:
                    serializedData += 'null' + ' '
            nodeQueue = [childNode for node in nodeQueue if node for childNode in [node.left, node.right]]
        return serializedData[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeValue = data.split(' ')
        rootValue = nodeValue.pop(0)
        root = TreeNode(int(rootValue)) if rootValue else None
        nodeQueue = [root] if root else []
        while nodeQueue:
            node = nodeQueue.pop(0)
            if not node:
                continue
            leftChildValue = nodeValue.pop(0)
            rightChildValue = nodeValue.pop(0)
            node.left = TreeNode(int(leftChildValue)) if leftChildValue != 'null' else None
            node.right = TreeNode(int(rightChildValue)) if rightChildValue != 'null' else None
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
        return root
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))