
from HelperFunctions import isConsistent
from DataStructures.Trees import BinaryConstraintTreeNode

ex_a = BinaryConstraintTreeNode("x")
ex_b = BinaryConstraintTreeNode("x")
ex_c = BinaryConstraintTreeNode("y")
ex_d = BinaryConstraintTreeNode("d")
ex_e = BinaryConstraintTreeNode("e")
ex_b.constraint = True

test_data = [ex_a,ex_c,ex_d,ex_b,ex_e]

print(isConsistent(test_data))


