# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # newLastNode denotes the new last node, lastNode denotes the previous node before the current last node
        
        if not head:
            return []
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        interval = 0
        newLastNode, prevLastNode, node = head, dummyNode, head
        while node:
            while interval > k:
                newLastNode = newLastNode.next
                interval -= 1
            
            prevLastNode, node = prevLastNode.next, node.next
            
            if not node and interval < k:
                newLastNode, prevLastNode, node = head, dummyNode, head
                
            interval += 1
        
        prevLastNode.next = head
        dummyNode.next = newLastNode.next
        newLastNode.next = None
        
        return dummyNode.next
            