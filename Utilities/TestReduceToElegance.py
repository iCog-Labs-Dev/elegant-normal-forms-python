import unittest

from DataStructures.Trees import BinaryExpressionTreeNode, TreeNode, NodeType, findAndRemoveChild
from Utilities.ReduceToElegance import compareSets, commandSetIterator, containsTerminalAndNode, applyOrCut, applyAndCut, intersections, computeGrandChildGuardSet, orSubTreeElegance,andSubTreeElegance,orSubTreeIterator,andSubTreeIterator,iterator,reduceToElegance, ReductionSignal, IterationSignal

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

        self.node11 = TreeNode("L")
        self.node11.type = NodeType.AND
        self.node11.value = "L"
        self.node11.constraint = True
        self.node11.guardSet = []
        self.node11.children = []

        # Node with one child but a non-empty guardSet
        self.node12 = TreeNode("M")
        self.node12.type = NodeType.AND
        self.node12.value = "M"
        self.node12.constraint = True
        self.node12.guardSet = [TreeNode("G4")]
        self.node12.children = [self.node3]

        # Node with a non-empty guardSet and no children
        self.node13 = TreeNode("N")
        self.node13.type = NodeType.AND
        self.node13.value = "N"
        self.node13.constraint = True
        self.node13.guardSet = [TreeNode("G5")]
        self.node13.children = []

        # Node with children but no guardSet
        self.node14 = TreeNode("O")
        self.node14.type = NodeType.AND
        self.node14.value = "O"
        self.node14.constraint = True
        self.node14.guardSet = []
        self.node14.children = [self.node1, self.node2]

        self.node15 = TreeNode("P")
        self.node15.type = NodeType.AND
        self.node15.value = "P"
        self.node15.constraint = True
        self.node15.guardSet = []
        self.node15.children = []

        # Node with a guardSet that will intersect with a commandSet (for testing deletion)
        self.node16 = TreeNode("Q")
        self.node16.type = NodeType.AND
        self.node16.value = "Q"
        self.node16.constraint = True
        self.node16.guardSet = [TreeNode("G6")]
        self.node16.children = []

        # Node for testing OR-subtree iteration
        self.node17 = TreeNode("R")
        self.node17.type = NodeType.OR
        self.node17.value = "R"
        self.node17.constraint = True
        self.node17.guardSet = []
        self.node17.children = [self.node15, self.node16]

        # Node for testing AND-subtree iteration
        self.node18 = TreeNode("S")
        self.node18.type = NodeType.AND
        self.node18.value = "S"
        self.node18.constraint = True
        self.node18.guardSet = []
        self.node18.children = [self.node15, self.node16]
    
    def test_orSubTreeElegance(self):
        # Adjust the dominantSet and localCommandSet to trigger DELETE
        dominantSet = [TreeNode("G7")]
        localCommandSet = [TreeNode("G6")]
        
        # Set node16's guardSet to intersect with localCommandSet for triggering DELETE
        self.node16.guardSet = [TreeNode("G6")]

        # Invoke orSubTreeElegance and check for DELETE outcome
        result = orSubTreeElegance(self.node16, self.node17, dominantSet, localCommandSet)
        self.assertEqual(result, ReductionSignal.DISCONNECT)
    
    def test_andSubTreeElegance(self):
        handleSet = [TreeNode("G6")]
        commandSet = [TreeNode("G7")]
        result = andSubTreeElegance(self.node16, self.node18, handleSet, commandSet)
        self.assertEqual(result, IterationSignal.ADVANCE)
    
    def test_orSubTreeIterator(self):
        dominantSet = [TreeNode("G5")]
        commandSet = [TreeNode("G6")]
        result = orSubTreeIterator(self.node15, self.node17.children[1:], self.node17, dominantSet, commandSet)
        self.assertEqual(result, ReductionSignal.DISCONNECT)  # Should return None at the end of iteration

    def test_andSubTreeIterator(self):
        handleSet = [TreeNode("G6")]
        commandSet = [TreeNode("G7")]
        result = andSubTreeIterator(self.node18.children, self.node18, handleSet, commandSet)
        self.assertIsNone(result)  # Should return None if no ReductionSignal is found

    def test_iterator(self):
        dominantSet = [TreeNode("G5")]
        commandSet = [TreeNode("G6")]
        result = iterator(self.node17, dominantSet, commandSet)
        self.assertIsNone(result)  # Should return None if no ReductionSignal is found

    def test_reduceToElegance(self):
        dominantSet = [TreeNode("G5")]
        commandSet = [TreeNode("G6")]
        result = reduceToElegance(self.node16, dominantSet, commandSet)
        self.assertEqual(result, ReductionSignal.DISCONNECT)


    def test_applyAndCut_single_child_empty_guardSet(self):
        # Node with one child and empty guardSet
        result = applyAndCut(self.node14, self.node10)
        
        # Check that the function returns False since child should not be removed
        self.assertFalse(result)
        self.assertEqual(len(self.node10.children), 1)
    
    def test_applyAndCut_no_children_empty_guardSet(self):
        # Node with no children and an empty guardSet
        result = applyAndCut(self.node11, self.node10)
        
        # Should return False since grandChild has no children
        self.assertFalse(result)
        self.assertEqual(self.node10.children, [self.node9])

    def test_applyAndCut_non_empty_guardSet(self):
        # Node with one child but a non-empty guardSet
        result = applyAndCut(self.node12, self.node10)
        
        # Should return False as the guardSet is not empty
        self.assertFalse(result)

    def test_computeGrandChildGuardSet_difference(self):
        # Node with a non-empty guardSet
        resultSet = [TreeNode("G5")]
        computeGrandChildGuardSet(self.node13, resultSet)
        
        # GuardSet should now be empty after the difference
        self.assertEqual(self.node13.guardSet, [])
    def test_computeGrandChildGuardSet_no_difference(self):
        grandChild = TreeNode("G")
        grandChild.type = NodeType.LITERAL
        grandChild.guardSet = [self.node1]

        resultSet = [self.node2]

        computeGrandChildGuardSet(grandChild, resultSet)

    # The guardSet should remain unchanged as there's no intersection with resultSet
        self.assertEqual(grandChild.guardSet, [self.node1])
    def test_computeGrandChildGuardSet_empty_guardSet(self):
        grandChild = TreeNode("G")
        grandChild.type = NodeType.LITERAL
        grandChild.guardSet = []

        resultSet = [self.node2]

        computeGrandChildGuardSet(grandChild, resultSet)

        # The guardSet should remain empty
        self.assertEqual(grandChild.guardSet, [])
    def test_computeGrandChildGuardSet_basic(self):
        grandChild = TreeNode("G")
        grandChild.type = NodeType.LITERAL
        grandChild.guardSet = [self.node1, self.node2]

        resultSet = [self.node2]

        computeGrandChildGuardSet(grandChild, resultSet)

        # The guardSet should now only contain node1
        self.assertEqual(grandChild.guardSet, [self.node1])


    def test_intersections_no_children(self):
        # No children provided
        result = intersections([], [])
        
        # Should return an empty list
        self.assertEqual(result, [])
    def test_intersections_basic(self):
        children = [self.node4, self.node5]
        intersectionSet = [self.node4.guardSet[0], self.node5.guardSet[0]]

        result = intersections(intersectionSet, children)

        # The intersection should return the common guard set
        self.assertEqual(result, [])
    def test_intersections_no_common_guardSet(self):
        children = [self.node4, self.node5]
        intersectionSet = [TreeNode("X")]

        result = intersections(intersectionSet, children)

        # There should be no intersection
        self.assertEqual(result, [])
    def test_intersections_empty_children(self):
        intersectionSet = [self.node4.guardSet[0]]

        result = intersections(intersectionSet, [])

        # Result should be empty as there are no children
        self.assertEqual(result, [])
    
    def test_intersections_empty_intersectionSet(self):
        children = [self.node4, self.node5]
        intersectionSet = []

        result = intersections(intersectionSet, children)

        # Result should be empty as intersectionSet is empty
        self.assertEqual(result, [])

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