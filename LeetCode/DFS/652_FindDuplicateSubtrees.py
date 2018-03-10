class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        self.memo = {}
        
        # return the tree representation given root node
        def findDuplicateSubtreesHelper(node):
            if not node:
                return ['null']
            tree = [node.val] + findDuplicateSubtreesHelper(node.left) + findDuplicateSubtreesHelper(node.right)
            
            if tuple(tree) not in self.memo:
                self.memo[tuple(tree)] = 1
            else:
                if self.memo[tuple(tree)] == 1: res.append(node)
                self.memo[tuple(tree)] += 1
                
            return tree
        
        findDuplicateSubtreesHelper(root)
        
        return res