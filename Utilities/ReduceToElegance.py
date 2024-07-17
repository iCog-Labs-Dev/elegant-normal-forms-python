from enum import Enum
from typing import Union,List
from DataStructures.Trees import TreeNode, NodeType, findAndRemoveChild
from Utilities.HelperFunctions import intersection, setDifference, union, isConsistent

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

class IterationSignal(Enum):
    ADVANCE = "ADVANCE"
    RESET = "RESET"
def commandSetIterator(children: List[TreeNode]):
    if children == []:
        return children
    else:
       if children[0].children == [] and len(children[0].guardSet) == 1:
           return [children[0]] + commandSetIterator(children[1:])
       else:
           return commandSetIterator(children[1:])
  
def containsTerminalAndNode(children: list[TreeNode]) -> bool:
    if len(children) == 0:
        return False
    firstChild = children[0]
    isAndNode = firstChild.type == NodeType.AND
    isTerminalNode = firstChild.children is None or len(firstChild.children) == 0
    hasSingleConstraint = firstChild.guardSet and len(firstChild.guardSet) == 1
    if isAndNode and isTerminalNode and hasSingleConstraint:
        return True 
    else:
        return containsTerminalAndNode(children[1:])
    

def applyOrCut(child: TreeNode, current: TreeNode):
        if child.children and len(child.children) == 1:
            grandChild = child.children[0]
            current.guardSet = union(current.guardSet if current.guardSet else [], grandChild.guardSet if grandChild.guardSet else [])
            current.children = grandChild.children if grandChild.children else [] + current.children if current.children else []

def applyAndCut(grandChild: TreeNode, child: TreeNode):
    hasOneChild = grandChild.children and len(grandChild.children) == 1 
    emptyGuardSet = grandChild.guardSet is None or len(grandChild.guardSet) == 0
    if hasOneChild and emptyGuardSet:
        if child.children and grandChild.children and grandChild.children[0].children:
            child.children = child.children + grandChild.children[0].children
            child.children = findAndRemoveChild(child.children, grandChild)
            return containsTerminalAndNode(grandChild.children[0].children)
    return False

def computeGrandChildGuardSet(grandChild: TreeNode, resultSet: list[TreeNode]):
    grandChild.guardSet = setDifference(grandChild.guardSet if grandChild.guardSet else [], resultSet)

def intersections(intersectionSet: list[TreeNode], children: list[TreeNode]) -> list[TreeNode]:
    if len(children) == 0:
        return []
    
    if(children[0].guardSet):
        intersectionSet = intersection(intersectionSet, children[0].guardSet)

    return intersections(intersectionSet, children[1:])

def subTreeElegance(child: TreeNode , current: TreeNode, handleSet: list[TreeNode], commandSet: list[TreeNode]):
    outcome = reduceToElegance(child, handleSet, commandSet)
    match outcome:
        case ReductionSignal.DELETE:
            current.children = []
            return ReductionSignal.DELETE 

        case ReductionSignal.DISCONNECT:
            if current.children:
                current.children = findAndRemoveChild(current.children, child)
                child.children = []
                return IterationSignal.ADVANCE

        case ReductionSignal.KEEP:
            resultSet = intersections([], current.children if current.children else [])
            if len(resultSet) > 0:
                current.guardSet = union(current.guardSet if current.guardSet else [], resultSet)
                map(lambda grandChild: computeGrandChildGuardSet(grandChild, resultSet), child.children if child.children else [])
                map(lambda grandChild: applyAndCut(grandChild, child), child.children if child.children else [])

                return IterationSignal.RESET
            else:
                bools = map(lambda grandChild: applyAndCut(grandChild, child), child.children if child.children else [])
                containsTerminalAndNode = any(bools)

                # if no terminal AND node whose guard set contains one constraint was adopted as a grandchild by current advance the child pointer to current’s next child
                if not containsTerminalAndNode:
                    return IterationSignal.ADVANCE
                else:
                    return IterationSignal.RESET

    map(lambda child: applyOrCut(child, current), current.children if current.children else [])

def iterator(previousGuardSet: list[TreeNode], current: TreeNode , dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    handleSet = []
    
    if not isConsistent(handleSet):
        return ReductionSignal.DELETE
    
    if current.children:
        current.children

def reduceToElegance(
    current: Union[TreeNode|None], 
    dominantSet: list[TreeNode], 
    commandSet: list[TreeNode]
    ) :
    if current == None:
        return 
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



