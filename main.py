from Utilities.BuildTree import *
from Utilities.GatherJunctors import gatherJunctors
from Utilities.HelperFunctions import print_tree, print_constraint_tree
from Utilities.PropagateTruthValue import propagateTruthValue

# from Utilities.HelperFunctions import isConsistent, union
from DataStructures.Trees import *

# from DataStructures.Graphs import *
# from Utilities.TraverseGraph import *
from Utilities.ReduceToElegance import reduceToElegance

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
# input = "&(B, !(|(C, |(A, &(!(B), A)))))"
# input = "|(&(A, |(!(B), !(C))), D)"
# input = "&(A, &(B, &(C, &(|(A, |(B, |(C, A))), &(B, &(&(A, A), !(A)))))))"
# input = "!(&(A, B), &(A, B))"
# input = "|(A, |(B, |(C, |(D, C))))"
# input = "|(A, &(B, &(C, &(D, C))))"
# input = "|(&(A, B), |(A, C))"
input = "|(A,B)"
# input = "|(|(!(A), &(A, &(B, C))), &(B, &(C, !(B))))"
# input = "|(|(!(A), &(A, &(B, C))), &(C, &(B, !(B))))"

tree = BuildTree(input)
root = BinaryExpressionTreeNode("Root")
root.type = NodeType.ROOT
root.right = tree


print("Binary Expression Tree finished")
print_tree(root)

binaryConstraintTree = propagateTruthValue(root)
print("Binary Constraint Tree finished")
print_tree(binaryConstraintTree)

constraintTree = TreeNode("ROOT")
constraintTree.type = NodeType.ROOT

if binaryConstraintTree is not None:
    constraintTree = gatherJunctors(binaryConstraintTree, constraintTree)
print("Constraint Tree Finished")
print("Before Reduction")

if constraintTree:
    print_constraint_tree(constraintTree)
# print("GuardSet: ")
# if constraintTree is not None and constraintTree.guardSet is not None:
#     for gct in constraintTree.guardSet:
#         print_tree(gct)
#     if constraintTree.children:
#         print("Children: ", len(constraintTree.children))
#
#     if constraintTree.children is not None:
#         for bct in constraintTree.children:
#             print_tree(bct)


lastAction = reduceToElegance(constraintTree, [], [])
# If the last action returned is a DELETE, that means the whole tree is a contradiction. Will always return False
# If the last action returned is a DISCONNECT, that means the whole tree is a tautology. Will always return True
# If the last action returned is a KEEP, that means the algorithm tried to reduce the tree as much as possible
print("Last action after reduction: ", lastAction)
if constraintTree:
    print_constraint_tree(constraintTree)
# print("GuardSet: ")
# if constraintTree is not None and constraintTree.guardSet is not None:
#     for gct in constraintTree.guardSet:
#         print_tree(gct)
#     if constraintTree.children:
#         print("Children: ", len(constraintTree.children))
#
#     if constraintTree.children is not None:
#         for bct in constraintTree.children:
#             print_tree(bct)
