class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        def dfs(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(nums) - 1)