"""Simple unbalanced binary search tree implementation.

Also contains basic pre-order, in-order, and post-order traversal functions.
"""
import random

ORDERED_ARRAY = [0, 1, 2, 3, 4, 5, 6]

class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def generate_array():
    return [random.randint(0, 100) for x in range(5)]


def build_tree(array):
    rand_val = random.randint(0, len(array) - 1)
    print("Random root index: ", rand_val, " ", array[rand_val])
    root = Node(array[rand_val])
    array.pop(rand_val)

    for x in array[1:]:
        current_node = root
        while True:
            if x < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(x, parent=current_node)
                    break
                else:
                    current_node = current_node.left

            if x >= current_node.value:
                if current_node.right is None:
                    current_node.right = Node(x, parent=current_node)
                    break
                else:
                    current_node = current_node.right

    return root

def traverse_tree(root):
    if root is None:
        return

    print(root.value)

    traverse_tree(root.left)
    traverse_tree(root.right)


def inorder_traversal(root):
    """Left, root, right"""
    if root is None:
        return
    
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def preorder_traversal(root):
    """Root, left, right"""
    if root is None:
        return
    
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    """left, right, root"""
    if root is None:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)


def main():
    # array = ORDERED_ARRAY
    array = generate_array()
    print(array)

    root = build_tree(array)
    print("in-order traversal (Left, Root, Right):")
    inorder_traversal(root)

    print("pre-order traversal (Root, Left, Right):")
    preorder_traversal(root)

    print("post-order traversal (Left, Right, Root):")
    postorder_traversal(root)


if __name__ == "__main__":
    main()