import unittest
from BPlusTree import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_key_value_size(self):
        size = 10
        node = LeafNode(size)

        self.assertEqual(size, len(node.keys))
        self.assertEqual(size, len(node.records))

    def test_full(self):
        size = 4
        node = LeafNode(size)

        cases = ['a', 'b']

        for case in cases:
            node.insert(case, None)
            self.assertFalse(node.full())

        node.insert('c', None)
        self.assertTrue(node.full())

    def test_insert(self):
        size = 5
        node = LeafNode(size)

        cases = [
            ('c', 'Value C', ['c', None, None, None, None]),
            ('e', 'Value E', ['c', 'e', None, None, None]),
            ('g', 'Value G', ['c', 'e', 'g', None, None]),
            ('f', 'Value F', ['c', 'e', 'f', 'g', None]),
            ('a', 'Value A', ['a', 'c', 'e', 'f', 'g'])
        ]

        for case in cases:
            node.insert(case[0], case[1])
            self.assertEqual(node.keys, case[2])

    def test_split_odd(self):
        size = 5
        node = LeafNode(size)

        node.insert('a', 1)
        node.insert('b', 2)
        node.insert('c', 3)
        node.insert('d', 4)
        node.insert('e', 5)

        split_key, split_node = node.split()

        self.assertEqual(split_key, 'c')
        self.assertEqual(node.keys, ['a', 'b', None, None, None])
        self.assertEqual(len(node.records), 5)
        self.assertEqual(node.record_index, 1)

        self.assertEqual(split_node.keys, ['c', 'd', 'e', None, None])
        self.assertEqual(len(split_node.records), 5)
        self.assertEqual(split_node.record_index, 2)

    def test_split_even(self):
        size = 4
        node = LeafNode(size)

        node.insert('a', 1)
        node.insert('b', 2)
        node.insert('c', 3)
        node.insert('d', 4)

        split_key, split_node = node.split()

        self.assertEqual(split_key, 'c')
        self.assertEqual(node.keys, ['a', 'b', None, None])
        self.assertEqual(len(node.records), 4)
        self.assertEqual(node.record_index, 1)

        self.assertEqual(split_node.keys, ['c', 'd', None, None])
        self.assertEqual(len(split_node.records), 4)
        self.assertEqual(split_node.record_index, 1)