# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_parents = []
        q_parents = []
        res = root
        def dfs(root, flag):
            if root == None:
                return False
            if flag == "p":
                if root == p:
                    p_parents.append(p)
                    return True
                if dfs(root.left, "p") == True:
                    p_parents.append(root)
                    return True
                else:
                    if dfs(root.right, "p") == True:
                        p_parents.append(root)
                        return True
                return False
            elif flag == "q":
                if root == q:
                    q_parents.append(q)
                    return True
                if dfs(root.left, "q") == True:
                    q_parents.append(root)
                    return True
                else:
                    if dfs(root.right, "q") == True:
                        q_parents.append(root)
                        return True
                return False
        dfs(root, "p")
        dfs(root, "q")

        p_index = len(p_parents) - 1
        q_index = len(q_parents) - 1

        while p_index >= 0 and q_index >= 0:
            if p_parents[p_index].val == q_parents[q_index].val:
                res = p_parents[p_index]
                p_index -= 1
                q_index -= 1               
            else:
                break

        return res