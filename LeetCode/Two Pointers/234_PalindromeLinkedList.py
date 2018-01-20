# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # fast is 2-pace pointer
        # slow is 1-pace pointer
        # reverse is the previous node before slow
        
        slow = fast = head
        reverse = None
        
        while fast and fast.next:
            fast = fast.next.next
            tmp = reverse
            reverse = slow
            slow = slow.next
            reverse.next = tmp
        
        if fast: # if odd number in list, slow is now the center number index
            slow = slow.next
            
        while reverse and slow:
            if reverse.val == slow.val:
                reverse = reverse.next
                slow = slow.next
            else:
                return False
            
        return True