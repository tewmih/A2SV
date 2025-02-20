# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            while curr.val == curr.next.val:
                if curr.next.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                    break
                
            curr = curr.next
        return head