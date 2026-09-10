# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        odd_d = ListNode(0)
        even_d = ListNode(0)

        odd = odd_d
        even = even_d

        curr = head

        while curr:
            i += 1
            if i % 2 != 0:
                odd.next = curr
                odd = odd.next

            else:
                even.next = curr
                even = even.next

            curr = curr.next
        
        odd.next = even_d.next
        even.next = None

        return odd_d.next