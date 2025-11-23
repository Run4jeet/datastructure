class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            if __name__ == "__main__":
                myList = LinkedList(5)
                myList.append(10)
                myList.append(15)
                myList.append(20)
                myList.append(30)
                myList.append(50)
                #myList.tail.next = myList.head


                #my_linked_list_1 = LinkedList(1)
                #my_linked_list_1.append(2)
                #my_linked_list_1.append(3)
                #my_linked_list_1.append(4)
                #my_linked_list_1.tail.next = my_linked_list_1.head
                #print(my_linked_list_1.has_loop() )


                print("**** My List ****")
                myList.printList()
                #print(myList.printList(), end=" ")

                ######## Find Kth Node from end ###########
                print("\n ### Find Kth Node ### ")
                print(myList.kth_node(1).value)

                ######## Find Loop ###########
                #print("\n ### Find Loop ### ")
                #print(myList.has_loop())


                ######## Find Midde ###########
                #print("\n ### Find Midde ### ")
                #print(myList.findMiddle())


                ######## REVerse ###########
                #print("\n reverse  ")
                #myList.reverse_v1()
                #myList.printList()


                ######## REMOVE ###########
                #print("\n reomve index 2  ")
                #myList.remove_v1(3)
                #myList.printList()



                ######## INSERT ###########
                #print("\n insert index 2 value 1 ")
                #myList.insert(3,22)
                #myList.printList()


                ######## SET ###########
                #print("\n set index 2 value 22 ")
                #myList.set_value(0,22)
                #myList.printList()

                ######## GET ##############
                #print("Get index 1 -> ",myList.get(3))

                #### after pop first #########
                #myList.popFirst()
                #myList.printList()

                # 2 Items - Returns 2 Node
                #print(myList.pop())
                # 1 Item - Returns 1 Node
                #print(myList.pop())
                # 0 Item - Returns None 
                #print(myList.pop())
        return False
    ### my version
    def insert_v1(self,index,value):
        if(index <0 and index >= self.length):
            return None
        temp = self.get(index -1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

        self.length +=1

    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    ### my remove function
    def remove_v1( self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.popFirst(index)
        if index == self.length:
            return self.pop(index)
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp


 ### my revers function
    def reverse_v1(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        next = temp.next
        prev = None
       

        for _ in range(self.length):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

    # My middle Function
    def findMiddle(self):
        slow = self.head
        fast = self.head
         # while fast is not None and fast.next is not None  : 
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow.value
    
    ## My Has Loop Function ##
    def has_loop_v1(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            return False

    ####### Has Loop ##########
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    ###### Kth Node from the end ####
    def kth_node(self,k):
        slow = self.head
        fast = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow

        


    

myList = LinkedList(5)
# myList.append(10)
# myList.append(15)
# myList.append(20)
# myList.append(30)
# myList.append(50)
#myList.tail.next = myList.head


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
#my_linked_list_1.append(3)
#my_linked_list_1.append(4)
#my_linked_list_1.tail.next = my_linked_list_1.head
#print(my_linked_list_1.has_loop() )



print("**** My List ****")
myList.printList()
#print(myList.printList(), end=" ")

######## Find Kth Node from end ###########
print("\n ### Find Kth Node ### ")
print(myList.kth_node(1).value)

######## Find Loop ###########
#print("\n ### Find Loop ### ")
#print(myList.has_loop())


######## Find Midde ###########
#print("\n ### Find Midde ### ")
#print(myList.findMiddle())



######## REVerse ###########
#print("\n reverse  ")
#myList.reverse_v1()
#myList.printList()


######## REMOVE ###########
#print("\n reomve index 2  ")
#myList.remove_v1(3)
#myList.printList()




######## INSERT ###########
#print("\n insert index 2 value 1 ")
#myList.insert(3,22)
#myList.printList()


######## SET ###########
#print("\n set index 2 value 22 ")
#myList.set_value(0,22)
#myList.printList()

######## GET ##############
#print("Get index 1 -> ",myList.get(3))

#### after pop first #########
#myList.popFirst()
#myList.printList()

# 2 Items - Returns 2 Node
#print(myList.pop())
# 1 Item - Returns 1 Node
#print(myList.pop())
# 0 Item - Returns None 
#print(myList.pop())


