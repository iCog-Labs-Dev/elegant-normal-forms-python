from typing import Union
from DataStructures.Trees import *


def propagateTruthValue(
    currentNode: BinaryExpressionTreeNode,
    truthValue: bool = True,
) -> Union[TreeNode, None]:
    temporaryNode: TreeNode= TreeNode("")

    match currentNode.type:
        case NodeType.ROOT:
            temporaryNode.type = currentNode.type
            temporaryNode.value = currentNode.value
            if currentNode.right is not None:
                temporaryNode.right = propagateTruthValue(currentNode.right, truthValue)
            return temporaryNode

        case NodeType.NOT:
            if currentNode.right is not None:
                return propagateTruthValue(currentNode.right, not truthValue)

        case NodeType.AND | NodeType.OR:
            if truthValue == False:
                if currentNode.type == NodeType.AND:
                    temporaryNode.type = NodeType.OR
                    temporaryNode.value = "OR"
                else:
                    temporaryNode.type = NodeType.AND
                    temporaryNode.value = "AND"

            else:
                temporaryNode.value = currentNode.value
                temporaryNode.type = currentNode.type

            if currentNode.left is not None and currentNode.right is not None:
                temporaryNode.left = propagateTruthValue(currentNode.left, truthValue)
                temporaryNode.right = propagateTruthValue(currentNode.right, truthValue)
            return temporaryNode
        case _:
            temporaryNode.value = currentNode.value
            temporaryNode.type = currentNode.type
            temporaryNode.constraint = truthValue
            return temporaryNode
