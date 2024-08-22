# Function to check  All terminal AND nodes have non-empty guard sets
def isEmptyGuardsetTerminal(node: TreeNode):
    if node.type == NodeType.AND and not node.children:
        return len(node.guardSet) > 0
    for child in node.children:
        if not isEmptyGuardsetTerminal(child): 
            return False
    return True
