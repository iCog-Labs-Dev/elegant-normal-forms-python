from functools import reduce
from DataStructures.Trees import NodeType
from Utilities.HelperFunctions import intersection, union


def ruleFive(tree):
    def traverse(node, level=0):
        for child in node.children:
            if child.type == NodeType.OR:
                if child.children:
                    guardsets = []
                    for gs in child.children:
                        guardsets.append(gs.guardSet)
                    assert (
                        len(reduce(intersection, guardsets, [])) == 0
                    ), "Not in ENF Form, case 5 Failed"

            traverse(child, level + 1)

    traverse(tree)


def ruleSix(tree):
    # For each AND node, the intersection of its guard set and its dominant set is
    # empty
    def dominantSetIterator(children, level, localDominantSet, target, targetNodeLevel):
        if children == []:
            return localDominantSet
        if children[0].value == target.value and children[0].type == target.type:
            return localDominantSet
        else:
            if children[0].type == NodeType.AND and level < targetNodeLevel:
                return union(
                    children[0].guardSet,
                    dominantSetIterator(
                        children[1:], level, localDominantSet, target, targetNodeLevel
                    ),
                )
            else:
                return dominantSetIterator(
                    children[1:], level + 1, localDominantSet, target, targetNodeLevel
                )

    def traverse(root, node, level=0):
        for child in node.children:
            if child.type == NodeType.AND:
                assert (
                    len(
                        intersection(
                            child.guardSet,
                            dominantSetIterator(root.children, 0, [], child, level),
                        )
                    )
                    == 0
                ), "Not in ENF, case 6 failed"
            traverse(root, child, level + 1)

    traverse(tree, tree)


def ruleSeven(tree):
    # For each AND node, the intersection of its guard set and its command set is
    # empty
    # A commands B if:
    #   if A is a childless AND node having only one constraint in its guard set.
    #   A is a child of an ancestor of B
    #   A and B are not in the same branch
    def commandSetIterator(children, level, localCommandSet, target, targetNodeLevel):
        if children == []:
            return localCommandSet
        if children[0].value == target.value and children[0].type == target.type:
            return localCommandSet
        else:
            if (
                children[0].children == []
                and len(children[0].guardSet if children[0].guardSet else []) == 1
                and children
                and children[0].type == NodeType.AND
            ):
                return union(
                    children[0].guardSet,
                    commandSetIterator(
                        children[1:], level, localCommandSet, target, targetNodeLevel
                    ),
                )
            else:
                return commandSetIterator(
                    children[1:], level + 1, localCommandSet, target, targetNodeLevel
                )

    def traverse(root, node, level=0):
        for child in node.children:
            if child.type == NodeType.AND:
                ds = commandSetIterator(root.children, 0, [], child, level)
                assert (
                    len(
                        intersection(
                            child.guardSet,
                            commandSetIterator(root.children, 0, [], child, level),
                        )
                    )
                    == 0
                ), "Not in ENF, case 7 failed"

            traverse(root, child, level + 1)

    traverse(tree, tree)
