from DataStructures.Graph import ConstraintGraphNode,GraphNodeType
from typing import List,Union

from DataStructures.Trees import BinaryConstraintTreeNode


def TraverseGraph(constraintGraphNode:ConstraintGraphNode,
                  incomingSet: List[BinaryConstraintTreeNode|ConstraintGraphNode])-> Union[List|None] :
    match constraintGraphNode.type:
        case GraphNodeType.START:
            local_set = []
            TraverseGraph(constraintGraphNode.next, local_set)
        case GraphNodeType.AND:
            pass
            