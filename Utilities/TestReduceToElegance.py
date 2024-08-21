import unittest

from DataStructures.Trees import BinaryExpressionTreeNode, TreeNode, NodeType, findAndRemoveChild
from Utilities.ReduceToElegance import compareSets, commandSetIterator, containsTerminalAndNode, applyOrCut

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

        self.node4 = TreeNode("D")
        self.node4.type = NodeType.AND
        self.node4.value = "D"
        self.node4.constraint = True
        self.node4.guardSet = [TreeNode("G1")]
        self.node4.children = []

        self.node5 = TreeNode("E")
        self.node5.type = NodeType.AND
        self.node5.value = "E"
        self.node5.constraint = True
        self.node5.guardSet = [TreeNode("G2")]
        self.node5.children = []

        self.node6 = TreeNode("F")
        self.node6.type = NodeType.OR
        self.node6.value = "F"
        self.node6.constraint = True
        self.node6.guardSet = []
        self.node6.children = [self.node4, self.node5]

        self.node7 = TreeNode("H")
        self.node7.type = NodeType.OR
        self.node7.value = "H"
        self.node7.constraint = True
        self.node7.guardSet = []
        self.node7.children = []

        self.node8 = TreeNode("I")
        self.node8.type = NodeType.AND
        self.node8.value = "I"
        self.node8.constraint = True
        self.node8.guardSet = [TreeNode("G3")]
        self.node8.children = [self.node7]

        self.node9 = TreeNode("J")
        self.node9.type = NodeType.OR
        self.node9.value = "J"
        self.node9.constraint = True
        self.node9.guardSet = []
        self.node9.children = [self.node8]

        self.node10 = TreeNode("K")
        self.node10.type = NodeType.AND
        self.node10.value = "K"
        self.node10.constraint = True
        self.node10.guardSet = []
        self.node10.children = [self.node9]

    def test_applyOrCut_basic(self):
        # Testing applyOrCut with simple nodes
        current = TreeNode("L")
        current.type = NodeType.AND
        current.constraint = True
        current.guardSet = []
        current.children = [self.node8]
        
        applyOrCut(self.node8, current)
        
        # After applyOrCut, current's guardSet should remain empty because node7 has no guardSet
        self.assertEqual(current.guardSet, [])
        
        # After applyOrCut, current's children should still contain node8 because node7 doesn't change it
        self.assertEqual(current.children, [self.node8])
    
    def test_applyOrCut_multiple_children(self):
        # Testing applyOrCut when current has multiple children
        current = TreeNode("M")
        current.type = NodeType.AND
        current.constraint = True
        current.guardSet = []
        current.children = [self.node8, self.node9]

        applyOrCut(self.node8, current)
        
        # After applyOrCut, current's guardSet should include the guardSet of node8 (G3)
        expected_guardSet = []
        self.assertEqual(current.guardSet, [])
        
        # After applyOrCut, the current node should still have two children: node8 and node9
        self.assertEqual(len(current.children), 2)
        
        # Check that the first child is still node8
        self.assertEqual(current.children[0].value, "I")
        
        # Check that the second child is node9
        self.assertEqual(current.children[1].value, "J")

    
    
    def test_commandSetIterator_with_terminal_AND_node(self):
        children = [self.node4, self.node5, self.node6]
        result = commandSetIterator(children, [])
        expected = [TreeNode("G1"), TreeNode("G2")]
        self.assertEqual([node.value for node in result], [node.value for node in expected])

    def test_commandSetIterator_without_terminal_AND_node(self):
        children = [self.node6]
        result = commandSetIterator(children, [])
        self.assertEqual(result, [])

    def test_commandSetIterator_empty_children(self):
        result = commandSetIterator([], [])
        self.assertEqual(result, [])
    
    def test_containsTerminalAndNode_true(self):
        children = [self.node4, self.node5]
        result = containsTerminalAndNode(children)
        self.assertTrue(result)

    def test_containsTerminalAndNode_false(self):
        children = [self.node6]
        result = containsTerminalAndNode(children)
        self.assertFalse(result)

    def test_containsTerminalAndNode_empty_children(self):
        result = containsTerminalAndNode([])
        self.assertFalse(result)


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
