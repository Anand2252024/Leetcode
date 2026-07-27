class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def preorder(node):
            if not node:
                return

            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None