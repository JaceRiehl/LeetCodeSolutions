"""
Leetcode 26 Removing duplicates from a sorted list
This is going to use a slightly different strategy from the array approach. This one is going to have an inner loop that cycles through the duplicates.

O(n) time
O(1) space

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def deleteDuplicates(head):
    current = head
    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next
        current = current.next
    return head