class Solution(object):
    def levelOrderBottom(self, root):

        self.result = []
        self.preorder(root, 0, self.result)
        return self.result[::-1]

    def preorder(self, root, level, result):
        if len(result) < level + 1:
            result.append([])
        result[level].append(root.val)
        self.preorder(root.left, level + 1, result)
        self.preorder(root.right, level + 1, result)