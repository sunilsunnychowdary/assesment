class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
 
    def append(self, data):
        if self.temp is None:
            self.head = Node(data)
            self.temp = self.head
        else:
            self.temp.next = Node(data)
            self.temp = self.temp.next
 
 
def find_length(mylist):
    temp1= mylist.head
    length = 0
    while temp1:
        temp1 = temp1.next
        length = length + 1
 
    print(length)
 
 
linked_list = LinkedList()
 
data_list = input('enter the elements into linked list: ').split()
for i in data_list:
    linked_list.append(int(i))
length=0
 
find_length(linked_list)
