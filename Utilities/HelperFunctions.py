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


def compareBCTNode(n1: BinaryConstraintTreeNode, n2: BinaryConstraintTreeNode) -> bool:
    return n1.value == n2.value and n1.constraint == n2.constraint


def find_object(
    objs_list: List[BinaryConstraintTreeNode],
    instance: BinaryConstraintTreeNode,
    index=0,
) -> bool:
    if index == len(objs_list):
        return False
    elif (
        objs_list[index].value == instance.value
        and objs_list[index].constraint == instance.constraint
    ):
        return True
    else:
        return find_object(objs_list, instance, index + 1)


def union(
    list1: List[BinaryConstraintTreeNode], list2: List[BinaryConstraintTreeNode]
) -> List[BinaryConstraintTreeNode]:
    if not list1:
        return list2
    elif find_object(list2, list1[0]):
        return union(list1[1:], list2)
    else:
        return [list1[0]] + union(list1[1:], list2)


def intersection(
    list1: List[BinaryConstraintTreeNode], list2: List[BinaryConstraintTreeNode]
) -> List[BinaryConstraintTreeNode]:
    if not list1 or not list2:
        return []
    element = list1[0]

    if find_object(list2, element):
        return [element] + intersection(list1[1:], list2)
    else:
        return intersection(list1[1:], list2)


def difference(
    list1: List[BinaryConstraintTreeNode], list2: List[BinaryConstraintTreeNode]
) -> List[BinaryConstraintTreeNode]:
    if not list1:
        return []
    element = list1[0]

    if find_object(list2, element):
        return difference(list1[1:], list2)
    return [element] + difference(list1[1:], list2)
