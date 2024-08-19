import unittest
from DataStructures.Trees import TreeNode, NodeType

from Utilities.HelperFunctions import find_object, setDifference
from typing import List

class TestHelperFunctions(unittest.TestCase):

    def test_find_object_true(self):
        # Create a list of TreeNode objects
        node1 = TreeNode("A")
        node1.type = NodeType.LITERAL
        node1.constraint = True

        node2 = TreeNode("B")
        node2.type = NodeType.LITERAL
        node2.constraint = False

        node3 = TreeNode("C")
        node3.type = NodeType.LITERAL
        node3.constraint = True

        objs_list = [node1, node2, node3]

        # Create the instance to search for (this should be found in the list)
        search_instance = TreeNode("B")
        search_instance.type = NodeType.LITERAL
        search_instance.constraint = False

        # Call the function and check if it returns True
        self.assertTrue(find_object(objs_list, search_instance))

    def test_find_object_false(self):
        # Create a list of TreeNode objects
        node1 = TreeNode("A")
        node1.type = NodeType.LITERAL
        node1.constraint = True

        node2 = TreeNode("B")
        node2.type = NodeType.LITERAL
        node2.constraint = False

        node3 = TreeNode("C")
        node3.type = NodeType.LITERAL
        node3.constraint = True

        objs_list = [node1, node2, node3]

        # Create the instance to search for (this should NOT be found in the list)
        search_instance = TreeNode("D")
        search_instance.type = NodeType.LITERAL
        search_instance.constraint = False

        # Call the function and check if it returns False
        self.assertFalse(find_object(objs_list, search_instance))

    def test_set_difference_empty_list(self):
        # Create an empty list1 and a list2 with some TreeNode objects
        list1 = []
        
        node1 = TreeNode("A")
        node1.type = NodeType.LITERAL
        node1.constraint = True

        node2 = TreeNode("B")
        node2.type = NodeType.LITERAL
        node2.constraint = False

        list2 = [node1, node2]

        # Call the function and check if it returns an empty list
        result = setDifference(list1, list2)
        self.assertEqual(result, [])

    def test_set_difference_existing_element(self):
        # Create a list1 and list2 with TreeNode objects
        node1 = TreeNode("A")
        node1.type = NodeType.LITERAL
        node1.constraint = True

        node2 = TreeNode("B")
        node2.type = NodeType.LITERAL
        node2.constraint = False

        node3 = TreeNode("C")
        node3.type = NodeType.LITERAL
        node3.constraint = True

        list1 = [node1, node2, node3]

        # Create list2 with an element that also exists in list1
        node4 = TreeNode("B")
        node4.type = NodeType.LITERAL
        node4.constraint = False

        list2 = [node4]

        # Call the function and check if it returns the correct set difference
        result = setDifference(list1, list2)
        expected_result = [node1, node3]  # node2 ("B") should be removed from list1

        self.assertEqual(result, expected_result)
    def test_set_difference_all_existing_element(self):
        # Create a list1 and list2 with TreeNode objects
        node1 = TreeNode("A")
        node1.type = NodeType.LITERAL
        node1.constraint = True

        node2 = TreeNode("B")
        node2.type = NodeType.LITERAL
        node2.constraint = False


        list1 = [node1, node2]

        # Create list2 with an element that also exists in list1
        node3 = TreeNode("A")
        node3.type = NodeType.LITERAL
        node3.constraint = True

        node4 = TreeNode("B")
        node4.type = NodeType.LITERAL
        node4.constraint = False

        list2 = [node3, node4]

        # Call the function and check if it returns the correct set difference
        result = setDifference(list1, list2)
        expected_result = []  # 

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
