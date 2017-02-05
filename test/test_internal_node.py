import unittest
from BPlusTree import InternalNode


class TestInternalNode(unittest.TestCase):
    def test_key_value_size(self):
        size = 10
        node = InternalNode(size)

        self.assertEqual(size, len(node.keys))
        self.assertEqual(size + 1, len(node.children))

    def test_full(self):
        size = 4
        node = InternalNode(size)

        cases = ['a', 'b']

        for case in cases:
            node.insert(None, case, None)
            self.assertFalse(node.full())

        node.insert(None, 'c', None)
        self.assertTrue(node.full())

    def test_next_child(self):
        size = 10
        node = InternalNode(size)

        node.record_index = 10
        node.keys = ['c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm']
        node.children = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Low Key Out-of-Range
        self.assertEqual(0, node.next_child("a"))

        # Smallest Key
        self.assertEqual(1, node.next_child("c"))

        # Middle Key - Exists
        self.assertEqual(6, node.next_child("i"))

        # Middle Key - Not Exists
        self.assertEqual(4, node.next_child("g"))

        # Largest Key
        self.assertEqual(10, node.next_child("m"))

        # High Key Out-of-Range
        self.assertEqual(10, node.next_child("p"))

    def test_insert(self):
        size = 3
        node = InternalNode(size)

        cases = [
            (3, 'c', 4, ['c', None, None], [3, 4, None, None]),
            (5, 'e', 6, ['c', 'e', None], [3, 5, 6, None]),
            (1, 'a', 2, ['a', 'c', 'e'], [1, 2, 5, 6])
        ]

        for case in cases:
            node.insert(case[0], case[1], case[2])
            self.assertEqual(node.keys, case[3])
            self.assertEqual(node.children, case[4])

    def test_split_odd(self):
        size = 5
        node = InternalNode(size)

        node.insert(1, 'a', 2)
        node.insert(2, 'b', 3)
        node.insert(3, 'c', 4)
        node.insert(4, 'd', 5)
        node.insert(5, 'e', 6)

        split_key, split_node = node.split()

        self.assertEqual(split_key, 'c')
        self.assertEqual(node.keys, ['a', 'b', None, None, None])
        self.assertEqual(node.children, [1, 2, 3, None, None, None])
        self.assertEqual(node.record_index, 1)

        self.assertEqual(split_node.keys, ['d', 'e', None, None, None])
        self.assertEqual(split_node.children, [4, 5, 6, None, None, None])
        self.assertEqual(split_node.record_index, 1)

    def test_split_even(self):
        size = 4
        node = InternalNode(size)

        node.insert(1, 'a', 2)
        node.insert(2, 'b', 3)
        node.insert(3, 'c', 4)
        node.insert(4, 'd', 5)

        split_key, split_node = node.split()

        self.assertEqual(split_key, 'c')
        self.assertEqual(node.keys, ['a', 'b', None, None])
        self.assertEqual(node.children, [1, 2, 3, None, None])
        self.assertEqual(node.record_index, 1)

        self.assertEqual(split_node.keys, ['d', None, None, None])
        self.assertEqual(split_node.children, [4, 5, None, None, None])
        self.assertEqual(split_node.record_index, 0)