class Node:
    def __init__(self, data, next=None):
        self.entry = data
        self.next = next

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
p = Node(1,next=num1)
q = Node(1,next=num2)

def compare(p,q):
    if p.entry > q.entry or p is None or q is None:
        return False
    elif p.entry < q.entry:
        return True
    else:
        return compare(p.next,q.next)

