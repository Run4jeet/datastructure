from linkedlist.node import Node

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        print("**** My List ****\n")
        while temp:
            print(temp.value, end=" -> ")
            #print(temp.data, end=" -> ")
            temp = temp.next
        print("\n\n**** End ****")

    def append_v2(self,value):
        new_node = Node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.length += 1

    def append(self,value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1




mylist = LinkedList(1)
mylist.append(2)
mylist.printlist()