from enum import Enum
from DataStructures.Trees import TreeNode, NodeType
from Utilities.HelperFunctions import intersection, setDifference, union

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

def iterator(previousGuardSet: list[TreeNode], current: TreeNode , dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    handleSet = []
    
    if current.guardSet:
        handleSet = union(dominantSet, current.guardSet)

        

def reduceToElegance(current: TreeNode, dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    match current.type:
        case NodeType.AND:
            if current.guardSet:
                current.guardSet = setDifference(current.guardSet, dominantSet)
                current.guardSet = setDifference(current.guardSet, commandSet)

            # if current has no children and current's guard set is empty
            if (current.children is None or len(current.children) == 0) and (current.guardSet is not None and len(current.guardSet) == 0):
                return ReductionSignal.DISCONNECT

            resultSet = []
            if current.guardSet:
                resultSet = intersection(current.guardSet, commandSet)

            if len(resultSet) == 0:
                return ReductionSignal.DELETE

        case _:
            pass



