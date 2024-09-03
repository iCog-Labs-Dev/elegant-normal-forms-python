from DataStructures.Trees import TreeNode, BinaryExpressionTreeNode, NodeType
from Utilities.BuildTree import BuildTree
from Utilities.HelperFunctions import print_constraint_tree
from Utilities.PropagateTruthValue import propagateTruthValue
from Utilities.GatherJunctors import gatherJunctors
from Utilities.ReduceToElegance import reduceToElegance


from Tests.TestHelpers import collectLiterals, generateReducedTruthTable, compare_tables
from Tests.EnfRuleCheckers import (
    ruleOne,
    ruleTwo,
    ruleThree,
    ruleFour,
    ruleFive,
    ruleSix,
    ruleSeven,
)

from Tests.ReduceToEleganceTests import *
from Tests.GeneralTestCases import EXPRESSIONS

input = EXPRESSIONS[0]
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
    match lastAction:
        case ReductionSignal.DELETE:
            constraintTree.children = []
            constraintTree.guardSet = []

        case ReductionSignal.DISCONNECT:
            constraintTree.children = []
            constraintTree.guardSet = []

table2 = generateReducedTruthTable(constraintTree, collectLiterals(constraintTree))
# # If the last action returned is a DELETE, that means the whole tree is a contradiction. Will always return False
# # If the last action returned is a DISCONNECT, that means the whole tree is a tautology. Will always return True
# # If the last action returned is a KEEP, that means the algorithm tried to reduce the tree as much as possible

print("Last action after reduction: ", lastAction)


if constraintTree:
    print("constraint Tree after reduction")
    print_constraint_tree(constraintTree)
    # check if the enf conditions hold
    rules = [
        ruleOne,
        ruleTwo,
        ruleThree,
        ruleFour,
        ruleFive,
        ruleSix,
        ruleSeven,
    ]

    try:
        for rule in rules:
            if not rule(constraintTree):
                raise Exception(f"{rule.__name__} failed")
        print("ENF conditions passed")
    except Exception as e:
        print("ENF conditions failed:", e)


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
