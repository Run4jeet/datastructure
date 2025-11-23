class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
            print(temp.data, end=" -> ")
            #print(temp.data, end=" -> ")
            temp = temp.next
        print("\n\n**** End ****")

    def append(self,value):
        new_node = Node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.length += 1


mylist = LinkedList(1)
mylist.append(2)
mylist.printlist()