from typing import Union, List, Any
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

    if node.left is not None:
        print_tree(node.left, level + 1, "L")

    if node.right is not None:
        print_tree(node.right, level + 1, "R")


def eval(node: TreeNode) -> Union[bool, None]:
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
        return node.constraint
    
def isConsistentForSingleValue(first_val: TreeNode, toBeChecked: List[TreeNode]) -> bool:
    if toBeChecked == []:
        return True
    elif first_val.value == toBeChecked[0].value \
    and first_val.constraint != toBeChecked[0].constraint:
        return False
    else:
        return isConsistentForSingleValue(first_val, toBeChecked[1:])
    
def isConsistent(toBeChecked):
    if toBeChecked == []:
        return True
    else:
        if not(isConsistentForSingleValue(toBeChecked[0],toBeChecked[1:])):
            return False
        else:
            return isConsistent(toBeChecked[1:])
        

def compareBCTNode(n1: TreeNode, n2: TreeNode) -> bool:
    return n1.value == n2.value and n1.constraint == n2.constraint


def find_object(
    objs_list: List[TreeNode],
    instance: TreeNode,
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
    list1: List[TreeNode], list2: List[TreeNode]
) -> List[TreeNode]:
    if not list1:
        return list2
    elif find_object(list2, list1[0]):
        return union(list1[1:], list2)
    else:
        return [list1[0]] + union(list1[1:], list2)


def intersection(
    list1: List[TreeNode], list2: List[TreeNode]
) -> List[TreeNode]:
    if not list1 or not list2:
        return []
    element = list1[0]

    if find_object(list2, element):
        return [element] + intersection(list1[1:], list2)
    else:
        return intersection(list1[1:], list2)


def difference(
    list1: List[TreeNode], list2: List[TreeNode]
) -> List[TreeNode]:
    if not list1:
        return []
    element = list1[0]

    if find_object(list2, element):
        return difference(list1[1:], list2)
    return [element] + difference(list1[1:], list2)



# def union(list1: List[Any], list2: List[Any]) -> List[Any]:
#     if not list2:
#         return list1
#     if list2[0] not in list1:
#         return union(list1 + [list2[0]], list2[1:])
#     else:
#         return union(list1, list2[1:])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     match node.value:
#         case "AND":
#             if node.left is not None and node.right is not None:
#                 return eval(node.left) and eval(node.right)
#         case "OR":
#             if node.left is not None and node.right is not None:
#                 return eval(node.left) or eval(node.right)
#         case "NOT":
#             if node.right is not None:
#                 return not eval(node.right)
#         case _:
#             return node.constraint

