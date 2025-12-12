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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length ==0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head =new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length ==0:
            self.tail = None
        return temp.value

    def get_v1(self,index):
        if index < 1 and index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_v1(self, index,value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return True

    def set_value(self,index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_v1(self,index,value):
        # 10 ->20 ->30

        new_node = Node(value)
        if index ==0:
            self.prepend(value)
            self.length +=1
            return True
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.get(index - 1)
            after = temp.next
            temp.next = new_node
            new_node.next = after
        self.length += 1
        return True

    def insert(self,index, value):
        if index < 0 or index >=self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index== self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True

    def remove_v1(self,index):
        #10->20->30->40>
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        pre = self.head
        for i in range(index):
            pre = temp
            temp = temp.next

        if self.length ==0:
            self.head = None
            self.tail = Node

        if index == 0:
            self.head = temp.next
            temp.next = None
            return temp
        if index == self.length-1:
            self.tail = pre
            pre.next = None
            temp.next = None
            return temp

        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for i in range( self.length):
            #before = temp
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next= None
        self.length -= 1
        return temp


    def reverse_v1(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        #while temp.next:
        for i in range(self.length):
            after = temp.next
            temp.next =before
            before = temp
            temp = after











###### test the method here #####
mylist = LinkedList(10)
mylist.append(20)
mylist.append(30)
mylist.printlist()
mylist.reverse()
#mylist.reverse_v1()
print("after reverse:\n")
mylist.printlist()

#mylist.prepend(5)
#mylist.printlist()
#print("test remove at index 1")
#mylist.remove(2)
#mylist.printlist()
#mylist.insert(1,22)
#mylist.set_v1(4,11)
#print("get 0", mylist.get(4))
#mylist.printlist()
#mylist.pop_first()
#print("after pop first \n",mylist.pop_first())
