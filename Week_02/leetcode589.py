"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def pre(self, root, res):
        if root == None:
            return res
        else:
            res.append(root.val)
            for i in range(len(root.children)):
                self.pre(root.children[i], res)

        return res

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        res = self.pre(root, res)

        return res