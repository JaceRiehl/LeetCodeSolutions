# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newHead = ListNode(next=head)
        prev = newHead
        current = head

        while current:
            nxt = current.next

            if current.val == val:
                prev.next = nxt
            else:
                prev = current
            current = nxt

        return newHead.next