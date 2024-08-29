# from Utilities.HelperFunctions import isConsistent, union
import itertools

from DataStructures.Trees import *
from enfCheckers.conditions import (
    ruleFive,
    ruleFour,
    ruleOne,
    ruleSeven,
    ruleSix,
    ruleThree,
    ruleTwo,
)
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

# from DataStructures.Graphs import *
# from Utilities.TraverseGraph import *


# ex_a = BinaryConstraintTreeNode("x")
# ex_b = BinaryConstraintTreeNode("x")
# ex_c = BinaryConstraintTreeNode("y")
# ex_d = BinaryConstraintTreeNode("d")
# ex_e = BinaryConstraintTreeNode("e")

# ex_b.constraint = True

# test_data = [ex_a,ex_c,ex_d,ex_b,ex_e]
# test_data2 = [ex_a,ex_c,ex_d,ex_e]

# print(isConsistent(test_data))
# print(isConsistent(test_data2))
# print("The consistency is finished")
# print(isConsistent([]))
# print(isConsistent([ex_a]))
# g_exa = ConstraintGraphNode()
# g_exa.graphNodeType = GraphNodeType.START
# g_exb = ConstraintGraphNode()
# g_exa.next = g_exb
# g_exb.value = 'second'
# g_exc = ConstraintGraphNode()
# g_exc.value = 'third'
# g_exd = ConstraintGraphNode()
# g_exd.value = 'fourth'
# #g_exd.graphNodeType = GraphNodeType.INTERNAL
# g_exe = ConstraintGraphNode()
# g_exe.graphNodeType = GraphNodeType.STOP
# g_exe.value = 'fifth'
# g_exa.children.append(g_exb)
# g_exa.children.append(g_exc)
# g_exb.children.append(g_exe)
# #result = traverseGraph(g_exa,[],[])
# print("this is the result of the guard set")
# print(traverseGraph(g_exa,[],[]))
# print(union([1,2,3,4,5],[1,3,4,5,8,9]))
# print(union([],[]))
# selection_set = []
# start_node = ConstraintGraphNode()
# head_and = ConstraintGraphNode()
# start_node.graphNodeType = GraphNodeType.START
# head_and.graphNodeType = GraphNodeType.INTERNAL
# head_and.type = NodeType.AND
# c = ConstraintGraphNode()
# d = ConstraintGraphNode()
# stop_node = ConstraintGraphNode()
# stop_node.graphNodeType = GraphNodeType.STOP
# c.next = stop_node
# d.next = stop_node
# c.value = 'C'
# d.value = 'D'
# start_node.next = head_and
# head_and.guardSet.append(c)
# head_and.guardSet.append(d)

# traverseGraph(start_node,[],selection_set)
# print(selection_set)
# node_stop = ConstraintGraphNode()
# node_stop.graphNodeType = GraphNodeType.STOP

# node_internal_or = ConstraintGraphNode()
# node_internal_or.graphNodeType = GraphNodeType.INTERNAL
# node_internal_or.type = NodeType.OR
# node_internal_or.children = [node_stop, node_stop]

# node_internal_and = ConstraintGraphNode()
# node_internal_and.graphNodeType = GraphNodeType.INTERNAL
# node_internal_and.type = NodeType.AND
# node_internal_and.next = node_internal_or
# node_internal_and.guardSet = [1, 2]

# node_start = ConstraintGraphNode()
# node_start.graphNodeType = GraphNodeType.START
# node_start.next = node_internal_and

# incoming_set = []
# selection_sets = []

# traverseGraph(node_start, incoming_set, selection_sets)
# print(f"Final selection_sets: {selection_sets}")


# input = "&(B, !(|(C, |(A, &(!(B), |(K,X))))))"
# input = "&(B, !(|(C, |(A, &(&(B, &(C, D)), A)))))"
# input = "|(&(A, |(!(B), !(C))), D)"
# input = "&(A, &(B, &(C, &(|(A, |(B, |(C, A))), &(B, &(&(A, A), !(A)))))))"
# input = "|(&(A, B), |(C, D))"
# input = "|(a, |(b, |(c, |(d, c))))"
# input = "&(a, &(b, &(c, &(d,c))))"
# input = "&(a, &(b, &(c, &(d, !(b)))))"
# input = "&(a, a)"
# input = "!(!(a))"
# input = "|(|(!(a), &(a, &(b,c))), &(b, &(c, !(b))))"
# input = "|(a, a)"
# input = "|(a, |(b, |(c, |(d, !(c)))))"
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

    literals = dfs(cTree, [])

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
