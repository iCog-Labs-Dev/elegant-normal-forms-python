from typing import Union
from DataStructures.Trees import (
    BinaryExpressionTreeNode,
    NodeType,
    TreeNode
)


def print_tree(
    node: Union[TreeNode, BinaryExpressionTreeNode, None], level=0, side=""
):
    constraint = ""
    if type(node) == TreeNode and node.type == NodeType.LITERAL:
        constraint = f"{'+' if node.constraint else '-'}"

    if node is None:
        return
    print("    " * level + f"[{side}{level}]", f"{constraint}{node.value}")

    if(node.left is not None):
        print_tree(node.left, level + 1, "L")

    if(node.right is not None):
        print_tree(node.right, level + 1, "R")


def eval(node: TreeNode) -> Union[bool, None]:
    if node is None:
        return
    match node.value:
        case "AND":
            if node.left is not None and node.right is not None:
                return eval(node.left) and eval(node.right)
        case "OR":
            if node.left is not None and node.right is not None:
                return eval(node.left) or eval(node.right)
        case "NOT":
            if node.right is not None:
                return not eval(node.right)
        case _:
            return node.constraint
