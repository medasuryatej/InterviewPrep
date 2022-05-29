# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = ListNode(0, head), ListNode(0, head)
        o, e = odd, even
        prev = None
        curr = head
        index = 0
        while curr:
            if index % 2 == 0:
                # even node
                # 1. connect even pointer to this node
                # 2. break prev to current and establish prev to current.next
                e.next = curr
                nextnode = curr.next
                curr.next = None
                e = e.next
                curr = nextnode
            else:
                # odd node
                o.next = curr
                nextnode = curr.next
                curr.next = None
                o = o.next
                curr = nextnode
            index += 1
        # o.next = even.next
        # return odd.next
        e.next = odd.next
        return even.next