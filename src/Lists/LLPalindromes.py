class Solution:
    def isPalindrome(self, head) -> bool:
        set1 = []
        while True:
            set1.append(head.val)
            if head.next:
                head = head.next
            else: break
        if set1 == set1[::-1]: 
            return True
        else:
            return False