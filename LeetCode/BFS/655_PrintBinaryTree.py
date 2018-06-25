class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        nodeQueue = [root] if root else [None]
        nodeInEachLayer = {}
        depth = 0
        while any(nodeQueue):
            nodeInEachLayer[depth] = [str(node.val) if node else "" for node in nodeQueue]
            depth += 1
            
            nextLayer = []
            for node in nodeQueue:
                nextLayer += [node.left, node.right] if node else [None, None]
            nodeQueue = nextLayer
        
        # print tree
        ans = []
        neighbourBlockCount = -0.5
        for i in range(depth):
            neighbourBlockCount = int(2 * neighbourBlockCount + 1)
            layer = []
            for index, node in enumerate(nodeInEachLayer[depth - 1 - i]):
                layer += neighbourBlockCount*[""] + [node] + neighbourBlockCount*[""]
                if index != len(nodeInEachLayer[depth - 1 - i]) - 1: layer += [""]
            ans.insert(0, layer)
        return ans