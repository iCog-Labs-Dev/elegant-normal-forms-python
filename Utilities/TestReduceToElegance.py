import unittest

from DataStructures.Trees import BinaryExpressionTreeNode, TreeNode, NodeType, findAndRemoveChild
from Utilities.ReduceToElegance import compareSets

class TestReduceToElegance(unittest.TestCase):
    
    def setUp(self):
        # Sample TreeNodes for testing
        self.node1 = TreeNode("A")
        self.node1.type = NodeType.LITERAL
        self.node1.value = "A"
        self.node1.constraint = True
        self.node1.guardSet = []

        self.node2 = TreeNode("B")
        self.node2.type = NodeType.LITERAL
        self.node2.value = "B"
        self.node2.constraint = True
        self.node2.guardSet = []

        self.node3 = TreeNode("C")
        self.node3.type = NodeType.LITERAL
        self.node3.value = "C"
        self.node3.constraint = True
        self.node3.guardSet = []

    def test_compareSets_identical_sets(self):
        set1 = [self.node1, self.node2, self.node3]
        set2 = [self.node1, self.node2, self.node3]
        result = compareSets(set1, set2)
        self.assertTrue(result)

    def test_compareSets_different_sets(self):
        set1 = [self.node1, self.node2, self.node3]
        set2 = [self.node1, self.node3]
        result = compareSets(set1, set2)
        self.assertFalse(result)

    def test_compareSets_empty_sets(self):
        set1 = []
        set2 = []
        result = compareSets(set1, set2)
        self.assertTrue(result)

    def test_compareSets_different_length(self):
        set1 = [self.node1, self.node2]
        set2 = [self.node1, self.node2, self.node3]
        result = compareSets(set1, set2)
        self.assertFalse(result)

    def test_findAndRemoveChild_found(self):
        children = [self.node1, self.node2, self.node3]
        result = findAndRemoveChild(children, self.node2)
        expected = [self.node1, self.node3]
        self.assertEqual(result, expected)

    def test_findAndRemoveChild_not_found(self):
        children = [self.node1, self.node3]
        result = findAndRemoveChild(children, self.node2)
        self.assertEqual(set(result), set(children))

    def test_findAndRemoveChild_empty_list(self):
        children = []
        result = findAndRemoveChild(children, self.node2)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
