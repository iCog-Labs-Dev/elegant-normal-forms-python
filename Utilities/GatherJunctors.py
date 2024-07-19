from typing import Union
from DataStructures.Trees import *


def gatherJunctors(
    currentNode: TreeNode, centerNode: TreeNode
) -> Union[TreeNode, None]:

    if currentNode.type == NodeType.ROOT:
        currentNode.type = NodeType.AND
        currentNode.value = "AND"
        currentNode.guardSet = []
        if currentNode.right is not None:
            gatherJunctors(currentNode.right, currentNode)

        currentNode.left = None
        currentNode.right = None

        return currentNode

    elif currentNode.type in [NodeType.OR, NodeType.AND]:
        if currentNode.type == centerNode.type:
            if currentNode.left is not None:
                gatherJunctors(currentNode.left, centerNode)

            if currentNode.right is not None:
                gatherJunctors(currentNode.right, centerNode)

        else:
            centerNode.children.append(currentNode)

            if currentNode.left:
                gatherJunctors(currentNode.left, currentNode)

            if currentNode.right:
                gatherJunctors(currentNode.right, currentNode)

            currentNode.left = None
            currentNode.right = None

        if currentNode.type == NodeType.AND:
            currentNode.guardSet = []

        return None
    elif currentNode.type == NodeType.LITERAL:
        if centerNode.type == NodeType.AND:
            centerNode.guardSet.append(currentNode)

        else:
            currentNode.type = NodeType.AND
            currentNode.guardSet = [currentNode]
            centerNode.children.append(currentNode)
    return None
