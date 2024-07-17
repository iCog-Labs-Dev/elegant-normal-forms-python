from enum import Enum
from typing import Union,List
from DataStructures.Trees import TreeNode, NodeType, findAndRemoveChild
from Utilities.HelperFunctions import find_object, intersection, setDifference, union, isConsistent

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

class IterationSignal(Enum):
    ADVANCE = "ADVANCE"
    RESET = "RESET"

def compareSets(set1: list[TreeNode], set2: list[TreeNode], currentIndex = 0) -> bool:
    if not (len(set1) == len(set2)):
        return False

    if currentIndex == len(set1):
        # This means the recursion finished with out finding a mismatch between the two
        return True

    currentElement = set1[0]
    if not find_object(set2, currentElement):
        return False
    else:
        set2 = findAndRemoveChild(set2, currentElement)
        return compareSets(set1[1:], set2, currentIndex + 1)
    

def commandSetIterator(children: List[TreeNode]):
    if children == []:
        return children
    else:
       if children[0].children == [] and len(children[0].guardSet if children[0].guardSet else []) == 1:
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
            current.children = findAndRemoveChild(current.children, grandChild) 

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

def orSubTreeElegance(child: TreeNode, current: TreeNode , dominantSet: list[TreeNode], localCommandSet: list[TreeNode]):
    outcome = reduceToElegance(child, dominantSet, localCommandSet)

    match outcome:
        case ReductionSignal.DELETE:
            if current.children and len(current.children) > 0:
                current.children = findAndRemoveChild(current.children, child)
                return IterationSignal.ADVANCE
            else:
                return ReductionSignal.DELETE
        case ReductionSignal.DISCONNECT:
            return ReductionSignal.DISCONNECT
        case ReductionSignal.KEEP:
            return IterationSignal.ADVANCE

def andSubTreeElegance(child: TreeNode , current: TreeNode, handleSet: list[TreeNode], commandSet: list[TreeNode]):
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


def orSubTreeIterator(child: TreeNode, remainingChildren: list[TreeNode], currentNode: TreeNode, dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    localCommandSet = commandSet

    #TODO: construct local command set here

    action = orSubTreeElegance(child, currentNode, dominantSet, localCommandSet)

    match action:
        case IterationSignal.ADVANCE:
            if len(remainingChildren) > 0:
                return orSubTreeIterator(remainingChildren[0], remainingChildren[1:],currentNode, dominantSet, commandSet)
            else:
                return None
        case IterationSignal.RESET:
            return None
        case _:
            return action


def andSubTreeIterator(children:list[TreeNode], currentNode: TreeNode, handleSet: list[TreeNode], commandSet: list[TreeNode], currentChildIndex = 0 ):
    currentChild = children[currentChildIndex]
    action = andSubTreeElegance(currentChild, currentNode, handleSet, commandSet)

    match action:
        case IterationSignal.ADVANCE :
            if currentChildIndex + 1 < len(children):
                return andSubTreeIterator(children, currentNode, handleSet, commandSet, currentChildIndex + 1)
            else:
                return None
        case IterationSignal.RESET:
            return andSubTreeIterator(children, currentNode, handleSet, commandSet, 0)
        case _:
            return action
    

def iterator(current: TreeNode , dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    handleSet = []
    
    # Determine if current is a site for inconsistent Handle
    if not isConsistent(handleSet):
        return ReductionSignal.DELETE
    
    # Reduce each child's subtree to relative elegance
    outcome = andSubTreeIterator(current.children if current.children else [], current, handleSet, commandSet)

    # The subtree iterator returns a value different from None only if ReductionSignal has been found during the processing. If not it will always return None in the end
    if outcome:
        return outcome

    # Apply OR-CUT to each child of current, if possible
    map(lambda child: applyOrCut(child, current), current.children if current.children else [])

    if not compareSets(previousGuardSet, current.guardSet if current.guardSet else []):
        return iterator(current, dominantSet, commandSet)
    
    return None


def reduceToElegance(
    current: Union[TreeNode,None], 
    dominantSet: list[TreeNode], 
    commandSet: list[TreeNode]
    ) :
    if current == None:
        return 
    match current.type:
        case NodeType.AND:
            if current.guardSet:
                # Apply Redundant to current, if possible
                current.guardSet = setDifference(current.guardSet, dominantSet)

                # Apply 1CCSubtract to current, if possible
                current.guardSet = setDifference(current.guardSet, commandSet)

            currentHasNoChild = (not current.children) or len(current.children) == 0 
            currentHasNoGuardSet = (not current.guardSet) or len(current.guardSet) == 0
            if currentHasNoChild and currentHasNoGuardSet: 
                return ReductionSignal.DISCONNECT

            # Determine if current is a site for 1Subsume

            resultSet = []
            if current.guardSet:
                resultSet = intersection(current.guardSet, commandSet)

            if len(resultSet) == 0:
                return ReductionSignal.DELETE
            
            # Repeat untile current's guardset doesn't change
            action = iterator(current, dominantSet, commandSet)
            
            if action:
                return action
            
            # Determine if current is a site for 0-Subsumption
            currentHasNoChild = (not current.children) or len(current.children) == 0 
            currentHasNoGuardSet = (not current.guardSet) or len(current.guardSet) == 0
            if currentHasNoChild and currentHasNoGuardSet :
                return ReductionSignal.DISCONNECT

            return ReductionSignal.KEEP
        case _:
            # Current type is OR
            if current.children and len(current.children) > 0:
                action = orSubTreeIterator(current.children[0], current.children[1:], current, dominantSet, commandSet)
                if action:
                    return action

            return ReductionSignal.KEEP