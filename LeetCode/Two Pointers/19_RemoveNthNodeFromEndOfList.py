# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # prevIndex denotes the index of (n + 1)-th to last node, lastIndex denotes the index of current last node
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        prevNode = dummyNode
        prevIndex, lastIndex = -1, -1
        
        curNode = head
        
        while curNode:
            lastIndex += 1
            while lastIndex - prevIndex > n:
                prevNode = prevNode.next
                prevIndex += 1
            curNode = curNode.next
            
        prevNode.next = prevNode.next.next
        
        return dummyNode.next