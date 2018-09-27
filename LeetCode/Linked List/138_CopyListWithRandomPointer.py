# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        
        dummyNode, curNode = RandomListNode(-1), head
        nodeMapping = {None: None}
        while curNode:
            newNode = RandomListNode(curNode.label)
            newNode.next, newNode.random = curNode.next, curNode.random
            nodeMapping[curNode] = newNode
            curNode = curNode.next
        
        dummyNode.next, curNode = nodeMapping[head], head
        while curNode:
            nodeMapping[curNode].next, nodeMapping[curNode].random = nodeMapping[curNode.next], nodeMapping[curNode.random]
            curNode = curNode.next
        
        return dummyNode.next
            
        
            