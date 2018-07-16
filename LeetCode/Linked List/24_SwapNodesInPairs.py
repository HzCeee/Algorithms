# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        prevNode, curNode, nextNode = dummyNode, head, head.next
        while curNode is not None and nextNode is not None:
            prevNode.next = nextNode
            curNode.next = nextNode.next
            nextNode.next = curNode
            
            # next pairs
            prevNode, curNode= curNode, curNode.next
            nextNode = curNode.next if curNode else None
        
        return dummyNode.next