class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

def preorder(root):
    if not root:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def inorder_iter(root):
    stack = [root]
    left = []

    while stack:
        ptr = stack[-1]
        if ptr.left and ptr not in left:
            stack.append(ptr.left)
            left.append(ptr)
        else:
            print(ptr.val, end=" ")
            stack.pop()
            if ptr.right:
                stack.append(ptr.right)


def insert(root, val):
    if not root:
        return Node(val)

    if val > root.val:
        root.right = insert(root.right, val)
    if val < root.val:
        root.left = insert(root.left, val)

    return root

def inorder_predecessor(root):
    root = root.left

    while root and root.right:
        root = root.right

    return root

def inorder_successor(root):
    root = root.right

    while root and root.left:
        root = root.left

    return root

def delete(root, val):
    if not root:
        return 

    if val > root.val:
        root.right = delete(root.right, val)
    elif val < root.val:
        root.left = delete(root.left, val)
    else:
        p = inorder_predecessor(root) or inorder_successor(root)

        if not p:
            return None

        root.val = p.val
        root.left = delete(root.left, p.val)
        root.right = delete(root.right, p.val)
    
    return root

root = Node(50)
insert(root, 10)
insert(root, 40)
insert(root, 20)
insert(root, 30)
inorder(root)
print()
inorder_iter(root)
