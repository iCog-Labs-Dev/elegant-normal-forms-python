from enum import Enum
from Trees import NodeType

class GraphNodeType(Enum):
    START = "START"
    STOP = "STOP"
    INTERNAL = "INTERNAL"

class ConstraintGraphNode:
    def __init__(self):
        self.value: str = ""
        self.next: ConstraintGraphNode | None = None
        self.type: NodeType = NodeType.LITERAL
        self.graphNodeType: GraphNodeType = GraphNodeType.INTERNAL
