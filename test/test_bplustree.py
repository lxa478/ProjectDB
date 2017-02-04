import unittest
from BPlusTree import BPlusTree, LeafNode, InternalNode

class TestLeafNode(unittest.TestCase):
	
	def test_set_item(self):
		bptree = BPlusTree(4)
		
		bptree['a'] = 'Value A'
		self.assertEqual(type(bptree.root), LeafNode)
		self.assertEqual(bptree.root.keys[0], 'a')
		
		bptree['b'] = 'Value B'
		self.assertEqual(type(bptree.root), LeafNode)
		self.assertEqual(bptree.root.keys[1], 'b')
		
		bptree['c'] = 'Value C'
		self.assertEqual(type(bptree.root), LeafNode)
		self.assertEqual(bptree.root.keys[2], 'c')
		
		bptree['d'] = 'Value D'
		self.assertEqual(type(bptree.root), LeafNode)
		self.assertEqual(bptree.root.keys[3], 'd')
		
		bptree['e'] = 'Value E'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['f'] = 'Value F'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
		
		bptree['g'] = 'Value G'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
		
		bptree['h'] = 'Value H'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['i'] = 'Value I'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['j'] = 'Value J'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['k'] = 'Value K'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['l'] = 'Value L'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'c')
				
		bptree['m'] = 'Value M'
		self.assertEqual(type(bptree.root), InternalNode)
		self.assertEqual(bptree.root.keys[0], 'g')
		
		keys = []
		node = bptree.root.children[0].children[0]
		while node:
			for key in node.keys:
				if key:
					keys.append(key)
			
			node = node.next_leaf_node
		self.assertEqual(keys, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
		print(keys)
