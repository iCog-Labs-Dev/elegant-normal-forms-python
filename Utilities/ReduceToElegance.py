from enum import Enum
from typing import Any
from DataStructures.Trees import BinaryConstraintTreeNode, ConstraintTreeNode, NodeType

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

def iterator(previousGuardSet: list[BinaryConstraintTreeNode], current: ConstraintTreeNode, dominantSet: list[BinaryConstraintTreeNode], commandSet: list[BinaryConstraintTreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    handleSet = setUnion(dominantSet, current.guardSet)

def reduceToElegance(current: ConstraintTreeNode, dominantSet: list[BinaryConstraintTreeNode], commandSet: list[BinaryConstraintTreeNode]):
    match current.type:
        case NodeType.AND:
            #current.guardSet = setDifference(current.guardSet, dominantSet)
            #current.guardSet = setDifference(current.guardSet, commandSet)

            if len(current.children) == 0 and (current.guardSet is not None and len(current.guardSet) == 0):
                return ReductionSignal.DISCONNECT
            #resultSet = setIntersection(current.guardSet, commandSet)
            resultSet = []
            if len(resultSet) == 0:
                return ReductionSignal.DELETE

        case _:
            pass



