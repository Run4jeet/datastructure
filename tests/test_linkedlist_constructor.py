import os
from pathlib import Path
import importlib.util


def load_ll_module():
    # locate the LL-ConstructorTest2.py relative to this test file
    tests_dir = Path(__file__).resolve().parent
    module_path = (tests_dir.parent / "linkedlist" / "LL-ConstructorTest2.py").resolve()
    spec = importlib.util.spec_from_file_location("ll_module", str(module_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_constructor_append_pop():
    ll_mod = load_ll_module()
    LinkedList = ll_mod.LinkedList

    l = LinkedList(1)
    assert l.head is not None
    assert l.head.value == 1
    assert l.tail.value == 1
    assert l.length == 1

    l.append(2)
    assert l.tail.value == 2
    assert l.length == 2

    popped = l.pop()
    assert popped == 2
    assert l.length == 1


def test_prepend_get_set_insert_remove():
    ll_mod = load_ll_module()
    LinkedList = ll_mod.LinkedList

    l = LinkedList(10)
    l.append(20)
    l.prepend(5)
    assert l.head.value == 5
    assert l.get(1).value == 10

    assert l.set_value(1, 11) is True
    assert l.get(1).value == 11

    # insert in middle
    assert l.insert(2, 15) is True
    assert l.get(2).value == 15

    # remove the inserted node using remove_v1 (which returns the node)
    removed = l.remove_v1(2)
    # removed may be a Node instance; check value and length
    assert hasattr(removed, "value") and removed.value == 15
    assert l.length == 3


def test_kth_node_find_middle_and_has_loop():
    ll_mod = load_ll_module()
    LinkedList = ll_mod.LinkedList

    l = LinkedList(1)
    l.append(2)
    l.append(3)
    l.append(4)

    # kth_node(1) should return the last node (k offset from end)
    assert l.kth_node(1).value == 4

    # find middle for odd-length list [1,2,3,4,5]
    l2 = LinkedList(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)
    l2.append(5)
    assert l2.findMiddle() == 3

    # test has_loop: initially False
    assert l.has_loop() is False

    # create a simple loop: tail -> head
    l.tail.next = l.head
    assert l.has_loop() is True
