from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __repr__(self):
        return f"<{self.val} -> {self.next.val if self.next is not None else None}>"

    def __str__(self):
        s = []
        curr = self
        while curr is not None:
            s.append(curr.val)
            curr = curr.next
        return str(s)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle edge cases
        if head is None or k == 0:
            return head

        # convert ListNodes to list of ListNodes
        nodes: List[ListNode] = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        # shift list
        nodes[-1].next = nodes[0]
        k = k % len(nodes)
        nodes[-k - 1].next = None
        return nodes[-k]  # return new head
