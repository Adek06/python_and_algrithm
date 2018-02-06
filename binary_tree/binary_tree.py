"""
binary tree creat
"""

class Node():
    """ Node object """

    def __init__(self, key):
        ''' init node '''

        self.key = key
        self.left = None
        self.right = None

class BinaryTree():
    """ Binary Tree object """

    def __init__(self):
        self.root = None

    def insert_node(self, node, new_node):
        ''' insert left node and right node '''

        if new_node.key < node.key:
            if node.left is None:
                node.left = new_node
            else:
                return self.insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                return self.insert_node(node.right, new_node)


    def insert(self, key):
        ''' insert node '''

        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def in_oder_traverse(self, node):
        ''' inoder traverse '''

        if node is None:
            return []
        result = [node.key]
        left_result = self.in_oder_traverse(node.left)
        right_result = self.in_oder_traverse(node.right)
        return left_result + result + right_result
    
    def pre_oder_traverse(self, node):
        ''' preoder traverse '''

        if node is None:
            return []
        result = [node.key]
        left_result = self.pre_oder_traverse(node.left)
        right_result = self.pre_oder_traverse(node.right)
        return result + left_result + right_result

    def post_oder_traverse(self, node):
        ''' postoder traverse '''

        if node is None:
            return []
        result = [node.key]
        left_result = self.post_oder_traverse(node.left)
        right_result = self.post_oder_traverse(node.right)
        return left_result + right_result + result
    
    def search_node(self, node, key):
        ''' search a node,exist return true,else return false '''
        if node is None:
            return False
        else:
            if key < node.key:
                return self.search_node(node.left, key)
            elif key > node.key:
                return self.search_node(node.right, key)
            else:
                return True

if __name__ == "__main__":
    NODES = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    BINARY_TREE = BinaryTree()
    for i in NODES:
        BINARY_TREE.insert(i)
    print(BINARY_TREE.in_oder_traverse(BINARY_TREE.root))
    print(BINARY_TREE.pre_oder_traverse(BINARY_TREE.root))
    print(BINARY_TREE.post_oder_traverse(BINARY_TREE.root))
    print(BINARY_TREE.search_node(BINARY_TREE.root, 7))
    print(BINARY_TREE.search_node(BINARY_TREE.root, 9))
