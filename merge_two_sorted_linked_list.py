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

def sorted_merge(nodeA, nodeB):
    if nodeA == None:
        return nodeB
    if nodeB == None:
        return nodeA
    
    if nodeA.val < nodeB.val:
        nodeA.next = sorted_merge(nodeA.next,nodeB)
        return nodeA
    else:
        nodeB.next = sorted_merge(nodeA,nodeB.next)
        return nodeB

# Sorted linked list A
a1 = Node(1)
a2 = Node(8)
a3 = Node(22)
a4 = Node(40)
a1.set_next(a2)
a2.set_next(a3)
a3.set_next(a4)

# Sorted linked list B
b1 = Node(4)
b2 = Node(11)
b3 = Node(16)
b4 = Node(20)
b1.set_next(b2)
b2.set_next(b3)
b3.set_next(b4)

head = sorted_merge(a1,b1)
print_linked_list(head)