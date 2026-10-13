class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def create():
    root = None

    while True:
        data = int(input("Enter admission number (enter 0 to stop): "))

        if data == 0:
            return root

        root = insert(root, data)


def preorder(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) != 0:
        current = stack.pop()

        print(current.data, end=" ")

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


root = create()

print("Non-Recursive Preorder Traversal:")
preorder(root)