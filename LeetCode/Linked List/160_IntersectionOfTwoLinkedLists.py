# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        NodeSet = set()
        node = headA
        while node:
            NodeSet.add(node)
            node = node.next
        node = headB
        while node:
            if node in NodeSet:
                return node
            node = node.next
        return None