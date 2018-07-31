"""This problem mimics one I encountered in an online interview.

Given a sorted array of unique integers, build a binary search tree, and find the distance between two nodes.

Example: Given an input of [2,3,6,7,9,23], n = 6, and two values (2, 6), return the distance between 2 and 6.

If one of the values does not exist in the tree, return None

A caviat to this problem was that I was asked not to write additional functions. I'm going to in my solution here
becuase that's a somewhat insane requirement.
"""
INPUT_ARRAY = [2, 3, 6, 7, 9, 23]

def main(array, n, val1, val2):
    """This problem breaks down into two fundamental parts, build the BST, then find the distance between the two
    nodes.
    """
    # Given the sorted input array, build the tree
    root = build_tree(array, n)

    # Find the distance between the two values
    print(find_distance(root, val1, val2))


class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
    

def build_tree(array, n):
    """Because the input array is sorted, we can simply start at the middle of the array for an ideal root."""
    if n % 2 == 0:
        middle = int(n / 2)
    else:
        middle = int((n - .5) / 2)  
    
    root = Node(array[middle])
    array.pop(middle)

    for x in array[0:]:
        current_node = root
        while True:
            if x < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(x, parent=current_node)
                    break
                else:
                    current_node = current_node.left

            # >= here is for good form due to the uniqueness of the integers
            if x >= current_node.value:
                if current_node.right is None:
                    current_node.right = Node(x, parent=current_node)
                    break
                else:
                    current_node = current_node.right

    return root


def find_distance(root, val1, val2):
    """The approach we use here is to find node1, node2, and the lowest common node between the two, and subtract the 
    total path from both to find the path length between the two nodes.
    """
    # Find length of path to node1
    l1_path = find_path(root, val1, [])

    # Find length of path to node2
    l2_path = find_path(root, val2, [])

    lowest_common_node = None
    for x, y in zip(l1_path, l2_path):
        if x == y:
            lowest_common_node = x
        else:
            break
    
    # Find lowest common node
    l3_path = find_path(root, lowest_common_node, [])

    # Subtract (node1 - LCN) + (node2 - LCN)
    return (len(l1_path) - len(l3_path)) + (len(l2_path) - len(l3_path))


def find_path(node, matching, path):
    if node is not None:
        if node.value == matching:
            path.append(node.value)
            return path
        
        if matching < node.value:
            path.append(node.value)
            return find_path(node.left, matching, path)
        
        if matching > node.value:
            path.append(node.value)
            return find_path(node.right, matching, path)


if __name__ == "__main__":
    main(INPUT_ARRAY, len(INPUT_ARRAY), 6, 23)