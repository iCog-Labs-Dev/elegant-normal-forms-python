import itertools

from Utilities.BuildTree import *
from Utilities.HelperFunctions import print_constraint_tree, print_tree
from Utilities.PropagateTruthValue import propagateTruthValue
from Utilities.ReduceToElegance import reduceToElegance, ReductionSignal, findAndRemoveChild

from DataStructures.Trees import *
from test import constraint as constraintTree, constraint2 as constraintTree2, current, dominantSet, commandSet, parentOfCurrent


# input = "&(B, !(|(C, |(A, &(!(B), A)))))"
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
# input = "|(&(D, &(C, A)), |(&(C, A), &(E, &(C, A))))"
# input = "!(!(&(A, B)))"
# input = "|(&(A, B), &(A, B))"
# input = "|(g, &(a, &(b, &(|(!(c), |(!(d), e)), |(c, &(c, f))))))" # Example from Mosh's paper
# input2 = "|(g,&(a, &(b, &(c, |(!(d), e)))))" # Reduced form of the above expression from Mosh's paper.
# input2 = "|(g, &(a, &(b, &(|(c, |(d, e)), |(c, f)))))"

# Test cases for inconsistent handle set
# input = "&(a, |(&(!(a), |(b, c)), b))" # Input tree
# input2 = "&(a, b)" # Output tree

# Test cases for Promote Common Constraints (Promote) Transformation
# input = "&(a, &(|(&(!(b), c), !(b)), |(!(c), &(!(b), !(d)))))"
# input2 = "&(a, &(!(b), &(c, |(!(c), &(!(b), !(d))))))"

# Test cases for Subtract redundant constraint (Redundant) Transformation
# input = "&(a, |(&(!(b), &(c, |(&(a, &(c, !(d))), a))), !(e)))"
# input2 = "&(a, |(&(!(b), &(c, |(!(d), a))), !(e)))"

# The 0-Consraint Subsumption (0-Subsume) Transformation
# input = "&(a, &(|(a, |(!(b), |(e, f))), c))"
# input2 = "&(a, |(a, &(!(b), |(e, f))))"

# The 1-Consraint Subsumption (1-Subsume) Transformation
# input = "&(a, |(&(b, |(&(e,d), c)), d))"
# input2 = "&(a, |(&(b, c), d))"

# 1-Constraint-Complement-Subtraction (1-CC-Subtract) Transformation
# input = "&(a, |(&(b, |(&(b, c), d)), !(b)))"
# input2 = "&(a, |(&(b, |(c, d)), !(b)))"

# 1-Constraint-Complement-Subtraction (1-CC-Subtract) Transformation
# input = "&(a, |(&(b, |(&(b, c), d)), !(b)))"
# input2 = "&(a, |(&(b, |(c, d)), !(b)))"



# tree = BuildTree(input)
# tree2 = BuildTree(input2)
# root = BinaryExpressionTreeNode("Root")
# root.type = NodeType.ROOT
# root.right = tree
#

print("Constraint tree before modification")
print_constraint_tree(constraintTree)

rteOutput = reduceToElegance(current, dominantSet, commandSet)
match rteOutput:
    case ReductionSignal.DELETE:
        parentOfCurrent.children = findAndRemoveChild(parentOfCurrent.children, current)

print("RTE action: ", rteOutput)
print("Constraint tree after modification")
print_constraint_tree(constraintTree)
#
# root2 = BinaryExpressionTreeNode("Root")
# root2.type = NodeType.ROOT
# root2.right = tree2
#
# # print("Binary Expression Tree finished")
# # print_tree(root)
#
# binaryConstraintTree = propagateTruthValue(root)
# print("Binary Constraint Tree finished")
# print_tree(binaryConstraintTree)
#
# binaryConstraintTree2 = propagateTruthValue(root2)
# print("Binary Constraint Tree finished")
# print_tree(binaryConstraintTree2)
#
# constraintTree = TreeNode("ROOT")
# constraintTree.type = NodeType.ROOT
#
# constraintTree2 = TreeNode("ROOT")
# constraintTree2.type = NodeType.ROOT

# if binaryConstraintTree is not None:
#     constraintTree = gatherJunctors(binaryConstraintTree, constraintTree)
# # print("Constraint Tree Finished")
# print("Before Reduction")
#
# if constraintTree:
#     print_constraint_tree(constraintTree)
#
#
# if binaryConstraintTree2 is not None:
#     constraintTree2 = gatherJunctors(binaryConstraintTree2, constraintTree2)
# # print("Constraint Tree Finished")
# print("Before Reduction 2")
#
# if constraintTree:
#     print_constraint_tree(constraintTree)


# lastAction = reduceToElegance(constraintTree, [], [])
# If the last action returned is a DELETE, that means the whole tree is a contradiction. Will always return False
# If the last action returned is a DISCONNECT, that means the whole tree is a tautology. Will always return True
# If the last action returned is a KEEP, that means the algorithm tried to reduce the tree as much as possible
# print("Last action after reduction: ", lastAction)
# if constraintTree:
#     print_constraint_tree(constraintTree)
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

print("constraint tree 1")
print_constraint_tree(constraintTree)

print("constraint tree 2")
print_constraint_tree(constraintTree2)

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
def generateExpressionTruthTable(tree, literals):
    truthTable = []
    for generatedTruthValues in generateTruthTableValues(literals):
        outcome = evaluateBinaryExpressionTreeNode(tree, generatedTruthValues)
        truthTable.append((generatedTruthValues, outcome))
    return truthTable

# print(generateExpressionTruthTable(['A', 'B']))
# print(generateExpressionTruthTable(['A', 'B', 'C', 'D']))
initialTruthTable = generateExpressionTruthTable(constraintTree, ['a', 'b', 'c', 'd'])
supposedlyReducedTruthTable = generateExpressionTruthTable(constraintTree2, ['a', 'b', 'c', 'd'])

def generateReducedTruthTable(literals):
    reducedTruthTable = []
    for generatedTruthValues in generateTruthTableValues(literals):
        outcome = evaluateReducedConstraintTree(constraintTree, generatedTruthValues)
        reducedTruthTable.append((generatedTruthValues, outcome))
    return reducedTruthTable

# print(generateReducedTruthTable(['A', 'B']))
# print(generateReducedTruthTable(['A', 'B', 'C']))
# print(generateReducedTruthTable(['A', 'B', 'C', 'D']))
reducedTruthTable = generateReducedTruthTable(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

def compare_tables(table1, table2):
    # Convert each tuple in the table into a sorted representation
    def sorted_tuple(t):
        return (tuple(sorted(t[0].items())), t[1])
    
    # Sort both tables based on their sorted tuple representation
    sorted_table1 = sorted(map(sorted_tuple, table1))
    sorted_table2 = sorted(map(sorted_tuple, table2))
    
    if sorted_table1 == sorted_table2:
        print("Tables are equal.")
        return True
    else:
        print("Tables are not equal.")
        
        # Create dictionaries to map the first elements to their boolean values
        dict_table1 = {sorted_tuple(t)[0]: sorted_tuple(t)[1] for t in table1}
        dict_table2 = {sorted_tuple(t)[0]: sorted_tuple(t)[1] for t in table2}
        
        # Find entries with the same first element but different second elements
        for key in dict_table1:
            if key in dict_table2 and dict_table1[key] != dict_table2[key]:
                print(f"Mismatch found for entry {key}:")
                print(f" - Table 1 has {dict_table1[key]}")
                print(f" - Table 2 has {dict_table2[key]}")
                
        return False

compare_tables(initialTruthTable, supposedlyReducedTruthTable)

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
