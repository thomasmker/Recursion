class Node():
    def __init__(self, value) -> None:
        self.val = value
        self.next = None

    def set_next(self, value):
        self.next = value

def print_linked_list(node):
    tmp = node
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next

def reverse_list(node):
    if node is None or node.next is None:
        return node
    
    p = reverse_list(node.next)
    node.next.next = node
    node.next = None
    return p

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)

print_linked_list(n1)
reversed = reverse_list(n1)
print("")
print_linked_list(reversed)