# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def getNextNode(isHead, head):
            if isHead:
                nextNode, newHead = head, head.next
                return nextNode, newHead
            else:
                if not head.next:
                    return head, None
                
                prevNode, curNode = head, head.next
                while curNode.next:
                    prevNode, curNode = prevNode.next, curNode.next
                prevNode.next = None
                return curNode, head
        
        isHead = True
        
        dummyNode = ListNode(None)
        curNode = dummyNode
        
        while True:
            nextNode, newHead = getNextNode(isHead, head)
            curNode.next = nextNode
            curNode = curNode.next
            if not newHead:
                curNode.next = None
                return dummyNode.next
            head = newHead
            isHead = not isHead
            