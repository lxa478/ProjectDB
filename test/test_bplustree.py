import unittest
from BPlusTree import BPlusTree, LeafNode, InternalNode


class TestBPlusTree(unittest.TestCase):
    def test_set_item_2level(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A', ['a', None, None, None], LeafNode),
            ('b', 'Value B', ['a', 'b', None, None], LeafNode),
            ('c', 'Value C', ['a', 'b', 'c', None], LeafNode),
            ('d', 'Value D', ['c', None, None, None], InternalNode)
        ]

        for case in cases1:
            bptree[case[0]] = case[1]
            self.assertEqual(type(bptree.root), case[3])
            self.assertEqual(bptree.root.keys, case[2])

        self.assertEqual(bptree.root.children[0].keys, ['a', 'b', None, None])
        self.assertEqual(bptree.root.children[1].keys, ['c', 'd', None, None])

    def test_set_item_3level(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D'),
            ('e', 'Value E'),
            ('f', 'Value F'),
            ('g', 'Value G'),
            ('h', 'Value H'),
            ('i', 'Value I'),
            ('j', 'Value J')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        """
                            [0 g 1]
                               |
                        |------------|
                  0:[0 c 1 e 2] 1:[3 i 4]
                        |             |
            |-------|-------|       |-------|
        0:[a b] 1:[c d] 2:[e f] 3:[g h] 4:[i j]
        """

        self.assertEqual(bptree.root.keys, ['g', None, None, None])
        self.assertEqual(bptree.root.children[0].keys, ['c', 'e', None, None])
        self.assertEqual(bptree.root.children[1].keys, ['i', None, None, None])

        self.assertEqual(bptree.root.children[0].children[0].keys, ['a', 'b', None, None])
        self.assertEqual(bptree.root.children[0].children[1].keys, ['c', 'd', None, None])
        self.assertEqual(bptree.root.children[0].children[2].keys, ['e', 'f', None, None])

        self.assertEqual(bptree.root.children[1].children[0].keys, ['g', 'h', None, None])
        self.assertEqual(bptree.root.children[1].children[1].keys, ['i', 'j', None, None])

    def test_get_item(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        self.assertEqual(bptree['a'], 'Value A')
        self.assertEqual(bptree['b'], 'Value B')
        self.assertEqual(bptree['c'], 'Value C')
        self.assertEqual(bptree['d'], 'Value D')

        with self.assertRaises(KeyError) as context:
            x = bptree['e']

    def test_get_item_with_default(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        self.assertEqual(bptree.get('a'), 'Value A')
        self.assertEqual(bptree.get('b'), 'Value B')
        self.assertEqual(bptree.get('c'), 'Value C')
        self.assertEqual(bptree.get('d'), 'Value D')

        self.assertEqual(bptree.get('e'), None)
        self.assertEqual(bptree.get('f', 'DEFAULT VALUE'), 'DEFAULT VALUE')

    def test_contains(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        self.assertTrue('a' in bptree)
        self.assertTrue('b' in bptree)
        self.assertTrue('c' in bptree)
        self.assertTrue('d' in bptree)
        self.assertFalse('e' in bptree)

    def test_keys(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        keys = list(bptree.keys())
        self.assertEqual(keys, ['a', 'b', 'c', 'd'])

    def test_items(self):
        size = 4
        bptree = BPlusTree(size)

        cases1 = [
            ('a', 'Value A'),
            ('b', 'Value B'),
            ('c', 'Value C'),
            ('d', 'Value D')
        ]

        for case in cases1:
            bptree[case[0]] = case[1]

        keys = list(bptree.items())
        self.assertEqual(keys, ['Value A', 'Value B', 'Value C', 'Value D'])
