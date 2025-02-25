# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        if not head.next.next:
            return head.val + head.next.val

        fast = head
        slow  = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow
        while cur:
            next_seg = cur.next
            cur.next = prev
            prev = cur
            cur = next_seg
        _max = float("-inf")
        temp = head
        while prev:
            _sum = prev.val + temp.val
            _max = max(_max, _sum)
            prev = prev.next
            temp = temp.next
        return _max