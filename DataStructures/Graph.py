from enum import Enum
from .Trees import NodeType, BinaryConstraintTreeNode
from typing import List

class GraphNodeType(Enum):
    START = "START"
    STOP = "STOP"
    INTERNAL = "INTERNAL"
    # AND = "AND"
    # OR = "OR"

class ConstraintGraphNode:
    def __init__(self):
        self.value: str = ""
        self.next: ConstraintGraphNode | None = None
        self.type: NodeType = NodeType.LITERAL
        self.graphNodeType: GraphNodeType = GraphNodeType.INTERNAL
        self.guardSet: List[BinaryConstraintTreeNode|ConstraintGraphNode] = []
        self.children: List[ConstraintGraphNode] =[]
        
    def __repr__(self):
        return f'{self.value}, {self.type}'
    def __str__(self):
        return f'{self.value}, {self.type}'