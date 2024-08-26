from DataStructures.Trees import TreeNode, NodeType

a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")

aprime = TreeNode("a")
bprime = TreeNode("b")
cprime = TreeNode("c")
dprime = TreeNode("d")
eprime = TreeNode("e")
fprime = TreeNode("f")

a.constraint = True
b.constraint = True
c.constraint = True
d.constraint = True
e.constraint = True
f.constraint = True

or11 = TreeNode("OR")
or21 = TreeNode("OR")
or22 = TreeNode("OR")
or11.type = NodeType.OR
or21.type = NodeType.OR
or22.type = NodeType.OR

or112 = TreeNode("OR")
or212 = TreeNode("OR")
or222 = TreeNode("OR")
or112.type = NodeType.OR
or212.type = NodeType.OR
or222.type = NodeType.OR

and11 = TreeNode("AND")
and12 = TreeNode("AND")
and13 = TreeNode("AND")
and14 = TreeNode("AND")
and21 = TreeNode("AND")
and22 = TreeNode("AND")
and23 = TreeNode("AND")
and24 = TreeNode("AND")
and11.type = NodeType.AND
and12.type = NodeType.AND
and13.type = NodeType.AND
and14.type = NodeType.AND
and21.type = NodeType.AND
and22.type = NodeType.AND
and23.type = NodeType.AND
and24.type = NodeType.AND

and112 = TreeNode("AND")
and122 = TreeNode("AND")
and132 = TreeNode("AND")
and142 = TreeNode("AND")
and212 = TreeNode("AND")
and222 = TreeNode("AND")
and232 = TreeNode("AND")
and242 = TreeNode("AND")
and112.type = NodeType.AND
and122.type = NodeType.AND
and132.type = NodeType.AND
and142.type = NodeType.AND
and212.type = NodeType.AND
and222.type = NodeType.AND
and232.type = NodeType.AND
and242.type = NodeType.AND

constraint = TreeNode("AND")
constraint.type = NodeType.AND

constraint2 = TreeNode("AND")
constraint2.type = NodeType.AND

# NOTE: Test case for inconsistent handle (InconHandle).

# and11.guardSet = [b]
# and12.guardSet = [c]
# and21.guardSet = [aprime]
# and22.guardSet = [b]
# constraint.guardSet = [a]
#
# and21.children = [or11]
# constraint.children = [or21]
# or11.children = [and11, and12]
# or21.children = [and21, and22]
#
# or112 = TreeNode("OR")
# or112.type = NodeType.OR
#
# and112.guardSet = [b]
# constraint2.guardSet = [a]
#
# or112.children = [and112]
# constraint2.children = [or112]
#
# current = and21
# parentOfCurrent = or21
# dominantSet = [a]
# commandSet = [b]

# NOTE: Test cases for Promote-Common-Constraints (Promote) Transformation.

# and11.guardSet = [bprime, c]
# and12.guardSet = [bprime]
# and13.guardSet = [cprime]
# and14.guardSet = [bprime, dprime]
#
# or11.children = [and11, and12]
# or12.children = [and13, and14]
#
# constraint.guardSet = [a]
# constraint.children = [or11, or12]
#
# and112.guardSet = [c]
# and122.guardSet = []
# and132.guardSet = [cprime]
# and142.guardSet = [bprime, dprime]
#
# or112.children = [and112, and122]
# or122.children = [and132, and142]
#
# constraint2.guardSet = [a, bprime]
# constraint2.children = [or112, or122]
#
# current = or11
# parentOfCurrent = constraint
# dominantSet = [a]
# commandSet = []

# NOTE: Test cases for subtract redundant constraint (Redundant) transformation.

# and11.guardSet = [a, c, dprime]
# and12.guardSet = [a]
# and21.guardSet = [bprime, c]
# and22.guardSet = [eprime]
# constraint.guardSet = [a]
#
# or11.children = [and11, and12]
# or21.children = [and21, and22]
# and21.children = [or11]
# constraint.children = [or21]
#
# and112.guardSet = [dprime]
# and122.guardSet = [a]
# and212.guardSet = [bprime, c]
# and222.guardSet = [eprime]
# constraint2.guardSet = [a]
#
# or112.children = [and112, and122]
# or212.children = [and212, and222]
# and212.children = [or112]
# constraint2.children = [or212]
#
# current = and11
# parentOfCurrent = or11
# dominantSet = [bprime, c, a]
# commandSet = [a]

