# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        stack = []
        ans = []
        while stack or head:
            while head:
                stack.append(head)
                head = head.left
            head = stack.pop()
            ans.append(head.val)
            head = head.right
        return ans
