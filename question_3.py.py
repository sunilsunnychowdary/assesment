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
 
 
def mid(mylist):
    temp1= mylist.head
    length = 0
    while temp1:
        temp1 = temp1.next
        length = length + 1
 
    temp1 = mylist.head
    for i in range((length - 1)//2):
        temp1 = temp1.next
 
    if temp1:
        if length % 2 == 0:
            print('two middle elements found, {} and {}.'.format(temp1.data, temp1.next.data))
        else:
            print('The middle element is {}.'.format(temp1.data))
    else:
        print('The list is empty.')
 
 
linked_list = LinkedList()
 
data_list = input('enter the elements into linked list: ').split()
for i in data_list:
    linked_list.append(int(i))
 
mid(linked_list)