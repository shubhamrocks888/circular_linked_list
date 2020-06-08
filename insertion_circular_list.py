##Insertion
##A node can be added in three ways:
##
##Insertion in an empty list
##Insertion at the beginning of the list
##Insertion at the end of the list
##Insertion in between the nodes
## 

class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def add_empty(self,data):
        new_node = node(data)
        new_node.next = new_node
        self.head = new_node

    def add_beginning(self,data):
        new_node = node(data)
        cur_node = self.head

        while cur_node.next!=self.head:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next!=self.head:
            cur_node = cur_node.next
        cur_node.next  = new_node
        new_node.next = self.head

    def add_after(self,data,item):
        new_node = node(data)
        cur_node = self.head

        while cur_node.data != item:
            cur_node = cur_node.next
        next_node = cur_node.next
        cur_node.next  = new_node
        new_node.next = next_node

    def print_list(self):
        cur_node = self.head

        while cur_node.next!=self.head:
            print(cur_node.data)
            cur_node = cur_node.next
            
        print(cur_node.data)

llist = cll()
llist.add_empty(6) 
llist.add_beginning(4) 
llist.add_beginning(2) 
llist.add_end(8) 
llist.add_end(12) 
llist.add_after(10,8) 
  
llist.print_list()
        
        
