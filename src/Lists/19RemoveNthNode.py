# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)

        s,f = dummy,head
        
        for i in range(n):
            f = f.next
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next