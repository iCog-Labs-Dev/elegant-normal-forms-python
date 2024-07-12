from DataStructurs.BinaryTrees import *

def BuildTree(input:str) -> BinaryExpressionTreeNode | None:
    tree = BinaryExpressionTreeNode("")
    first = input[0]
    if first in ["|", "&"]:
        input = input[2: len(input) -1]
        firstArg, secondArg = input.split(",")
        tree.value = "AND" if first == "&" else "OR"
        tree.left = BuildTree(firstArg)
        tree.right = BuildTree(secondArg)
        return tree
    elif first == "!":
        input = input[2: len(input) -1]
        tree.value = "NOT"
        tree.right = BuildTree(input)
        return tree
    elif first in ["(", ")"]:
        raise ValueError("Invalid Boolean expression format")
    else:
        tree.value = first
        return tree
