from Utilities.BuildTree import *
from Utilities.HelperFunctions import print_constraint_tree, print_tree
from Utilities.PropagateTruthValue import propagateTruthValue
from Utilities.GatherJunctors import gatherJunctors
from Utilities.ReduceToElegance import (
    reduceToElegance,
    ReductionSignal,
    findAndRemoveChild,
)

from DataStructures.Trees import *
from Tests import *


# input = "&(B, !(|(C, |(A, &(!(B), A)))))"
# input = "&(B, !(|(C, |(A, &(!(B), |(K,X))))))"
# input = "&(B, !(|(C, |(A, &(&(B, &(C, D)), A)))))"
# input = "|(&(A, |(!(B), !(C))), D)"
# input = "&(A, &(B, &(C, &(|(A, |(B, |(C, A))), &(B, &(&(A, A), !(A)))))))"
# input = "|(&(A, B), |(C, D))"
input = "|(a, |(b, |(c, |(d, c))))"  # Failing test case.
input = "|(a, |(b, |(c, |(d, !(c)))))"  # Failing test case.
# input = "|(A, &(B, &(C, &(D, C))))"
# input = "|(&(A, B), |(A, C))"
# input = "|(A,B)"
# input = "&(&(A,B),|(C,D))"
# input = "|(|(!(A), &(A, &(B, C))), &(B, &(C, !(B))))"
# input = "|(|(!(A), &(A, &(B, C))), &(C, &(B, !(B))))"
# input = "!(&(|(a, b), &(c,d)))"
# input = "|(!(a), |(!(c), !(d)))"
# input = "!(&(|(a, b), &(c,d)))"
# input = "|(&(!(a), b), |(!(c), !(d)))"
# input = "|(g, &(a, &(b, &(|(!(c), |(!(d), e)), |(c, &(c, f))))))" # Example from Mosh's paper. Expected output: "|(g,&(a, &(b, &(c, |(!(d), e)))))"
# input = "|(g,&(a, &(b, &(c, |(!(d), e)))))" # Reduced form of the above expression from Mosh's paper.

tree = BuildTree(input)
# tree2 = BuildTree(input2)

root = BinaryExpressionTreeNode("Root")
root.type = NodeType.ROOT
root.right = tree

root2 = BinaryExpressionTreeNode("Root")
root2.type = NodeType.ROOT
# root2.right = tree2

binaryConstraintTree = propagateTruthValue(root)
# binaryConstraintTree2 = propagateTruthValue(root2)

constraintTree = TreeNode("ROOT")
constraintTree.type = NodeType.ROOT

# constraintTree2 = TreeNode("ROOT")
# constraintTree2.type = NodeType.ROOT


if binaryConstraintTree is not None:
    constraintTree = gatherJunctors(binaryConstraintTree, constraintTree)

# if binaryConstraintTree2 is not None:
#     constraintTree2 = gatherJunctors(binaryConstraintTree2, constraintTree2)
print("Constraint Tree Finished")

if constraintTree:
    print("constraint Tree before reduction")
    print_constraint_tree(constraintTree)

table1 = generateReducedTruthTable(constraintTree, collectLiterals(constraintTree))

lastAction = None
if constraintTree is not None:
    lastAction = reduceToElegance(constraintTree, constraintTree, [], [])

table2 = generateReducedTruthTable(constraintTree, collectLiterals(constraintTree))
# # If the last action returned is a DELETE, that means the whole tree is a contradiction. Will always return False
# # If the last action returned is a DISCONNECT, that means the whole tree is a tautology. Will always return True
# # If the last action returned is a KEEP, that means the algorithm tried to reduce the tree as much as possible

print("Last action after reduction: ", lastAction)

if constraintTree:
    print("constraint Tree after reduction")
    print_constraint_tree(constraintTree)

print("*" * 50)
print("Expression VS. Reduction Equivalence")
print("*" * 50)

is_equivalent, differences = compare_tables(table1, table2)

if is_equivalent:
    print("The truth tables are equivalent.")
else:
    print(
        "The truth tables are not equivalent. Found ", len(differences), " differences"
    )
    print("The Differences are:")
    for difference in differences:
        print(f"Index: {difference[0]}")
        print("Table 1:", difference[1])
        print("Table 2:", difference[2])

print("*" * 50)
