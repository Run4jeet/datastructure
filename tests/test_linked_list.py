import unittest
from linkedlist.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList(10)
        ll.append(5)

        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.tail.value, 5)
        self.assertEqual(ll.head.value, 10)

if __name__ == '__main__':
    unittest.main()