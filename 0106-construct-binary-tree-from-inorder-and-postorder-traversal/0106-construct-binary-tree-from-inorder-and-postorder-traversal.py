class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        post = len(postorder) - 1

        def dfs(l, r):
            nonlocal post
            if l > r:
                return None

            root = TreeNode(postorder[post])
            post -= 1

            mid = pos[root.val]

            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)