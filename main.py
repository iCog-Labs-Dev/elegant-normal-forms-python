from Utilities.BuildTree import *
from Utilities.HelperFunctions import print_tree
from Utilities.PropagateTruthValue import propagateTruthValue

input = "&(B, !(|(C, |(A, &(!(B), A)))))"

tree = BuildTree(input)
root = BinaryExpressionTreeNode("Root")
root.type = NodeType.ROOT
root.right = tree

print("Binary Expression Tree finished")
print_tree(root)

constraintTree = propagateTruthValue(root)
print("Constraint Tree finished")
print_tree(constraintTree)
