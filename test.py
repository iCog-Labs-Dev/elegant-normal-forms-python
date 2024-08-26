from Utilities.HelperFunctions import print_constraint_tree, union
from DataStructures.Trees import NodeType, TreeNode

a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
root = TreeNode("OR")
root.type = NodeType.OR
secondORNode = TreeNode("OR")
secondORNode.type = NodeType.OR
b.children.append(secondORNode)

c.guardSet.append(b)
b.guardSet.append(a)

a.constraint = True
b.constraint = True
d.constraint = True
c.constraint = True
e.constraint = True

chAndNode1 = TreeNode("AND")
chAndNode1.type = NodeType.AND
chAndNode1.guardSet.append(a)

chAndNode2 = TreeNode("AND")
chAndNode2.type = NodeType.AND
chAndNode2.guardSet.append(b)

chAndNode3 = TreeNode("AND")
chAndNode3.type = NodeType.AND
chAndNode3.guardSet.append(c)

chAndNode4 = TreeNode("AND")
chAndNode4.type = NodeType.AND
chAndNode4.guardSet.append(d)

chAndNode5 = TreeNode("AND")
chAndNode5.type = NodeType.AND
chAndNode5.guardSet.append(e)

children = [a, b, c, d]


# print(commandSetIterator(children))
def commandSetIterator(children, level, localCommandSet, target, targetNodeLevel):
    if children == [] or (
        children[0].value == target.value and children[0].type == target.type
    ):
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


def buildOneSubsumeIO():
    input = TreeNode("AND")
    input.type = NodeType.AND
    input.guardSet = [a]

    firstInputORNode = TreeNode("OR")
    firstInputORNode.type = NodeType.OR

    secondInputORNode = TreeNode("OR")
    secondInputORNode.type = NodeType.OR
    bAnd = TreeNode("AND")
    bAnd.type = NodeType.AND
    bAnd.guardSet = [b]
    bAnd.children = [secondInputORNode]

    dAnd = TreeNode("AND")
    dAnd.type = NodeType.AND
    dAnd.guardSet = [d]
    firstInputORNode.children = [bAnd, dAnd]
    input.children = [firstInputORNode]

    edAnd = TreeNode("AND")
    edAnd.type = NodeType.AND
    edAnd.guardSet = [e, d]

    cAnd = TreeNode("AND")
    cAnd.type = NodeType.AND
    cAnd.guardSet = [c]
    secondInputORNode.children = [edAnd, cAnd]

    output = TreeNode("AND")
    output.type = NodeType.AND
    output.guardSet = [a]

    firstOutputORNode = TreeNode("OR")
    firstOutputORNode.type = NodeType.OR
    secondOutputORNode = TreeNode("OR")
    secondOutputORNode.type = NodeType.OR
    secondOutputORNode.children = [cAnd]

    bbAnd = TreeNode("AND")
    bbAnd.type = NodeType.AND
    bbAnd.guardSet = [b]
    bbAnd.children = [secondOutputORNode]

    firstOutputORNode.children = [bbAnd, dAnd]
    output.children = [firstOutputORNode]

    return input, output, edAnd


def buildApplyORCutIO():
    input = TreeNode("AND")
    input.type = NodeType.AND
    input.guardSet = [a]

    dAnd = TreeNode("AND")
    dAnd.type = NodeType.AND
    negD = TreeNode("d")
    negD.constraint = False
    dAnd.guardSet = [negD]

    secondInputORNode = TreeNode("OR")
    secondInputORNode.type = NodeType.OR
    secondInputORNode.children = [dAnd]

    bAnd = TreeNode("AND")
    bAnd.type = NodeType.AND
    bAnd.guardSet = [b]
    bAnd.children = [secondInputORNode]

    cAnd = TreeNode("AND")
    negC = TreeNode("c")
    negC.type = NodeType.LITERAL
    negC.constraint = False
    cAnd.type = NodeType.AND
    cAnd.guardSet = [negC]

    firstInputORNode = TreeNode("OR")
    firstInputORNode.type = NodeType.OR
    firstInputORNode.children = [bAnd, cAnd]

    input.children = [firstInputORNode]

    output = TreeNode("AND")
    output.type = NodeType.AND
    output.guardSet = [a]

    firstOutputORNode = TreeNode("OR")
    firstOutputORNode.type = NodeType.OR

    b2And = TreeNode("AND")
    b2And.type = NodeType.AND
    b2And.guardSet = [b]

    bdAnd = TreeNode("AND")
    bdAnd.type = NodeType.AND
    bdAnd.guardSet = [b, negD]

    firstOutputORNode.children = [bdAnd, cAnd]
    output.children = [firstOutputORNode]

    return input, output, secondInputORNode


