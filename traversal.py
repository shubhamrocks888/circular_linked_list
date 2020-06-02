class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        cur_node = self.head
        new_node.next = self.head

        if self.head:
            
            while cur_node.next!=self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

##    def push(self,data):
##        new_node = node(data)
##        cur_node = self.head
##        if self.head:
##            while cur_node.next!=self.head:
##                cur_node = cur_node.next
##            new_node.next = self.head
##            cur_node.next = new_node
##            self.head = new_node
##        else:
##            self.head = new_node
##            new_node.next = self.head

    def print_list(self):
        cur_node = self.head
        while cur_node.next!=self.head:
            print(cur_node.data)
            cur_node = cur_node.next
        print(cur_node.data)
##        temp = self.head 
##        if self.head is not None: 
##            while(True): 
##                print (temp.data)
##                temp = temp.next
##                if (temp == self.head): 
##                    break 

l = circular_linked_list()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.print_list()
