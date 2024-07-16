from Utilities.BuildTree import *
from Utilities.GatherJunctors import gatherJunctors
from Utilities.HelperFunctions import print_tree
from Utilities.PropagateTruthValue import propagateTruthValue
from Utilities.HelperFunctions import isConsistent,union
from DataStructures.Trees import *
from DataStructures.Graph import *
from Utilities.TraverseGraph import *
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
# g_exa = ConstraintGraphNode()
# g_exa.value = 'first'

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
start_node = ConstraintGraphNode()
head_or = ConstraintGraphNode()
start_node.graphNodeType = GraphNodeType.START
or_node = ConstraintGraphNode()
or_node.graphNodeType = GraphNodeType.INTERNAL
or_node.type = NodeType.OR
c = ConstraintGraphNode()
d = ConstraintGraphNode()
c.value = 'C'
d.value = 'D'
start_node.next = head_or
head_or.children.append(c)
head_or.children.append(d)
print(traverseGraph(start_node,[],[]))
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
