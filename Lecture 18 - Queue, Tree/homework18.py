class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def printParents(self):
        print('The parents of each node are: ')
        self._printParents(self.root, None)

    def _printParents(self, node, parentNode):
        if node is not None:
            if parentNode is None:
                print(node.key, '-> Root')
            else:
                print(node.key, '->', parentNode.key)

            self._printParents(node.left, node)
            self._printParents(node.right, node)

    def findLeaves(self, root):
        def dfs(root):
            if root is None:
                return -1

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            height = max(left_height, right_height) + 1

            if root.left is None and root.right is None:
                if height == len(ans):
                    ans.append([])
                ans[height].append(root.key)

            return height

        ans = []
        dfs(root)
        return ans[-1] if ans else []


    def count_edges(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return self._count_nodes(node) - 1

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)


tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(14)
tree.insert(16)
tree.insert(9)
tree.insert(4)


#       10
#      /  \
#     5    15
#    / \   / \
#   4   9|14  16


print('total edges: ', tree.count_edges())
print('leaves: ', tree.findLeaves(tree.root))