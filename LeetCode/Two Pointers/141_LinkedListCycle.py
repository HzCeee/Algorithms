# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        lowPtr = fastPtr = head
        
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            lowPtr = lowPtr.next
            if lowPtr == fastPtr:
                return True
            
        return False