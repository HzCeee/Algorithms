# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        prevNode, curNode, nextNode = dummyNode, head, head.next
        duplicate = False
        
        while curNode and nextNode:
            if curNode.val == nextNode.val:
                duplicate = True
                nextNode = nextNode.next
            else:
                if not duplicate:
                    prevNode.next = curNode
                    prevNode = curNode
                curNode, nextNode = nextNode, nextNode.next
                duplicate = False
        prevNode.next = None if duplicate else curNode
        
        return dummyNode.next
                    
            