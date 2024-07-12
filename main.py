from Utilities.BuildTree import *
from Utilities.HelperFunctions import print_tree
from Utilities.PropagateTruthValue import propagateTruthValue

input = "&(B, !(|(C, |(A, &(!(B), A)))))"

tree = BuildTree(input)
print("Binary Expression Tree finished")
print_tree(tree)

constraintTree = propagateTruthValue(tree)
print("Constraint Tree finished")
print_tree(constraintTree)
