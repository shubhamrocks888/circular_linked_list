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
        new_node.next = self.head

        if self.head:
            while cur_node.next!= self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

        else:
            new_node.next = new_node
        self.head = new_node

    def delete_node(self,data):
        # If linked list is empty
        if self.head is None:
            return

        # If the list contains only a single node
        if (self.head.data==data) and (self.head.next==self.head):
            self.head = None
            return
            
        cur_node = prev_node = self.head

        while cur_node.data!=data:
            prev_node = cur_node
            cur_node = cur_node.next
        
        if prev_node == cur_node:
            while cur_node.next!=self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = cur_node.next

        else:
            prev_node.next = cur_node.next
            


    def print_list(self):
        cur_node = self.head

        while cur_node.next!=self.head:
            print(cur_node.data)
            cur_node = cur_node.next
        print (cur_node.data)

l= cll()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.delete_node(5)
l.print_list()
