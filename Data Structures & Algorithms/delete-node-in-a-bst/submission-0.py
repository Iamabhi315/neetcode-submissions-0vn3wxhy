# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        curr = root
        prev = None

        while curr:

            if curr.val == key:

                # Case 1: Leaf node
                if not curr.left and not curr.right:
                    if not prev:
                        root = None
                    elif prev.left == curr:
                        prev.left = None
                    else:
                        prev.right = None
                    break

                # Case 2: Only right child
                elif not curr.left:
                    if not prev:
                        root = curr.right
                    elif prev.left == curr:
                        prev.left = curr.right
                    else:
                        prev.right = curr.right
                    break

                # Case 3: Only left child
                elif not curr.right:
                    if not prev:
                        root = curr.left
                    elif prev.left == curr:
                        prev.left = curr.left
                    else:
                        prev.right = curr.left
                    break
 
                # Case 4: Two children
                else:
                    parent = curr
                    temp = curr.right

                    # Find inorder successor
                    while temp.left:
                        parent = temp
                        temp = temp.left

                    # Copy successor value
                    curr.val = temp.val

                    # Delete successor
                    if parent.left == temp:
                        parent.left = temp.right
                    else:
                        parent.right = temp.right

                    break

            elif key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        return root