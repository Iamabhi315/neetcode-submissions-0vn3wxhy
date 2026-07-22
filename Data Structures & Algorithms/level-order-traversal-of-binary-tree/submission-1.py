# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        indx = 0
        res = []

        while indx < len(q):
            temp = len(q) - indx
            lst = []
            for j in range(temp):
                lst.append(q[indx].val)
                if q[indx].left:
                    q.append(q[indx].left)
                if q[indx].right:
                    q.append(q[indx].right)
                indx += 1
            res.append(lst)
        return res