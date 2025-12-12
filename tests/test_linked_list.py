import unittest
from linkedlist.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList(10)
        self.ll.append(20)
        self.ll.append(30)

    def test_append(self):
        ll = LinkedList(10)
        ll.append(5)

        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.tail.value, 5)
        self.assertEqual(ll.head.value, 10)

    def test_pop(self):
        ll = LinkedList(10)
        ll.append(5)
        ll.pop()
        self.assertEqual(ll.length, 1)
        self.assertEqual(ll.tail.value, 10)
        #self.assertEqual(ll.length, 2)

    def test_prepend(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.prepend(5)
        self.assertEqual(ll.length,4)
        self.assertEqual(ll.head.value,5)

    def test_pop_first_with_one_element(self):
        ll = LinkedList(10)
        ll.pop_first()
        self.assertEqual(ll.length, 0)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_pop_first_with_multiple_elements(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.pop_first()
        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.head.value, 20)
       # self.assertEqual(ll.tail, None)

    def test_get(self):
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)

        self.assertEqual(self.ll.length, 4)
        self.assertEqual(self.ll.get(1).value,20)


    def test_set_value(self):
        self.ll.append(40)
        self.ll.set_value(1, 22)
        self.assertEqual(self.ll.length,4)
        self.ll.printlist()
        self.assertEqual(self.ll.get(1).value,22)

    def test_insert(self):
        #10->20->30
        self.ll.insert(0,5)
        self.assertEqual(self.ll.head.value,5)
        self.assertEqual(self.ll.tail.value,30)
        self.assertEqual(self.ll.insert(1,11),True)

    def test_remove(self):
        self.ll.remove(1)
        #self.ll.printlist()
        #print(self.ll)
        self.assertEqual(self.ll.length,2)
        # test remove first
        self.ll.remove(0)
        self.assertEqual(self.ll.head.value,30)

    def test_reverse(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.reverse()
        self.assertEqual(ll.head.value , 30)
        self.assertEqual(ll.tail.value,10)

if __name__ == '__main__':

    unittest.main()