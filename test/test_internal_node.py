import unittest
from BPlusTree import InternalNode

class TestInternalNode(unittest.TestCase):
	
	def test_key_value_size(self):
		size = 10
		node = InternalNode(size)
		
		self.assertEqual(size, len(node.keys))
		self.assertEqual(size+1, len(node.children))
	
	def test_next_child(self):
		size = 10
		node = InternalNode(size)
		node.keys = ['c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm']
		node.children = [i for i in range(len(node.children))]
		
		# Low Key Out-of-Range
		self.assertEqual(0, node.next_child("a"))
		
		# Smallest Key
		self.assertEqual(0, node.next_child("c"))
		
		# Middle Key - Exists
		self.assertEqual(5, node.next_child("i"))
		
		# Middle Key - Not Exists
		self.assertEqual(4, node.next_child("g"))
		
		# Largest Key
		self.assertEqual(9, node.next_child("m"))
		
		# High Key Out-of-Range
		self.assertEqual(10, node.next_child("p"))