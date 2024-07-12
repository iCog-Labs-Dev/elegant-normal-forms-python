def print_tree(node, level=0, side=""):
    if node is None:
        return
    print("    " * level + f"[{side}{level}]", node.value)
    print_tree(node.left, level + 1, "L")
    print_tree(node.right, level + 1, "R")
