class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def morris(root):
            curr = root
            while curr != None:
                if curr.left == None:
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    prv = curr.left
                    while(prv.right != None and prv.right != curr):
                        prv  = prv.right
                    if prv.right == None:
                        prv.right = curr
                        curr = curr.left
                    else:
                        prv.right = None
                        ans.append(curr.val)
                        curr = curr.right
        morris(root)
        return ans
