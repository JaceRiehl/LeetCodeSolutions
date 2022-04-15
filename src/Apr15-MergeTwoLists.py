""" LeetCode 6.Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    blank_node = ListNode()
    current = blank_node
    while list1 or list2:
        v1 = list1.val if list1 else None
        v2 = list2.val if list2 else None
        if (v1 or v1 == 0) and (v2 or v2 == 0):
            if v1 <= v2:
                current.next = ListNode(v1)
                current = current.next
                list1 = list1.next if list1 else None
            elif v2 <= v1:
                current.next = ListNode(v2)
                current = current.next
                list2 = list2.next if list2 else None
        elif v1 or v1 == 0:
            current.next = ListNode(v1)
            current = current.next
            list1 = list1.next if list1 else None
        elif v2 or v2 == 0:
            current.next = ListNode(v2)
            current = current.next
            list2 = list2.next if list2 else None
    return blank_node.next 

print(mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))), ListNode(1,ListNode(3,ListNode(4)))).val)
