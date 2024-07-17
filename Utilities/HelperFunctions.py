from typing import Union,List,Any
from DataStructures.Trees import (
    BinaryConstraintTreeNode,
    BinaryExpressionTreeNode,
    ConstraintTreeNode,
    NodeType,
)


def print_tree(
    node: Union[BinaryConstraintTreeNode, BinaryExpressionTreeNode, None], level=0, side=""
):
    constraint = ""
    if type(node) == BinaryConstraintTreeNode and node.type == NodeType.LITERAL:
        constraint = f"{'+' if node.constraint else '-'}"

    if node is None:
        return
    print("    " * level + f"[{side}{level}]", f"{constraint}{node.value}")

    if(node.left is not None):
        print_tree(node.left, level + 1, "L")

    if(node.right is not None):
        print_tree(node.right, level + 1, "R")


def eval(node: Union[BinaryConstraintTreeNode|None]) -> Union[bool, None]:
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
    
def isConsistentForSingleValue(
    first_val: Union[BinaryConstraintTreeNode|ConstraintTreeNode], 
    toBeChecked: List[BinaryConstraintTreeNode|ConstraintTreeNode]
    ) -> bool:
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
        
def union(list1: List[Any], list2: List[Any]) -> List[Any]:
    if not list2:
        return list1
    if list2[0] not in list1:
        return union(list1 + [list2[0]], list2[1:])
    else:
        return union(list1, list2[1:])

    

    
        

            
    
        
        
    
    
    
    
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
