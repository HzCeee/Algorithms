# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(None)
        curNode = dummyNode
        
        while l1 and l2:
            if l1.val < l2.val:
                curVal = l1.val
                l1 = l1.next
            else:
                curVal = l2.val
                l2 = l2.next
            curNode.next = ListNode(curVal)
            curNode = curNode.next
        
        if l1:
            curNode.next = l1
        else:
            curNode.next = l2
        
        return dummyNode.next
            