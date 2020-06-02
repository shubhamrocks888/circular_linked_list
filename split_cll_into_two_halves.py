##Split a Circular Linked List into two halves
##If there are odd number of nodes, then first list should contain one extra.
##Original Circular Linked List
##11 2 56 12 
##First Circular Linked List
##11 2 
##Second Circular Linked List
##56 12 
##Time Complexity: O(n)

##Thanks to Geek4u for suggesting the algorithm.
##1) Store the mid and last pointers of the circular linked list using tortoise and hare algorithm.
##2) Make the second half circular.
##3) Make the first half circular.
##4) Set head (or start) pointers of the two linked lists.




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
            while cur_node.next!=self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node



##    def length(self):
##        cur_node = self.head
##        count =0
##
##        while cur_node.next!=self.head:
##            count+=1
##            cur_node = cur_node.next
##        count+=1
##        return count
##        
##    def split(self,head1,head2):
##        len = self.length()
##        if (len%2)==0:
##            mid = (len/2)
##        else:
##            mid = (len//2) + 1
##        count = 0
##
##        prev_node = cur_node = self.head
##        

##        if self.head:
##            while count!=mid:
##                count +=1
##                prev_node = cur_node
##                cur_node = cur_node.next
##            prev_node.next = self.head
##            head1.head = self.head
##
##            head2.head = cur_node
##            while cur_node.next!=self.head:
##                cur_node = cur_node.next
##            cur_node.next = head2.head
##            
    def split(self,head1,head2):
        slow_ptr = fast_ptr = self.head

        if self.head is None:
            print ("empty list")
            return

        while fast_ptr.next != self.head and fast_ptr.next.next!=self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        head1.head = self.head
##take the example of 1,2,3,4,5  for if condition and make algo
##and for else case take the condition of 1,2,3,4 and make algo
        if fast_ptr.next==self.head:
            
            head2.head = slow_ptr.next
            slow_ptr.next = head1.head
            fast_ptr.next = head2.head
        else:
            head2.head = slow_ptr.next
            slow_ptr.next = head1.head
            fast_ptr.next.next = head2.head
            

            
    
    def print_list(self):
        cur_node = self.head

        while cur_node.next!=self.head:
            print (cur_node.data)
            cur_node = cur_node.next
        print (cur_node.data)
        

head = cll()
head1 = cll()
head2 = cll()
head.push(9)
head.push(8)
head.push(7)
head.push(6)
head.push(5)
head.push(4)
head.push(3)
head.push(2)
head.push(1)

head.split(head1,head2)

head1.print_list()
print("second circular list")
head2.print_list()
