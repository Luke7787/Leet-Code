# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque([root])
        res = []
        while queue:
            level_count = len(queue)
            level_sum = 0
            for _ in range(level_count):
                root = queue.popleft()
                level_sum += root.val
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
            res.append(float(level_sum)/level_count)
        return res