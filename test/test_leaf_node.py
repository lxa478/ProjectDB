import unittest
from BPlusTree import LeafNode

class TestLeafNode(unittest.TestCase):
	
	def test_key_value_size(self):
		size = 10
		node = LeafNode(size)
		
		self.assertEqual(size, len(node.keys))
		self.assertEqual(size, len(node.records))
		
	def test_full(self):
		size = 3
		node = LeafNode(size)
		
		node.insert('a', 'a')	
		node.insert('b', 'b')
		self.assertFalse(node.full())
		
		node.insert('c', 'c')
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
		
		self.assertRaises(IndexError, node.insert, 'm', 'Value M')