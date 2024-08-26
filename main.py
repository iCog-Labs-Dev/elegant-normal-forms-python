from Utilities.BuildTree import *
from Utilities.GatherJunctors import gatherJunctors
from Utilities.HelperFunctions import print_tree, print_constraint_tree,intersection
from Utilities.PropagateTruthValue import propagateTruthValue

# from Utilities.HelperFunctions import isConsistent, union
from DataStructures.Trees import *

# from DataStructures.Graphs import *
# from Utilities.TraverseGraph import *
from Utilities.ReduceToElegance import reduceToElegance,orSubTreeElegance,andSubTreeElegance,orSubTreeIterator,andSubTreeIterator,iterator

import itertools

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

input = "&(B, !(|(C, |(A, &(!(B), A)))))"
# input = "&(B, !(|(C, |(A, &(!(B), |(K,X))))))"
# input = "&(B, !(|(C, |(A, &(&(B, &(C, D)), A)))))"
# input = "|(&(A, |(!(B), !(C))), D)"
# input = "&(A, &(B, &(C, &(|(A, |(B, |(C, A))), &(B, &(&(A, A), !(A)))))))"
# input = "|(&(A, B), |(C, D))"
# input = "|(A, |(B, |(C, |(D, C))))"
# input = "|(A, &(B, &(C, &(D, C))))"
# input = "|(&(A, B), |(A, C))"
# input = "|(A,B)"
# input = "&(&(A,B),|(C,D))"
# input = "|(|(!(A), &(A, &(B, C))), &(B, &(C, !(B))))"
# input = "|(|(!(A), &(A, &(B, C))), &(C, &(B, !(B))))"
input = "|(&(A, B), |(&(A, C), &(A, D)))"

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

print('*'*50)

def generateTruthTableValues(literals):
    combinations = list (itertools.product([True, False], repeat=len(literals)))

    result = []
    for combination in combinations:
        result.append(dict(zip(literals,combination)))
    
    return result

# print(generateTruthTableValues(['A', 'B', 'C', 'D', 'E']))
# print(len(generateTruthTableValues(['A', 'B', 'C', 'D', 'E'])))

# truthValues = {
#     'A': True,
#     'B': True,
#     'C': False,
#     'D': False,
# }

def evaluateBinaryExpressionTreeNode(currentNode, truthValues):
    match currentNode.type:
        case NodeType.NOT:
            if currentNode.right is not None:
                return (not evaluateBinaryExpressionTreeNode(currentNode.right, truthValues))
        case NodeType.AND:
            if currentNode.left is not None and currentNode.right is not None:
                return (
                    evaluateBinaryExpressionTreeNode(currentNode.left, truthValues) and evaluateBinaryExpressionTreeNode(currentNode.right, truthValues)
                )
        case NodeType.OR:
            if currentNode.left is not None and currentNode.right is not None:
                return (
                    evaluateBinaryExpressionTreeNode(currentNode.left, truthValues) or evaluateBinaryExpressionTreeNode(currentNode.right, truthValues)
                )
        case NodeType.LITERAL:
            if currentNode.value is not None and currentNode.value in truthValues:
                return truthValues[currentNode.value]

# res = evaluateBinaryExpressionTreeNode(tree, truthValues)
# print(res)

def evaluateReducedConstraintTree(constraintTree, truthValues):
    truthValue = None
    match constraintTree.type:
        case NodeType.AND:
            if constraintTree.guardSet == [] and constraintTree.children == []:
                return True
            if constraintTree.guardSet != []:
                for literal in constraintTree.guardSet:
                    if literal.value is not None and literal.value in truthValues:
                        literalTruthValue = truthValues[literal.value]

                        if literal.constraint == False:
                            literalTruthValue = not literalTruthValue
                        
                        if truthValue is None:
                            truthValue = literalTruthValue
                        else:
                            truthValue = truthValue and literalTruthValue

            if constraintTree.children != []:
                for orNode in constraintTree.children:
                    if truthValue is None:
                        truthValue = evaluateReducedConstraintTree(orNode, truthValues)
                    else:
                        truthValue = truthValue and evaluateReducedConstraintTree(orNode, truthValues)
            return truthValue
        case NodeType.OR:
            for andNode in constraintTree.children:
                if truthValue is None:
                    truthValue = evaluateReducedConstraintTree(andNode, truthValues)
                else:
                    truthValue = truthValue or evaluateReducedConstraintTree(andNode, truthValues)
            return truthValue

