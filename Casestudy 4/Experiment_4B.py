class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    while True:
        data = input("Enter the book name (enter 0 to stop): ")

        if data == "0":
            return None

        root = Node(data)

        print("Enter left of", data)
        root.left = create()

        print("Enter right of", data)
        root.right = create()

        return root


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = create()

print("Preorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)