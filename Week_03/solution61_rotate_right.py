
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        size = 1
        cur = head
        while cur.next:
            size += 1
            cur = cur.next
        cur.next = head
        rotate_size = size - k % size - 1
        cur = head
        for _ in range(rotate_size):
            cur = cur.next

        root = cur.next
        cur.next = None
        return root


