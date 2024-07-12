from typing import Union
from DataStructurs.BinaryTrees import BinaryContraintTreeNode


def print_tree(node, level=0, side=""):
    if node is None:
        return
    print("    " * level + f"[{side}{level}]", node.value)
    print_tree(node.left, level + 1, "L")
    print_tree(node.right, level + 1, "R")

def eval(node: BinaryContraintTreeNode) -> Union[bool, None]:
    if node is None:
        return
    if node.value == "AND":
        if node.left is not None and node.right is not None:
            return eval(node.left) and eval(node.right)
    elif node.value == "OR":
        if node.left is not None and node.right is not None:
            return eval(node.left) or eval(node.right)
    elif node.value == "NOT":
        if node.right is not None:
            return not eval(node.right)
    else:
        return node.contraint
