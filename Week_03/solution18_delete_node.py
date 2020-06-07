
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head

        cur = head
        pre = dummy

        while cur:
            if cur.val == val:
                pre.next = cur.next
                return dummy.next
            pre = cur
            cur = cur.next

        return dummy.next
