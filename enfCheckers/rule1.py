from DataStructures.Trees import NodeType, TreeNode
from Utilities.HelperFunctions import union


def check_branch_set_consistency(branch_set: list[TreeNode]) -> bool:
    """Check if a branch set is consistent."""
    literals = set()
    negated_literals = set()

    for node in branch_set:
        if node.type == NodeType.LITERAL:
            if node.constraint:
                literals.add(node.value)
            else:
                negated_literals.add(node.value)

    # Check for any literal that is both in literals and negated_literals
    for literal in literals:
        if literal in negated_literals:
            return False

    return True


def rule1(node: TreeNode, branch_set: list[TreeNode] | None = None) -> bool:
    """Gather guard sets and constraints from the root to each leaf and check for consistency."""
    if branch_set is None:
        branch_set = []

    # If it's an AND node, we gather guard sets from it
    if node.type == NodeType.AND:
        # Convert guard sets to TreeNode and add to branch set
        branch_set = union(
            branch_set,
            [TreeNode(guard.value, guard.constraint) for guard in node.guardSet],
        )

    # If we reach a leaf node, check for consistency
    if not node.children:
        return check_branch_set_consistency(branch_set)

    # Recursively check  all childrens
    for child in node.children:
        if not rule1(child, branch_set.copy()):
            return False

    return True
