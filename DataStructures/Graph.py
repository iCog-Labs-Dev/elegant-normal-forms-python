from enum import Enum
from Trees import NodeType, BinaryConstraintTreeNode

class GraphNodeType(Enum):
    START = "START"
    STOP = "STOP"
    INTERNAL = "INTERNAL"
    AND = "AND"
    OR = "OR"

class ConstraintGraphNode:
    def __init__(self):
        self.value: str = ""
        self.next: ConstraintGraphNode | None = None
        self.type: NodeType = NodeType.LITERAL
        self.graphNodeType: GraphNodeType = GraphNodeType.INTERNAL
        self.guardSet: list[BinaryConstraintTreeNode] | None = None