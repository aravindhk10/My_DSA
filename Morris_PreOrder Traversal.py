def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return(self.morris(res, root))

    def morris(self, res, root):
        curr = root
        while curr != None:
            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            else:
                prv = curr.left
                while prv.right != None and prv.right != curr:
                    prv = prv.right
                if prv.right == None:
                    prv.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    prv.right = None
                    curr = curr.right
        return res
