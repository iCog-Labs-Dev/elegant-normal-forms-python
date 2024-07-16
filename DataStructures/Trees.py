from enum import Enum


class NodeType(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LITERAL = "LITERAL"
    ROOT = "ROOT"


class BinaryExpressionTreeNode:
    def __init__(self, value: str):
        self.left: BinaryExpressionTreeNode | None = None
        self.right: BinaryExpressionTreeNode | None = None
        self.value: str = value
        self.type: NodeType = NodeType.LITERAL


class BinaryConstraintTreeNode:
    def __init__(self, value: str, constraint: bool = False):
        self.left: BinaryConstraintTreeNode | None = None
        self.right: BinaryConstraintTreeNode | None = None
        self.value: str = value
        self.constraint: bool = constraint
        self.guardSet: list[BinaryConstraintTreeNode] | None = None
        self.type: NodeType = NodeType.LITERAL


class ConstraintTreeNode:
    def __init__(self, value:str, constraint: bool = False):
        self.value: str = value
        self.constraint: bool = constraint
        self.type: NodeType = NodeType.LITERAL
        self.children: list[BinaryConstraintTreeNode] = []
        self.guardSet: list[BinaryConstraintTreeNode] | None = None

def compareBinaryConstraintTreeNode(node1: BinaryConstraintTreeNode, node2: BinaryConstraintTreeNode):
    return node1.value == node2.value and node1.constraint == node2.constraint

def findAndRemoveChild(children: list[BinaryConstraintTreeNode], child: BinaryConstraintTreeNode) -> list[BinaryConstraintTreeNode]:
    if len(children) == 0:
        return []

    firstChild = children[0]
    if compareBinaryConstraintTreeNode(firstChild, child):
        return children[1:]
    elif len(children) > 0:
        acc = findAndRemoveChild(children[1:], child)
        acc.append(firstChild)
        return acc
    else:
        return []
