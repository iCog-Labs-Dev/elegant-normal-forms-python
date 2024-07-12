from typing import Union
from DataStructurs.BinaryTrees import *


def BuildTree(input: str) -> BinaryExpressionTreeNode | None:
    input = input.strip()
    tree = BinaryExpressionTreeNode("Null")
    first = input[0]
    if first in ["|", "&"]:
        input = input[2 : len(input) - 1]
        firstArg, secondArg = splitArgs(input)

        if firstArg is None or secondArg is None:
            raise ValueError("Insufficient arguments for binary operator")

        tree.value = "AND" if first == "&" else "OR"
        tree.left = BuildTree(firstArg)
        tree.right = BuildTree(secondArg)
        return tree
    elif first == "!":
        input = input[2 : len(input) - 1]
        tree.value = "NOT"
        tree.right = BuildTree(input)
        return tree
    elif first in ["(", ")"]:
        raise ValueError("Invalid Boolean expression format")
    else:
        tree.value = first
        return tree


def splitArgs(input: str) -> Union[tuple[str, str], tuple[None, None]]:
    brackets = 0
    index = 0
    for c in input:
        if c == "(":
            brackets += 1
        elif c == ")":
            brackets -= 1
        elif c == "," and brackets == 0:
            return input[:index], input[index + 1 :]
        index += 1
    return None, None
