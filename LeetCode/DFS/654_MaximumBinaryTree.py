class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # return root of the tree constructed given nums
        def constructMaximumBinaryTreeHelper(nums):
            if not nums:
                return None
            index, rootVal = max(enumerate(nums), key=lambda num: num[1])
            node = TreeNode(rootVal)
            node.left = constructMaximumBinaryTreeHelper(nums[:index])
            node.right = constructMaximumBinaryTreeHelper(nums[index+1:])
            return node
        
        return constructMaximumBinaryTreeHelper(nums)
        
        