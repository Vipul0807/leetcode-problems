# Binary Tree Inorder Traversal
# Difficulty: Unknown
# Language: Python

class Solution:
    def inorderTraversal(self, root):
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        def build_tree(values):
            if not values:
                return None

            nodes = [TreeNode(v) if v is not None else None for v in values]
            for i in range(len(values)):
                if nodes[i] is not None:
                    left_index = 2 * i + 1
                    right_index = 2 * i + 2

                    if left_index < len(values):
                        nodes[i].left = nodes[left_index]
                    if right_index < len(values):
                        nodes[i].right = nodes[right_index]

            return nodes[0]

        if isinstance(root, str):
            root = root.replace("null", "None")
            root = eval(root)

        if isinstance(root, list):
            root = build_tree(root)

        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result