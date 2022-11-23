from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __repr__(self):
        return f"<{self.val} -> {self.next.val if self.next != None else None}>"

    def __str__(self):
        s = []
        curr = self
        while curr != None:
            s.append(curr.val)
            curr = curr.next
        return str(s)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle edge cases
        if head is None or k == 0:
            return head

        # convert ListNodes to list of ListNodes
        l: List[ListNode] = []
        curr = head
        while curr != None:
            l.append(curr)
            curr = curr.next

        # shift list
        l[-1].next = l[0]
        k = k % len(l)
        l[-k - 1].next = None
        return l[-k]  # return new head
