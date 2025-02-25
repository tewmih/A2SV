# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        curr = head
        flag = True

        while curr and curr.next:
            next_node = curr.next

            if flag:
                odd.next = curr.next.next
                if odd.next:
                    odd = odd.next
                flag = not flag
            else:
                even.next = curr.next.next
                even = even.next
                flag = not flag
            curr = next_node
        odd.next = even_head
        return head

