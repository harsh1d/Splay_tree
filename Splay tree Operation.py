class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def splay(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        if root.left is None:
            return root

        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = left_rotate(root.left)
            return root if root.left is None else right_rotate(root)
    else:
        if root.right is None:
            return root

        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = right_rotate(root.right)
            return root if root.right is None else left_rotate(root)

    return root

def insert(root, key):
    if root is None:
        return Node(key)

    root = splay(root, key)

    if root.key == key:
        return root

    new_node = Node(key)

    if key < root.key:
        new_node.right = root
        new_node.left = root.left
        root.left = None
    else:
        new_node.left = root
        new_node.right = root.right
        root.right = None

    return new_node

# Traversal in Splay Tree

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.key, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=' ')

# Example usage

root = None
keys = [10, 20, 15, 5]
for key in keys:
    root = insert(root, key)

print("Inorder Traversal: ")
inorder_traversal(root)
print("\nPreorder Traversal: ")
preorder_traversal(root)
print("\nPostorder Traversal: ")
postorder_traversal(root)
