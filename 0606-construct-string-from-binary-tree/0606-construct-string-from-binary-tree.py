# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ''

        def dfs(node):

            nonlocal s

            if not node:
                return

            s += f"({node.val}"

            if node.left:
                dfs(node.left)
            elif node.right:
                s += '()'

            if node.right:
                dfs(node.right)

            s += ')'

        if not root:
            return ''

        dfs(root)

        return s[1:-1]