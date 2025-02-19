# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # current = head
        # # if current.next = None:
        # #     del current
        # #     return []
        # while current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #         current.next.next=None
        #         del current.next.next
        #     current = current.next
        # return head

        new_node = ListNode(100)
        new_node.next = head
        prev = None

        current = new_node
        if head== None:
            return head
        n = head.next
        # prev = new_node
        while current != None:
            # if current and current.val == val
            if  current and current.val == val:
                current = n
                prev.next = n
                if current != None:
                    n = current.next
            else:
                prev = current
                current = n
                if current != None:
                    n = current.next

        return new_node.next

