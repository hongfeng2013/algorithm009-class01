
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        size = 0
        cur = dummy
        while cur.next:
            size += 1
            cur = cur.next
        cur = dummy
        for _ in range(size - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next

