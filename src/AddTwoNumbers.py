""" LeetCode 2.Add Two Numbers 
 Does addition how you would in elementary school. Ones place first and so on. Thats why the reversed linked list works for us.
 Edge Cases:
    Have to watch out for carry
    Carry on the final place
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummyNode = ListNode()
        current = dummyNode
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            current.next = ListNode(carry)
        return dummyNode.next
