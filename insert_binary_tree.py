class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def set_right(self, value):
        self.right = value

    def set_left(self, value):
        self.left = value;

def insertNode(head, data):
    if head is None:
        head = Node(data)
        return head
    
    if head.data < data:
        head.set_right(insertNode(head.right, data))
    else:
        head.set_left(insertNode(head.left, data))
    
    return head

def print_leaves(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    
    if root.left is not None:
        print_leaves(root.left)

    if root.right is not None:
        print_leaves(root.right)

head = insertNode(None, 10)
head = insertNode(head, 5)
head = insertNode(head, 15)
print_leaves(head)

head = insertNode(head, 3)
head = insertNode(head, 7)
head = insertNode(head, 13)
head = insertNode(head, 17)
print_leaves(head)