def buildApplyANDCutIO():
    input = TreeNode("AND")
    input.type = NodeType.AND
    input.guardSet = [a]
    cAnd = TreeNode("AND")
    cAnd.type = NodeType.AND
    cAnd.guardSet = [c]

    bdAnd = TreeNode("AND")
    bdAnd.type = NodeType.AND
    bdAnd.guardSet = [b, d]

    eAnd = TreeNode("AND")
    eAnd.type = NodeType.AND
    negE = TreeNode("e")
    negE.constraint = False
    eAnd.guardSet = [negE]

    secondInputORNode = TreeNode("OR")
    secondInputORNode.type = NodeType.OR
    secondInputORNode.children = [bdAnd, eAnd]

    emptyGsAnd = TreeNode("AND")
    emptyGsAnd.type = NodeType.AND
    emptyGsAnd.children = [secondInputORNode]

    firstInputORNode = TreeNode("OR")
    firstInputORNode.type = NodeType.OR
    firstInputORNode.children = [emptyGsAnd, cAnd]
    input.children = [firstInputORNode]

    output = TreeNode("AND")
    output.type = NodeType.AND
    output.guardSet = [a]

    firstOutputORNode = TreeNode("OR")
    firstOutputORNode.type = NodeType.OR
    firstOutputORNode.children = [bdAnd, eAnd, cAnd]

    output.children = [firstOutputORNode]

    return input, output, emptyGsAnd


def OneCCSubtract():
    input = TreeNode("AND")
    input.type = NodeType.AND
    input.guardSet = [a]

    bcAnd = TreeNode("AND")
    bcAnd.type = NodeType.AND
    bcAnd.guardSet = [b, c]

    dAnd = TreeNode("AND")
    dAnd.type = NodeType.AND
    dAnd.guardSet = [d]

    secondInputORNode = TreeNode("OR")
    secondInputORNode.type = NodeType.OR
    secondInputORNode.children = [bcAnd, dAnd]

    posBAnd = TreeNode("AND")
    posBAnd.type = NodeType.AND
    posBAnd.guardSet = [b]
    posBAnd.children = [secondInputORNode]

    negBAnd = TreeNode("AND")
    negBAnd.type = NodeType.AND
    negB = TreeNode("b")
    negBAnd.guardSet = [negB]

    cAnd = TreeNode("AND")
    cAnd.type = NodeType.AND
    cAnd.guardSet = [c]

    firstInputORNode = TreeNode("OR")
    firstInputORNode.type = NodeType.OR
    firstInputORNode.children = [posBAnd, negBAnd]

    input.children = [firstInputORNode]

    output = TreeNode("AND")
    output.type = NodeType.AND
    output.guardSet = [a]

    firstOutputORNode = TreeNode("OR")
    firstOutputORNode.type = NodeType.OR
    secondOutputORNode = TreeNode("OR")
    secondOutputORNode.type = NodeType.OR
    secondOutputORNode.children = [cAnd, dAnd]
    posB2And = TreeNode("AND")
    posB2And.type = NodeType.AND
    posB2And.guardSet = [b]
    posB2And.children = [secondOutputORNode]
    firstOutputORNode.children = [posB2And, negBAnd]
    output.children = [firstOutputORNode]

    return input, output, bcAnd


# oneCCSub = OneCCSubtract()
# oneCCSubDomSet = dominantSetIterator(oneCCSub[0].children, 0, [], oneCCSub[2], 3)
# oneCCSubComSet = commandSetIterator(oneCCSub[0].children, 0, [], oneCCSub[2], 3)
# print(oneCCSubDomSet, oneCCSubComSet)
# print_constraint_tree(OneCCSubtract()[0])
# print_constraint_tree(OneCCSubtract()[1])
# print_constraint_tree(OneCCSubtract()[2])

# print_constraint_tree(buildOneSubsumeIO()[0])
# print_constraint_tree(buildOneSubsumeIO()[1])
# print_constraint_tree(buildOneSubsumeIO()[2])

# print_constraint_tree(buildApplyORCutIO()[0])
# print_constraint_tree(buildApplyORCutIO()[1])
# print_constraint_tree(buildApplyORCutIO()[2])

# print_constraint_tree(buildApplyANDCutIO()[0])
# print_constraint_tree(buildApplyANDCutIO()[1])
# print_constraint_tree(buildApplyANDCutIO()[2])
