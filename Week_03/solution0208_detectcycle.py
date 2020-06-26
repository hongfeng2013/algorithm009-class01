
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur:
            if cur.val is True:
                return cur
            cur.val = True
            cur = cur.next
        return cur