from DataStructures.Graph import ConstraintGraphNode,GraphNodeType
from .HelperFunctions import isConsistent,union
from typing import List,Union,Any

from DataStructures.Trees import BinaryConstraintTreeNode

def traverseGraphIterator(childrenList: List[Any], incomingSet: List[Any], selectionSet: List):
    if childrenList == []:
        return []
    else:
        traverseGraph(childrenList[0],incomingSet,selectionSet)
        traverseGraphIterator(childrenList[1:],incomingSet,selectionSet)
    
    


def traverseGraph(constraintGraphNode:Union[ConstraintGraphNode|None],
                  incomingSet: List[BinaryConstraintTreeNode|ConstraintGraphNode],
                  selectionSet: List[BinaryConstraintTreeNode|ConstraintGraphNode])-> List :
    if constraintGraphNode == None:
        return []
    match constraintGraphNode.graphNodeType:
        case GraphNodeType.START:
            local_set = []
            traverseGraph(constraintGraphNode.next, local_set,selectionSet)
        case GraphNodeType.AND:
            if (isConsistent(incomingSet)):
                traverseGraph(constraintGraphNode.next,union(constraintGraphNode.guardSet,incomingSet),selectionSet)
        case GraphNodeType.OR:
            traverseGraphIterator(constraintGraphNode.children,incomingSet,selectionSet)
        case GraphNodeType.STOP:
            selectionSet.append(incomingSet)
            return selectionSet
                
            