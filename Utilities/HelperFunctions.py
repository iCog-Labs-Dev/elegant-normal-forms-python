from typing import Union, List
from DataStructures.Trees import (
    BinaryConstraintTreeNode,
    BinaryExpressionTreeNode,
    NodeType,
)


def print_tree(
    node: Union[BinaryConstraintTreeNode, BinaryExpressionTreeNode, None],
    level=0,
    side="",
):
    constraint = ""
    if type(node) == BinaryConstraintTreeNode and node.type == NodeType.LITERAL:
        constraint = f"{'+' if node.constraint else '-'}"

    if node is None:
        return
    print("    " * level + f"[{side}{level}]", f"{constraint}{node.value}")

    if node.left is not None:
        print_tree(node.left, level + 1, "L")

    if node.right is not None:
        print_tree(node.right, level + 1, "R")


def eval(node: BinaryConstraintTreeNode) -> Union[bool, None]:
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


def union(list1: List, list2: List) -> List:
    if not list1:
        return list2
    elif list1[0] in list2:
        return union(list1[1:], list2)
    else:
        return [list1[0]] + union(list1[1:], list2)


def intersection(list1: List, list2: List) -> List:
    if not list1 or not list2:
        return []
    element = list1[0]

    if element in list2:
        return [element] + intersection(list1[1:], list2)
    else:
        return intersection(list1[1:], list2)


def difference(list1: List, list2: List) -> List:
    if not list1:
        return []
    element = list1[0]

    if element in list2:
        return difference(list1[1:], list2)
    return [element] + difference(list1[1:], list2)
