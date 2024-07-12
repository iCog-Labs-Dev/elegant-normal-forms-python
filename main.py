from Utilities.BuildTree import *
from Utilities.HelperFunctions import print_tree

input = "|(!(&(A,B)),&(B,C))"

tree = BuildTree(input)
print_tree(tree)
