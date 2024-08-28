from DataStructures.Trees import *
def parse_tree_to_lisp(node: TreeNode) -> str:
    if node.type == NodeType.LITERAL or (node.type == NodeType.AND and node.children == []):
        return node.value
    elif node.type in {NodeType.AND, NodeType.OR, NodeType.NOT}:
        operator = node.type.value
        children_exprs = [parse_tree_to_lisp(child) for child in node.children]
        guard_exprs = [parse_tree_to_lisp(guard) for guard in node.guardSet]
        print(node.guardSet)
        return f"({operator} {' '.join(children_exprs)}{' '.join(guard_exprs)})"
    elif node.type == NodeType.ROOT:
        return parse_tree_to_lisp(node.children[0]) if node.children else ""
    return ""


        


        