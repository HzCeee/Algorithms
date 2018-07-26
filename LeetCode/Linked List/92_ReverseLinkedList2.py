class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        
        dummyNode = ListNode(None)
        dummyNode.next = head
        
        curCount, prevNode, curNode, nextNode = 1, dummyNode, head, head.next
        reverse = False
        for count in range(1, n+1):
            if count == m:
                prevStartNode, startNode = prevNode, curNode
                reverse = True
            if count == n:
                nextEndNode, endNode = nextNode, curNode
            
            if reverse:
                curNode.next = prevNode

            prevNode, curNode = curNode, nextNode
            if nextNode: nextNode = nextNode.next
        
        prevStartNode.next = endNode
        startNode.next = nextEndNode
        
        return dummyNode.next
        