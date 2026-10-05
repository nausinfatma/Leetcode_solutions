# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def count_paths(node, target):
            if not node:
                return 0

            count = 0

            if node.val == target:
                count += 1

            count += count_paths(node.left, target - node.val)
            count += count_paths(node.right, target - node.val)

            return count

        if not root:
            return 0

        return (
            count_paths(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )