import unittest
import Tree

class TestTree(unittest.TestCase):
    def test_find(self):
        tree = Tree.Tree()
        tree.add(1)
        tree.add(2)
        tree.add(0)
        self.assertEqual(tree.find(1).data, 1)
        self.assertEqual(tree.find(2).data, 2)
        self.assertEqual(tree.find(0).data, 0)
        self.assertEqual(tree.find(3), None)