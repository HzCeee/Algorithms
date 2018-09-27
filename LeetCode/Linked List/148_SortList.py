# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        fastPtr, slowPtr = head, head
        while fastPtr.next and fastPtr.next.next:
            fastPtr, slowPtr = fastPtr.next.next, slowPtr.next
        firstPart, secondPart = head, slowPtr.next
        slowPtr.next = None
        
        ptr1, ptr2 = self.sortList(firstPart), self.sortList(secondPart)
        dummyNode = ListNode(None)
        curNode = dummyNode
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curNode.next = ptr1
                ptr1 = ptr1.next
            else:
                curNode.next = ptr2
                ptr2 = ptr2.next
                
            curNode = curNode.next
        curNode.next = ptr1 if ptr1 else ptr2
        
        return dummyNode.next