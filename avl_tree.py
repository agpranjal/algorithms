class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None
        self.height = 1

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

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

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        p = inorder_successor(root) or inorder_predecessor(root)

        if not p:
            return None

        root.val = p.val
        root.left = delete(root.left, p.val)
        root.right = delete(root.right, p.val)

    if bf(root) == 2 and bf(root.left) == 1:
        return ll_rotation(root)
    elif bf(root) == 2 and bf(root.left) == -1:
        return lr_rotation(root)
    elif bf(root) == -2 and bf(root.right) == -1:
        return rr_rotation(root)
    elif bf(root) == -2 and bf(root.right) == 1:
        return rl_rotation(root)

    return root



def level_order(ROOT):
    queue = [ROOT]
        
    while queue:
        ptr = queue.pop(0)
        print(ptr.val, end=" ")

        if ptr.left:
            queue.append(ptr.left)
        if ptr.right:
            queue.append(ptr.right)
    print()

def node_height(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1
    
    if not root.left:
        return root.right.height+1
    if not root.right:
        return root.left.height+1

    return max(root.left.height, root.right.height)+1

def bf(root):
    if not root.left and not root.right:
        return 1
    if not root.left:
        return -(root.right.height)
    if not root.right:
        return root.left.height

    return root.left.height - root.right.height

def ll_rotation(root):
    new_root = root.left
    t = new_root.right
    new_root.right = root
    root.left = t
    
    root.height = node_height(root)
    new_root.height = node_height(new_root)
    
    return new_root

def lr_rotation(root):
    new_root = root.left.right
    lc = new_root.left
    rc = new_root.right

    new_root.left = root.left
    new_root.right = root
    root.left = rc
    new_root.left.right = lc

    root.height = node_height(root)
    new_root.height = node_height(new_root)

    return new_root

def rr_rotation(root):
    new_root = root.right
    lc = new_root.left
    new_root.left = root
    root.right = lc

    root.height = node_height(root)
    new_root.height = node_height(new_root)


    return new_root

def rl_rotation(root):
    new_root = root.right.left
    lc = new_root.left
    rc = new_root.right

    new_root.left = root
    new_root.right = root.right
    
    root.right = lc
    new_root.right.left = rc

    root.height = node_height(root)
    new_root.height = node_height(new_root)

    return new_root

def insert(root, val):
    if not root:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    root.height = node_height(root)
    if bf(root) == 2 and bf(root.left) == 1:
        return ll_rotation(root)
    elif bf(root) == 2 and bf(root.left) == -1:
        return lr_rotation(root)
    elif bf(root) == -2 and bf(root.right) == -1:
        return rr_rotation(root)
    elif bf(root) == -2 and bf(root.right) == 1:
        return rl_rotation(root)

    return root

ROOT = None
values = [10, 5, 15, 2, 9, 12, 20, 3, 17, 30]

for i in range(len(values)):
    ROOT = insert(ROOT, values[i])

delete(ROOT, 15)
delete(ROOT, 12)
inorder(ROOT)