# NOTE: Test cases for cut unnecessary or (OrCut) transformation.

# and11.guardSet = [dprime]
# and21.guardSet = [b]
# and22.guardSet = [cprime]
# constraint.guardSet = [a]
#
# or11.children = [and11]
# or21.children = [and21, and22]
# and21.children = [or11]
# constraint.children = [or21]
#
# and112.guardSet = [b, dprime]
# and122.guardSet = [cprime]
# constraint2.guardSet = [a]
#
# or112.children = [and112, and122]
# constraint2.children = [or112]
#
# current = or11
# parentOfCurrent = and21
# dominantSet = [a, b]
# commandSet = []

# NOTE: Test cases for cut unnecessary and (AndCut) transformation.

# and11.guardSet = [b, a]
# and12.guardSet = [eprime]
# and21.guardSet = []
# and22.guardSet = [c]
# constraint.guardSet = [a]
#
# or11.children = [and11, and12]
# or21.children = [and21, and22]
# and21.children = [or11]
# constraint.children = [or21]
#
# and112.guardSet = [b, d]
# and122.guardSet = [eprime]
# and132.guardSet = [c]
# constraint2.guardSet = [a]
#
# or112.children = [and112, and122, and132]
# constraint2.children = [or112]
#
# current = and21
# parentOfCurrent = or21
# dominantSet = []
# commandSet = []

# NOTE: Test cases for 0 constraint subsumption(0-Subsume) transformation.

# and11.guardSet = [e]
# and12.guardSet = [f]
# and21.guardSet = [a]
# and22.guardSet = [bprime]
# and23.guardSet = [c]
# and24.guardSet = []
# and22.children = [or11]
#
# or11.children = [and11, and12]
# or21.children = [and21, and22]
# or22.children = [and23, and24]
#
# constraint.guardSet = [a]
# constraint.children = [or21, or22]
#
# and112.guardSet = [e]
# and122.guardSet = [f]
# and212.guardSet = [a]
# and222.guardSet = [bprime]
# and222.children = [or112]
#
# or112.children = [and112, and122]
# or212.children = [and212, and222]
#
# constraint2.guardSet = [a]
# constraint2.children = [or212]
#
# current = or22
# parentOfCurrent = constraint
# dominantSet = [a]
# commandSet = []

# NOTE: Test cases for 1 - Constraint - Subsumption (1Subsume) Transformation.

# and11.guardSet = [e, d]
# and12.guardSet = [c]
# and21.guardSet = [b]
# and22.guardSet = [d]
# constraint.guardSet = [a]
#
# or11.children = [and11, and12]
# or21.children = [and21, and22]
# and21.children = [or11]
# constraint.children = [or21]
#
# and112.guardSet = [c]
# and212.guardSet = [b]
# and222.guardSet = [d]
# constraint2.guardSet = [a]
#
# or112.children = [and112]
# or212.children = [and212, and222]
# and212.children = [or112]
# constraint2.children = [or212]
#
# current = and11
# parentOfCurrent = or11
# dominantSet = [a, b]
# commandSet = [c]

# NOTE: Test cases for 1 Constraint Complement subtraction (1CCSubtract) tranforamtion.

and11.guardSet = [b, c]
and12.guardSet = [d]
and21.guardSet = [b]
and22.guardSet = [bprime]
constraint.guardSet = [a]

or11.children = [and11, and12]
or21.children = [and21, and22]
and21.children = [or11]
constraint.children = [or21]

and112.guardSet = [c]
and122.guardSet = [d]
and212.guardSet = [b]
and222.guardSet = [bprime]
constraint2.guardSet = [a]

or112.children = [and112, and122]
or212.children = [and212, and222]
and212.children = [or112]
constraint2.children = [or212]

current = and11
parentOfCurrent = or11
dominantSet = [a, b]
commandSet = [d]
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