# val = evaluateReducedConstraintTree(constraintTree, truthValues)
# print(val)

# truthTable = [
#     (
#         truthValues,
#         outcome
#     )
# ]
def generateExpressionTruthTable(literals):
    truthTable = []
    for generatedTruthValues in generateTruthTableValues(literals):
        outcome = evaluateBinaryExpressionTreeNode(tree, generatedTruthValues)
        truthTable.append((generatedTruthValues, outcome))
    return truthTable

# print(generateExpressionTruthTable(['A', 'B']))
print(generateExpressionTruthTable(['A', 'B', 'C']))
# print(generateExpressionTruthTable(['A', 'B', 'C', 'D']))

def generateReducedTruthTable(literals):
    reducedTruthTable = []
    for generatedTruthValues in generateTruthTableValues(literals):
        outcome = evaluateReducedConstraintTree(constraintTree, generatedTruthValues)
        reducedTruthTable.append((generatedTruthValues, outcome))
    return reducedTruthTable

# print(generateReducedTruthTable(['A', 'B']))
print(generateReducedTruthTable(['A', 'B', 'C']))
# print(generateReducedTruthTable(['A', 'B', 'C', 'D']))


# dominantSet = [TreeNode("G7")]
# localCommandSet = [TreeNode("G6")]

# node15 = TreeNode("P")
# node15.type = NodeType.AND
# node15.value = "P"
# node15.constraint = True
# node15.guardSet = []
# node15.children = []

# node16 = TreeNode("Q")
# node16.type = NodeType.AND
# node16.value = "Q"
# node16.constraint = True
# node16.guardSet = [TreeNode("G6")]
# node16.children = []
#         # Set node16's guardSet to intersect with localCommandSet for triggering DELETE
# node17 = TreeNode("R")
# node17.type = NodeType.OR
# node17.value = "R"
# node17.constraint = True
# node17.guardSet = []
# node17.children = [node15, node16]

# node18 = TreeNode("S")
# node18.type = NodeType.AND
# node18.value = "S"
# node18.constraint = True
# node18.guardSet = []
# node18.children = [node15, node16]

#         # Invoke orSubTreeElegance and check for DELETE outcome
# result = orSubTreeElegance(node16, node17, dominantSet, localCommandSet)
# print("or subtree elegance result")
# print(result)

# handleSet = [TreeNode("G6")]
# commandSet = [TreeNode("G7")]

# result = andSubTreeElegance(node16, node18, handleSet, commandSet)
# print("andSubTreeElegance result")
# print(result)

# dominantSet = [TreeNode("G5")]
# commandSet = [TreeNode("G6")]
# result = orSubTreeIterator(node15, node17.children[1:], node17, dominantSet, commandSet)
# print("orSubTreeIterator result")
# print(result)

# handleSet = [TreeNode("G6")]
# commandSet = [TreeNode("G7")]
# result = andSubTreeIterator(node18.children, node18, handleSet, commandSet)
# print("andSubTreeIterator result")
# print(result)

# dominantSet = [TreeNode("G5")]
# commandSet = [TreeNode("G6")]
# result = iterator(node17, dominantSet, commandSet)
# print("iterator result")
# print(result)

# dominantSet = [TreeNode("G5")]
# commandSet = [TreeNode("G6")]
# result = reduceToElegance(node16, dominantSet, commandSet)
# print("reduceToElegance result")

# print(result)
