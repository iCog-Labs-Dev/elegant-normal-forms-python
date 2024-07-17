from enum import Enum
from DataStructures.Trees import TreeNode, NodeType

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

def iterator(previousGuardSet: list[TreeNode], current: TreeNode , dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    # handleSet = setUnion(dominantSet, current.guardSet)

def reduceToElegance(current: TreeNode, dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    match current.type:
        case NodeType.AND:
            #current.guardSet = setDifference(current.guardSet, dominantSet)
            #current.guardSet = setDifference(current.guardSet, commandSet)

            if current.children and len(current.children) == 0 and (current.guardSet is not None and len(current.guardSet) == 0):
                return ReductionSignal.DISCONNECT
            #resultSet = setIntersection(current.guardSet, commandSet)
            resultSet = []
            if len(resultSet) == 0:
                return ReductionSignal.DELETE

        case _:
            pass



