"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def dfs(curr):
            tail = curr

            while curr:
                nxt = curr.next

                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    tail = child_tail
                else:
                    tail = curr

                curr = nxt

            return tail

        dfs(head)
        return head