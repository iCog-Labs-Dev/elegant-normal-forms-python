from Utilities.BuildTree import *
from Utilities.GatherJunctors import gatherJunctors
from Utilities.HelperFunctions import print_tree
from Utilities.PropagateTruthValue import propagateTruthValue

input = "&(B, !(|(C, |(A, &(!(B), A)))))"

tree = BuildTree(input)
root = BinaryExpressionTreeNode("Root")
root.type = NodeType.ROOT
root.right = tree

print("Binary Expression Tree finished")
print_tree(root)

binaryConstraintTree = propagateTruthValue(root)
print("Binary Constraint Tree finished")
print_tree(binaryConstraintTree)

constraintTree = ConstraintTreeNode("ROOT")
constraintTree.type = NodeType.ROOT

if binaryConstraintTree is not None:
    constraintTree = gatherJunctors(binaryConstraintTree, constraintTree)
print("Constraint Tree Finished")

print("GuardSet: ", constraintTree.guardSet)
print("Children: ", len(constraintTree.children))

for bct in constraintTree.children:
    print_tree(bct)
