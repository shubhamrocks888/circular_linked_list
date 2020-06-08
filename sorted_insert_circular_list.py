class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        cur_node = self.head

        if self.head:
            while cur_node.next!=self.head:
                cur_node = cur_node.next
            new_node.next = self.head
            cur_node.next = new_node
            self.head = new_node

        else:
            new_node.next = new_node
            self.head = new_node

    def print_list(self):
        cur_node = self.head

        while cur_node.next!=self.head:
            print (cur_node.data)
            cur_node = cur_node.next
        print (cur_node.data)

    def sortedinsert(self,data):
        new_node = node(data)
        cur_node = self.head
        if self.head is None:
            return

         # If value is smaller than head's value then we 
        # need to change next of last node 
        elif cur_node.data >= data:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head
            self.head = new_node

        else:
            while cur_node.next != self.head and data>=cur_node.next.data:
                cur_node = cur_node.next
            next_node = cur_node.next 
            cur_node.next = new_node
            new_node.next = next_node
                
            
##        if self.head:
##            cur_node = prev_node = self.head
##
##            while data>cur_node.data and cur_node.next!=self.head:
##                prev_node = cur_node
##                cur_node = cur_node.next
##
##            if data<cur_node.data:
##                new_node = node(data)
##                if cur_node == self.head:
##                    while cur_node.next!=self.head:
##                        cur_node = cur_node.next
##                    new_node.next = self.head
##                    cur_node.next = new_node
##                    self.head = new_node
##                        
##                    
##                else:
##                    next_node = prev_node.next
##                    prev_node.next = new_node
##                    new_node.next = next_node
##
##            else:
##                new_node = node(data)
##                next_node = cur_node.next
##                cur_node.next = new_node
##                new_node.next = next_node

l = cll()
l.push(8)
l.push(6)
l.push(4)
l.push(2)
l.push(1)
##l.print_list()
l.sortedinsert(9)
l.print_list()

            
            
        
            
