# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # smallHead denotes the head node with value smaller than x
        # smallTail denotes the tail node with value smaller than x
        # bigHead denotes the head node with value greater than x
        # bigTail denotes the tail node with value greater than x
        if not head:
            return head
        
        smallHead, smallTail, bigHead, bigTail = ListNode(None), ListNode(None), ListNode(None), ListNode(None)
        isSmallHead = isBigHead = True
        isNodeAfterSmallHead = isNodeAfterBigHead = True
        node = head
        
        while node:
            if node.val < x:
                tmp = smallTail
                smallTail = node
                
                if isNodeAfterSmallHead and not isSmallHead:
                    smallHead.next = smallTail
                    node = node.next
                    isNodeAfterSmallHead = False
                    continue
                    
                if isSmallHead:
                    smallHead = node
                    node = node.next
                    smallHead.next = None
                    isSmallHead = False
                    continue
                    
                node = node.next
                tmp.next = smallTail
            else:
                tmp = bigTail
                bigTail = node
                
                if isNodeAfterBigHead and not isBigHead:
                    bigHead.next = bigTail
                    node = node.next
                    isNodeAfterBigHead = False
                    continue
                
                if isBigHead:
                    bigHead = node
                    node = node.next
                    bigHead.next = None
                    isBigHead = False
                    continue
                    
                node = node.next
                tmp.next = bigTail
        
        bigTail.next = None
        smallTail.next = None
        
        if not isSmallHead:
            if not isBigHead:
                smallTail.next = bigHead
            return smallHead
        else:
            return bigHead
                