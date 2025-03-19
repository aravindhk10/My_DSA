class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.rightside(root, 0, ans)
        return ans
    def rightside(self, root, level, ans):
        if root == None:
            return
        elif len(ans) == level:
            ans.append(root.val)
        self.rightside(root.right, level+1, ans)
        self.rightside(root.left, level+1, ans)
