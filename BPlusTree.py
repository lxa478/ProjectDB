class Record(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{}:{}".format(self.key, self.value)


class InternalNode(object):
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.children = [None] * (size + 1)
        self.record_index = -1
        self.parent = None

    def full(self):
        return self.record_index + 1 == self.size - 1

    def next_child(self, key):
        # Binary search
        lo = 0
        hi = self.record_index

        while lo <= hi:
            mid = (lo + hi) // 2

            if key < self.keys[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return self.children[lo]

    def insert(self, node, split_key, split_node):
        # Add the new key-value to the next free spot
        self.record_index += 1
        self.keys[self.record_index] = split_key
        self.children[self.record_index + 1] = split_node

        # Shift the new key-value into sorted order
        i = self.record_index
        while i > 0 and self.keys[i] < self.keys[i - 1]:
            self.keys[i], self.keys[i - 1] = self.keys[i - 1], self.keys[i]
            self.children[i + 1], self.children[i] = self.children[i], self.children[i + 1]
            i -= 1

        self.children[i] = node

    def split(self):
        node = self.__class__(self.size)
        node.parent = self.parent

        # Partition records between the two nodes
        copy_position = self.size // 2
        for i in range(copy_position + 1, self.size):
            node.insert(self.children[i], self.keys[i], self.children[i + 1])

        # Store the split key before we remove it from the node
        split_key = self.keys[copy_position]

        # Remove records from node that were copied to the new node
        for i in range(copy_position, self.size):
            self.keys[i] = None
            self.children[i + 1] = None

        self.record_index = copy_position - 1

        return split_key, node


class LeafNode(object):
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.records = [None] * size
        self.next_leaf_node = None
        self.record_index = -1
        self.parent = None

    def full(self):
        return self.record_index + 1 == self.size - 1

    def find(self, key):
        # Binary search
        lo = 0
        hi = self.record_index

        while lo <= hi:
            mid = (lo + hi) // 2

            if key == self.keys[mid]:
                return self.records[mid]

            if key < self.keys[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return None

    def insert(self, key, value):
        # Add the new key-value to the next free spot
        self.record_index += 1
        self.keys[self.record_index] = key
        self.records[self.record_index] = value

        # Shift the new key-value into sorted order
        i = self.record_index
        while i > 0 and self.keys[i] < self.keys[i - 1]:
            self.keys[i], self.keys[i - 1] = self.keys[i - 1], self.keys[i]
            self.records[i], self.records[i - 1] = self.records[i - 1], self.records[i]
            i -= 1

    def split(self):
        # Create a new empty leaf node
        node = self.__class__(self.size)
        node.parent = self.parent

        # Update next_leaf_node pointers
        node.next_leaf_node = self.next_leaf_node
        self.next_leaf_node = node

        # Partition records between the two nodes
        copy_position = self.size // 2
        for i in range(copy_position, self.size):
            node.insert(self.keys[i], self.records[i])
            self.keys[i] = None
            self.records[i] = None

        self.record_index = copy_position - 1

        return node.keys[0], node


class BPlusTree(object):
    def __init__(self, size):
        self.size = size
        self.root = None

    def _find_leaf(self, key, root):
        node = root
        while type(node) is not LeafNode:
            node = node.next_child(key)

        return node

    def insert_in_parent(self, node, split_key, split_node):
        if node is self.root:
            internal_node = InternalNode(self.size)
            internal_node.insert(node, split_key, split_node)
            self.root = internal_node
            node.parent = internal_node
            split_node.parent = internal_node
        else:
            parent = node.parent

            if not parent.full():
                parent.insert(node, split_key, split_node)
            else:
                parent.insert(node, split_key, split_node)
                split_key, split_parent = parent.split()
                self.insert_in_parent(parent, split_key, split_parent)

    def __setitem__(self, key, value):
        self.set(key, value)

    def set(self, key, value):
        if not self.root:
            # If the tree is empty, create a new LeafNode and set it to root
            self.root = LeafNode(self.size)
            node = self.root
        else:
            # Find the LeafNode that should contain key
            node = self._find_leaf(key, self.root)

        if not node.full():
            # If the node has room, then insert the key-value pair
            node.insert(key, value)
        else:
            # If the node is full, insert then split
            node.insert(key, value)
            split_key, split_node = node.split()

            # Insert the nodes into parent internal nodes
            self.insert_in_parent(node, split_key, split_node)

    def __getitem__(self, key):
        record = self.get(key, default=None)

        if not record:
            raise KeyError(key)

        return record

    def get(self, key, default=None):
        leaf_node = self._find_leaf(key, self.root)
        record = leaf_node.find(key)

        if record:
            return record

        return default

    def __contains__(self, key):
        return self.contains(key)

    def contains(self, key):
        leaf_node = self._find_leaf(key, self.root)
        record = leaf_node.find(key)

        return record is not None

    def __delete__(self, key):
        self.delete(key)

    def delete(self, key):
        pass

    def keys(self):
        node = self.root
        while type(node) is not LeafNode:
            node = node.children[0]

        leaf = node
        while leaf:
            for key in leaf.keys:
                if key:
                    yield key
            leaf = leaf.next_leaf_node


    def items(self):
        node = self.root
        while type(node) is not LeafNode:
            node = node.children[0]

        leaf = node
        while leaf:
            for record in leaf.records:
                if record:
                 yield record
            leaf = leaf.next_leaf_node
