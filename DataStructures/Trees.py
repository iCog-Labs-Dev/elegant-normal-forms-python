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
        self.type: NodeType = NodeType.LITERAL


class ConstraintTreeNode:
    def __init__(self, value:str, constraint: bool = False):
        self.value: str = value
        self.constraint: bool = constraint
        self.type: NodeType = NodeType.LITERAL
        self.children: list[BinaryConstraintTreeNode] = []
        self.guardSet: list[BinaryConstraintTreeNode] | None = None
