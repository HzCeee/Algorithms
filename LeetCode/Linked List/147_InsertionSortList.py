# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummyNode = ListNode(None)
        dummyNode.next, prevNode, curNode = head, head, head.next
        while curNode:
            prevCmpNode, cmpNode = dummyNode, dummyNode.next
            nextNode = curNode.next
            isChanged = False
            while cmpNode is not curNode and cmpNode:
                if curNode.val < cmpNode.val:
                    prevCmpNode.next, curNode.next, prevNode.next = curNode, cmpNode, nextNode
                    isChanged = True
                    break
                prevCmpNode, cmpNode = prevCmpNode.next, cmpNode.next
            curNode = nextNode
            if not isChanged: 
                prevNode = prevNode.next
        return dummyNode.next