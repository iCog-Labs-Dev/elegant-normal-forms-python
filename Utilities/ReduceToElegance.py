from enum import Enum
from DataStructures.Trees import TreeNode, NodeType, findAndRemoveChild
from Utilities.HelperFunctions import find_object, intersection, setDifference, union, isConsistent

class ReductionSignal(Enum):
    DELETE = "DELETE"
    DISCONNECT = "DISCONNECT"
    KEEP = "KEEP"

class IterationSignal(Enum):
    ADVANCE = "ADVANCE"
    RESET = "RESET"

def compareGuardSets(set1: list[TreeNode], set2: list[TreeNode], currentIndex = 0) -> bool:
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
        return compareGuardSets(set1[1:], set2, currentIndex + 1)
    

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

def subTreeIterator(children:list[TreeNode], currentNode: TreeNode, handleSet: list[TreeNode], commandSet: list[TreeNode], currentChildIndex = 0 ):
    currentChild = children[currentChildIndex]
    action = subTreeElegance(currentChild, currentNode, handleSet, commandSet)

    match action:
        case IterationSignal.ADVANCE :
            if currentChildIndex + 1 < len(children):
                return subTreeIterator(children, currentNode, handleSet, commandSet, currentChildIndex + 1)
            else:
                return None
        case IterationSignal.RESET:
            return subTreeIterator(children, currentNode, handleSet, commandSet, 0)
        case _:
            return action
    

def iterator(current: TreeNode , dominantSet: list[TreeNode], commandSet: list[TreeNode]):
    previousGuardSet = current.guardSet if current.guardSet is not None else []
    handleSet = []
    
    # Determine if current is a site for inconsistent Handle
    if not isConsistent(handleSet):
        return ReductionSignal.DELETE
    
    # Reduce each child's subtree to relative elegance
    outcome = subTreeIterator(current.children if current.children else [], current, handleSet, commandSet)

    # The subtree iterator returns a value different from None only if ReductionSignal has been found during the processing. If not it will always return None in the end
    if outcome:
        return outcome

    # Apply OR-CUT to each child of current, if possible
    map(lambda child: applyOrCut(child, current), current.children if current.children else [])

    if not compareGuardSets(previousGuardSet, current.guardSet if current.guardSet else []):
        return iterator(current, dominantSet, commandSet)
    
    return None


def reduceToElegance(current: TreeNode, dominantSet: list[TreeNode], commandSet: list[TreeNode]) :
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



