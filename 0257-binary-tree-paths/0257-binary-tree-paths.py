# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []
        
        def dfs(node, path):
            if not node:
                return
            # extend current path
            path += str(node.val)
            if not node.left and not node.right:  # leaf
                paths.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
        
        dfs(root, "")
        return paths
