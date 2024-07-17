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


class TreeNode:
    def __init__(self, value: str, constraint: bool = False):
        self.value: str = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.constraint: bool = constraint
        self.guardSet: list[TreeNode] | None = None
        self.children: list[TreeNode] | None = None 
        self.type: NodeType = NodeType.LITERAL


def findAndRemoveChild(children: list[TreeNode], child: TreeNode) -> list[TreeNode]:
    if len(children) == 0:
        return []

    firstChild = children[0]
    if firstChild == child:
        return children[1:]
    elif len(children) > 0:
        acc = findAndRemoveChild(children[1:], child)
        acc.append(firstChild)
        return acc
    else:
        return []
