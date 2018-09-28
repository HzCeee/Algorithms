# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyNode = ListNode(None)
        dummyNode.next = head
        prevNode, curNode = dummyNode, head
        while curNode:
            if curNode.val == val:
                prevNode.next = curNode.next
            else:
                prevNode = prevNode.next
            curNode = curNode.next
        
        return dummyNode.next