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
        # newLastNode denotes the new last node, prevLastNode denotes the previous node before the current last node
        # interval denotes the interval between newLastNode and prevLastNode
        
        if not head:
            return []
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        interval = 0
        newLastNode, prevLastNode, node = head, dummyNode, head
        while node:
            # track the prevLastNode
            while interval > k:
                newLastNode = newLastNode.next
                interval -= 1
            
            prevLastNode, node = prevLastNode.next, node.next
            
            # prevLastNode is now the last node
            # if the interval < k, k >= length of linked list
            if not node and interval < k:
                newLastNode, prevLastNode, node = head, dummyNode, head
                k %= (interval + 1) # after every (interval + 1) rounds, the linked list remained the same
                interval = -1 # so that it become zero after the excution of the last line
                
            interval += 1
                   
        prevLastNode.next = head
        dummyNode.next = newLastNode.next
        newLastNode.next = None
        
        return dummyNode.next