from Node import Node

def gather_junctors(current_node:Node, parent_node:Node):
    match current_node.node_type:
        case 'ROOT':
            current_node.node_type = 'AND'
            current_node.guard_set = []
            gather_junctors(current_node.right, current_node)
            return current_node
        case 'AND'|'OR':
            if current_node.node_type == parent_node.node_type:
                gather_junctors(current_node.right, current_node)
                gather_junctors(current_node.left,current_node)
                
            