class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, curr_sum):
            if node is None:
                return

            path.append(node.val)
            curr_sum += node.val

            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    result.append(path[:])

            dfs(node.left, path, curr_sum)
            dfs(node.right, path, curr_sum)

            path.pop()

        dfs(root, [], 0)
        return result