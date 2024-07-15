from Utilities.BuildTree import *
from Utilities.GatherJunctors import gatherJunctors
from Utilities.HelperFunctions import print_tree
from Utilities.PropagateTruthValue import propagateTruthValue
from Utilities.HelperFunctions import isConsistent
from DataStructures.Trees import *
ex_a = BinaryConstraintTreeNode("x")
ex_b = BinaryConstraintTreeNode("x")
ex_c = BinaryConstraintTreeNode("y")
ex_d = BinaryConstraintTreeNode("d")
ex_e = BinaryConstraintTreeNode("e")
ex_b.constraint = True

test_data = [ex_a,ex_c,ex_d,ex_b,ex_e]
test_data2 = [ex_a,ex_c,ex_d,ex_e]

print(isConsistent(test_data))
print(isConsistent(test_data2))
print("The consistency is finished")

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

print("GuardSet: ")
if constraintTree is not None and constraintTree.guardSet is not None:
    for gct in constraintTree.guardSet:
        print_tree(gct)
    print("Children: ", len(constraintTree.children))

    for bct in constraintTree.children:
        print_tree(bct)
