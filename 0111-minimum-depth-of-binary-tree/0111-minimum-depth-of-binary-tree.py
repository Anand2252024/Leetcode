class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if root.left is None:
            return right_depth + 1

        if root.right is None:
            return left_depth + 1

        return min(left_depth, right_depth) + 1