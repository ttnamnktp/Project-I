# BST
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def InsertNode(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if root.key > val:
            root.left = InsertNode(root.left, val)
        elif root.key < val:
            root.right = InsertNode(root.right, val)
        else:
            return root
    return root


def preOrder(root):
    if root:
        print(root.key, end=" ")  # Print the current node
        preOrder(root.left)  # Traverse the left subtree
        preOrder(root.right)  # Traverse the right subtree

# Helper function to print the PreOrder traversal of a BST
def printPreOrder(root):
    preOrder(root)
    print()


if __name__ == "__main__":
    root = None
    while True:
        Input = input().strip().split()
        if Input[0] == "#":
            break
        elif Input[0] == "insert":
            val = int(Input[1])
            root = InsertNode(root, val)
        else:
            continue

    printPreOrder(root)