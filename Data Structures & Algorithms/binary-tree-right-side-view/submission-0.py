# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        indx = 0
        res = []

        while indx < len(q):
            temp = len(q) - indx
            res.append(q[-1].val)
            for j in range(temp):
                if q[indx].left:
                    q.append(q[indx].left)
                if q[indx].right:
                    q.append(q[indx].right)
                indx += 1
        return res