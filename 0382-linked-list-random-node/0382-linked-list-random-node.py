# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        self.head = head
        

    def getRandom(self) -> int:
        curr = self.head
        chosen = None
        count = 0

        while curr:
            count += 1

            if random.randint(1, count) == 1:
                chosen = curr.val

            curr = curr.next

        return chosen
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()