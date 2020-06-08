##Check if a linked list is Circular Linked List
##Given a singly linked list, find if the linked list is circular or not.
##A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.

##An empty linked list is considered as circular.

class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def circular(self):
        cur_node = self.head
        if self.head is None:
            return "yes"

        else:
            while cur_node.next==None:
                return "no"
            return "yes"

l = cll()
l.head = node(1)
second = node(2)
third = node(3)
fourth = node(4)

l.head.next = second
second.next = third
third.next = fourth
fourth.next = l.head

print (l.circular())
